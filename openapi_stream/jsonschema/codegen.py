import sys  # noqa
import typing as t
import re
import json
import logging
import keyword
from collections import defaultdict
from prestring.python import Module
from prestring.naming import pascalcase
from openapi_stream import Event
from openapi_stream.jsonschema import ToplevelVisitor
from openapi_stream.jsonschema import names

logger = logging.getLogger(__name__)


class _LazyName:
    def __init__(self, callable: t.Callable[[], str]) -> None:
        self.callable = callable

    def __str__(self) -> str:
        return self.callable()


# todo: toplevel $ref
# todo: drop link of primitive types
# todo: required support
# todo: enum support(?)
# todo: additionalProperties (schema)
# todo: anonymous definition(nested definition)
# todo: anonymous patternPropertites
# todo: anonymous definition(oneOf, anyof, allOf)
# todo: rename python reserved word


class _PythonNameNormalizer:
    def __init__(self):
        self.unpython_name_map = defaultdict(lambda: f"x{len(self.unpython_name_map)}")
        self.unpython_rx = re.compile(r"^(?P<number>\d)+|(?P<unpython>[^a-zA-Z0-9_]+)")

    def __call__(self, name):
        if self.unpython_rx.search(name) is not None:
            name = self.unpython_rx.sub(self._replace, name).rstrip("_")
        if keyword.iskeyword(name):
            name = name + "_"
        return name

    def _replace(self, match: re.Match):
        md = match.groupdict()
        if md["number"] is not None:
            return "n{md['number']}"
        return "_"


class Helper:
    def __init__(self):
        self.to_python_name = _PythonNameNormalizer()

    def classname(self, ev: Event, *, name: str = None) -> str:
        retname = name or ev.get_annotated(names.annotations.name)
        return self.to_python_name(pascalcase(retname))

    def methodname(self, name: str) -> str:
        return self.to_python_name(name)

    def create_submodule(self, m) -> Module:
        sm = m.submodule()
        sm.import_area = m.import_area
        return sm

    def has_pattern_properties(self, ev: Event) -> bool:
        return (
            names.roles.has_extra_properties in ev.roles
            and "patternProperties" in ev.data
        )

    def has_additional_properties(self, ev: Event) -> bool:
        return (
            names.roles.has_extra_properties in ev.roles
            and "additionalProperties" in ev.data
        )

    def iterate_links(self, ev: Event) -> t.Iterable[t.Tuple[str, str]]:
        return ev.get_annotated(names.annotations.links) or []

    def iterate_xxx_of_links(self, ev: Event) -> t.Iterable[t.Tuple[str, str]]:
        return ev.get_annotated(names.annotations.xxx_of_links) or []

    def is_link_of_anonymous_definition(self, uid):
        return uid is None


class NameManager:  # todo: rename
    def __init__(self, *, helper: Helper):
        self.visitor_class_names: t.Dict[str, t.Tuple[str, str]] = {}
        self.helper = helper

    def iterate_clssname_and_prefix_pairs(self) -> t.Iterator[t.Tuple[str, str]]:
        return self.visitor_class_names.items()

    def add_visitor_name(self, ev: Event, clsname, prefix: str = ""):
        self.visitor_class_names[ev.uid] = (clsname, prefix)

    def __contains__(self, uid: str) -> bool:
        return uid in self.visitor_class_names

    def create_lazy_visitor_name(self, uid: str) -> _LazyName:
        assert uid is not None

        def to_str(uid: str = uid):
            # name = self.visitor_class_names[uid]
            name, prefix = self.visitor_class_names.get(uid) or (None, "")
            if name is None:
                logger.warning("missing, resolve clasname: %s -> %s", uid, name)
                name = "<missing>"
            else:
                name = self.helper.methodname(name)
                if prefix:
                    name = prefix + name
                logger.debug("resolve clasname: %s -> %s", uid, name)
            return name

        return _LazyName(to_str)


class CaseDefinitionsManager:
    def __init__(self) -> None:
        self.definitions = {}  # all xxx_of definitions

    def add_definitions(self, defs: dict) -> None:
        self.definitions.update(defs)

    @property
    def has_definitions(self) -> bool:
        return bool(self.definitions)


class Emitter:  # todo: rename
    def emit_data(self, m, fmt: str, d: dict, *, nofmt=False):
        """emit data as python literal"""
        if nofmt:
            m.stmt("# fmt: off")
        m.stmt(fmt, json.loads(json.dumps(d)))
        if nofmt:
            m.stmt("# fmt: on")


