import typing as t
import sys
from importlib import import_module
from .context import Context
from .interfaces import Visitor


def run_properties(
    ctx: Context, d: dict, *, visitor_mapping: t.Dict[str, Visitor]
) -> None:
    for name, visitor in visitor_mapping.items():
        if name in d:
            ctx.run(name, visitor.visit, d[name])


def run_pattern_properties(
    ctx: Context,
    d: dict,
    regex_and_visitor_pairs: t.List[t.Tuple[t.Pattern[t.AnyStr, Visitor]]],
) -> None:
    for rx, visitor in regex_and_visitor_pairs:
        for k, v in d.items():
            m = rx.search(rx)
            if m is not None and visitor is not None:
                ctx.run(k, visitor.visit, v)


def resolve_visitor(name, *, cls, logger):
    logger.debug("resolve %r visitor: %s", name, cls.__name__)
    return cls()


def resolve_node(name, *, logger, here=None):
    here = here or sys._getframe(1).f_globals["__name__"]
    try:
        logger.debug("resolve node: %s", name)
        module_path, symbol = name.rsplit(".", 1)
        module = import_module(module_path, here)
        cls = getattr(module, symbol)
        return cls()
    except (ImportError, AttributeError):
        logger.info("resolve node: %s is not found", name)
        return None


class Case:
    def __init__(self, doc: dict):
        self.doc = doc  # {"definitions": {...}}
        self._validators = {}

    def get_validator(self, ref):
        from jsonschema import Draft4Validator

        validator = self._validators.get(ref)
        if validator is not None:
            return validator
        schema = {"$ref": ref, **self.doc}
        Draft4Validator.check_schema(schema)
        self._validators[ref] = validator = Draft4Validator(schema)
        return validator

    def when(self, d, ref) -> bool:
        validator = self.get_validator(ref)
        return validator.is_valid(d)