class Logging:
    def __init__(self, m, *, enable: bool):
        self.enable = enable

        if not hasattr(m, "import_area"):  # xxx:
            m.import_area = m.submodule()

        if self.enable:
            m.import_area.from_("logging", "getLogger")
            m.stmt("logger = getLogger(__name__)  # noqa")
            m.sep()

    def log(self, m, fmt, *args, **kwargs):
        if self.enable:
            m.stmt(fmt, *args, **kwargs)


class Generator:
    def __init__(self, m, logging_enable=True):
        self.m = m

        self.logging = Logging(m, enable=logging_enable)
        self.emitter = Emitter()

        self.helper = Helper()
        self.name_manager = NameManager(helper=self.helper)

        self.case_definitions_manager = CaseDefinitionsManager()

        # xxx:
        self._end_of_private_visit_method_conts = {}  # classname -> m.submodule()
        self._end_of_class_definition_conts = {}  # classname -> m.submodule()

    def generate_class(
        self, ev: Event, *, m=None, clsname: str = None, prefix: str = ""
    ) -> None:
        m = m or self.m
        clsname = clsname or self.helper.classname(ev)
        self.name_manager.add_visitor_name(ev, clsname, prefix=prefix)

        m.import_area.from_("openapi_stream.interfaces", "Visitor")
        with m.class_(clsname, "Visitor"):
            self._gen_headers(ev, m=m)

            if self.helper.has_pattern_properties(ev):
                self._gen_pattern_properties_regexes(ev, m=m)

            self._gen_node_property(ev, m=m)
            self._gen_visit_method(ev, m=m)
            self._gen_visit_private_method(ev, clsname=clsname, m=m)

            # reify properties
            self._gen_properties_visitors(ev, m=m)
            if ev.name in (names.types.oneOf, names.types.allOf, names.types.anyOf):
                self._gen_xxx_of_visitors(ev, m=m)

            # xxx:
            self._end_of_class_definition_conts[ev.uid] = self.helper.create_submodule(
                m
            )

    def _gen_headers(self, ev: Event, *, m) -> None:
        m.stmt(f"_schema_type = {ev.name!r}")
        m.stmt(f"_roles = {sorted(ev.roles)!r}")

        m.stmt(f"_uid = {ev.uid!r}")
        if names.roles.has_properties in ev.roles:
            m.stmt(
                f"_properties = {sorted(ev.get_annotated(names.annotations.properties))!r}"
            )
        if names.roles.has_extra_properties in ev.roles:
            data = ev.get_annotated(names.annotations.extra_properties)
            self.emitter.emit_data(m, "_extra_properties = {}", sorted(data))

        links = list(self.helper.iterate_links(ev))
        if links:
            m.stmt(
                f"_links = {[name for name, ref in self.helper.iterate_links(ev)]!r}"
            )
        if names.roles.combine_type in ev.roles:
            self.emitter.emit_data(
                m,
                "_xxx_of_definitions = {}",
                ev.get_annotated(names.annotations.expanded)[ev.name],
                nofmt=False,
            )
        m.sep()

    def _gen_pattern_properties_regexes(self, ev: Event, *, m) -> None:
        m.stmt("@reify")
        with m.def_("_pattern_properties_regexes", "self"):
            m.import_area.import_("re")
            m.stmt("return [")
            with m.scope():
                for k, uid in ev.get_annotated(
                    names.annotations.pattern_properties_links
                ):
                    if self.helper.is_link_of_anonymous_definition(uid):
                        uid = f"{ev.uid.rstrip('/')}/patternProperties/{k}"  # xxx

                    lazy_name = self.name_manager.create_lazy_visitor_name(uid)
                    m.stmt(
                        """(re.compile({k!r}), runtime.resolve_visitor({k!r}, cls={cls}, logger=logger)),""",
                        k=k,
                        cls=lazy_name,
                    )
            m.stmt("]")

    def _gen_node_property(self, ev: Event, *, m) -> None:
        lazy_name = self.name_manager.create_lazy_visitor_name(ev.uid)
        m.import_area.from_("openapi_stream", "runtime")
        m.stmt("@reify")
        with m.def_("node", "self"):
            m.stmt(
                "return runtime.resolve_node('.nodes.{cls}', here=__name__, logger=logger)",
                cls=lazy_name,
            )

    def _gen_visit_method(self, ev: Event, *, m) -> None:
        with m.def_("visit", "self", "ctx: Context", "d: dict"):
            if ev.name == names.types.array:
                m.return_("[self._visit(ctx, x) for x in d]")
            elif names.roles.primitive_type in ev.roles:
                # drop schema definitions?
                m.return_("self._visit(ctx, d)  # todo: simplify")
            elif names.roles.combine_type in ev.roles:
                expanded = ev.get_annotated(names.annotations.expanded)
                bodies = {k: v for k, v in expanded.items() if k != "definitions"}
                m.stmt("# for {} (xxx: _case is module global)", ev.name)

                if ev.name == names.types.oneOf:
                    for i, prop in enumerate(bodies[ev.name]):
                        with m.if_(f"_case.when(d, {prop['$ref']!r})"):
                            m.stmt(
                                f"return ctx.run(None, self.{ev.name}{i!r}.visit, d)"
                            )
                    m.stmt(
                        "raise ValueError('unexpected value')  # todo gentle message"
                    )
                elif ev.name == names.types.anyOf:
                    m.stmt("matched = False")
                    for i, prop in enumerate(bodies[ev.name]):
                        with m.if_(f"_case.when(d, {prop['$ref']!r})"):
                            m.stmt("matched = True")
                            m.stmt(f"ctx.run(None, self.{ev.name}{i!r}.visit, d)")
                    with m.if_("not matched"):
                        m.stmt(
                            "raise ValueError('unexpected value')  # todo gentle message"
                        )
                elif ev.name == names.types.allOf:
                    for i, prop in enumerate(bodies[ev.name]):
                        with m.if_(f"not _case.when(d, {prop['$ref']!r})"):
                            m.stmt(
                                "raise ValueError('unexpected value')  # todo gentle message"
                            )
                        m.stmt(f"ctx.run(None, self.{ev.name}{i!r}.visit, d)")
            else:
                m.return_("self._visit(ctx, d)  # todo: remove this code")

    def _gen_visit_private_method(self, ev: Event, *, clsname: str, m) -> None:
        with m.def_("_visit", "self", "ctx: Context", "d: dict"):
            self.logging.log(m, f"""logger.debug("visit: %s", {clsname!r})""")

            with m.if_("self.node is not None"):
                m.stmt("self.node.attach(ctx, d, self)")

            for name, uid in self.helper.iterate_links(ev):
                if self.helper.is_link_of_anonymous_definition(uid):
                    uid = f"{ev.uid}/{name}"
                with m.if_(f"{name!r} in d"):
                    m.stmt(
                        f"ctx.run({name!r}, self.{self.helper.methodname(name)}.visit, d[{name!r}])",
                        name=name,
                    )

            if self.helper.has_pattern_properties(ev):
                m.sep()
                m.stmt("# patternProperties")
                with m.for_("rx, visitor in self._pattern_properties_regexes"):
                    with m.for_("k, v in d.items()"):
                        m.stmt("m = rx.search(k)")
                        with m.if_("m is not None and visitor is not None"):
                            m.stmt("ctx.run(k, visitor.visit, v)")
            if self.helper.has_additional_properties(ev):
                m.sep()
                m.stmt("# additionalProperties")

                def _on_continue():
                    m.stmt("continue")

                if ev.data["additionalProperties"] is False:

                    def _on_continue_with_warning():
                        # m.stmt(f"raise RuntimeError('additionalProperties is False, but unexpected property is found (k=%s, where=%s)' %  (k, self.__class__.__name__))")
                        self.logging.log(
                            m,
                            "logger.warning('unexpected property is found: %r, where=%s', k, self.__class__.__name__)",
                        )
                        m.stmt("continue")

                    _on_continue = _on_continue_with_warning  # noqa

                with m.for_("k, v in d.items()"):
                    with m.if_("k in self._properties"):
                        m.stmt("continue")
                    if self.helper.has_pattern_properties(ev):
                        with m.for_("rx, visitor in self._pattern_properties_regexes"):
                            m.stmt("m = rx.search(rx)")
                            with m.if_("m is not None"):
                                m.stmt("continue")

                    if ev.data["additionalProperties"] is False:
                        self.logging.log(
                            m,
                            "logger.warning('unexpected property is found: %r, where=%s', k, self.__class__.__name__)",
                        )
                    else:
                        m.stmt("ctx.run(k, self.additional_properties.visit, v)")

            # add code, after visited
            self._end_of_private_visit_method_conts[
                ev.uid,
            ] = self.helper.create_submodule(m)

    def _gen_visitor_property(self, ev: Event, *, name: str, uid: str, m) -> None:
        m.import_area.from_("openapi_stream", "runtime")
        m.stmt("@reify")
        with m.def_(self.helper.methodname(name), "self"):
            lazy_link_name = self.name_manager.create_lazy_visitor_name(uid)
            m.stmt(
                "return runtime.resolve_visitor({name!r}, cls={cls}, logger=logger)",
                name=name,
                cls=lazy_link_name,
            )

    def _gen_properties_visitors(self, ev: Event, *, m) -> None:
        for name, uid in self.helper.iterate_links(ev):
            if self.helper.is_link_of_anonymous_definition(uid):
                continue  # generated by delayed stream
            self._gen_visitor_property(ev, name=name, uid=uid, m=m)

    def _gen_xxx_of_visitors(self, ev: Event, *, m) -> None:
        for i, uid in self.helper.iterate_xxx_of_links(ev):
            name = f"{ev.name}{i}"
            if self.helper.is_link_of_anonymous_definition(uid):
                uid = f"{ev.uid}/{ev.name}/{i}"
            self._gen_visitor_property(ev, name=name, uid=uid, m=m)


def main():
    from openapi_stream import main

    m = Module(import_unique=True)
    m.header_area = m.submodule()
    m.import_area = m.submodule()
    m.sep()

    g = Generator(m)
    toplevels: t.List[Event] = []

    stream: t.Iterable[Event] = main(create_visitor=ToplevelVisitor)

    def consume_stream(stream: t.Iterable[Event], *, is_delayed=False) -> t.List[Event]:
        delayed_stream: t.List[Event] = []
        for ev in stream:
            if ev.uid in g.name_manager:
                continue

            if names.roles.has_expanded in ev.roles:
                g.case_definitions_manager.add_definitions(
                    ev.get_annotated(names.annotations.expanded)["definitions"]
                )
            if names.roles.has_name in ev.roles:
                g.generate_class(ev)
                continue

            if not is_delayed:
                if names.roles.toplevel_properties in ev.roles:
                    toplevels.append(ev)  # xxx
                delayed_stream.append(ev)
                continue

            # xxx:
            if (
                ev.name in (names.types.object, names.types.array)
                or names.roles.combine_type in ev.roles
                or names.roles.child_of_xxx_of in ev.roles
                or names.roles.field_of_something in ev.roles
            ):
                uid_and_clsname_pairs = sorted(
                    g.name_manager.iterate_clssname_and_prefix_pairs(),
                    key=lambda pair: len(pair[0]),
                    reverse=True,
                )

                uid = ev.uid
                for parent_uid, (parent_clsname, prefix) in uid_and_clsname_pairs:
                    if uid.startswith(parent_uid):
                        classdef_sm = g._end_of_class_definition_conts[parent_uid]
                        fieldname = uid.replace(parent_uid, "").lstrip("/")
                        clsname = f"_{g.helper.classname(ev, name=fieldname)}"

                        classdef_sm.stmt(
                            f"# anonymous definition for {fieldname!r} (TODO: nodename)"
                        )
                        g.generate_class(
                            ev,
                            clsname=clsname,
                            m=classdef_sm,
                            prefix=f"{prefix}{parent_clsname}.",
                        )

                        # ok: properties
                        # ok:  oneOf, anyof, allof
                        # todo: additionalProperties, patternProperties
                        # assert "/" not in fieldname
                        name = fieldname
                        g._gen_visitor_property(ev, name=name, uid=uid, m=classdef_sm)
                        break
                else:
                    raise RuntimeError(f"unexpected type: {ev.name}")

        return delayed_stream

    delayed_stream = consume_stream(stream, is_delayed=False)

    for ev in toplevels:
        if ev.uid.endswith("#/"):
            g.generate_class(ev, clsname="Toplevel")

    import os.path

    m.header_area.stmt(
        f"# generated from {os.path.relpath(ev.root_file, start=os.getcwd())}"
    )
    m.import_area.from_("dictknife.langhelpers", "reify")
    m.import_area.from_("openapi_stream", "runtime")
    m.import_area.from_("openapi_stream.context", "Context")

    delayed_stream = sorted(delayed_stream, key=lambda ev: len(ev.uid))
    delayed_stream = consume_stream(delayed_stream, is_delayed=True)

    if g.case_definitions_manager.has_definitions:
        data = {"definitions": g.case_definitions_manager.definitions}
        m.import_area.from_("openapi_stream", "runtime")
        g.emitter.emit_data(m, "_case = runtime.Case({})", data, nofmt=True)

    print(m)


if __name__ == "__main__":
    main()
