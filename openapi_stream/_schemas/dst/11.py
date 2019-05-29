# generated from examples/11toplevel-pattern-properties.yaml
from logging import getLogger
from openapi_stream.interfaces import (
    Visitor
)
from openapi_stream import (
    runtime
)
from dictknife.langhelpers import reify
from openapi_stream.context import Context


logger = getLogger(__name__)  # noqa


class Toplevel(Visitor):
    _schema_type = 'object'
    _roles = ['has_extra_properties', 'has_properties', 'toplevel_properties']
    _uid = '/examples/11toplevel-pattern-properties.yaml#/'
    _properties = ['openapi']
    _extra_properties = ['additionalProperties', 'patternProperties']

    @reify
    def _pattern_properties_regexes(self):
        import re
        return [
            (re.compile('^x-'), runtime.resolve_visitor('^x-', cls=Toplevel._PatternPropertiesx0xx1, logger=logger)),
        ]

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Toplevel', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Toplevel')
        if self.node is not None:
            self.node.attach(ctx, d, self)

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(rx)
                if m is not None and visitor is not None:
                    ctx.run(k, visitor.visit, v)

        # additionalProperties
        for k, v in d.items():
            if k in self._properties:
                continue
            for rx, visitor in self._pattern_properties_regexes:
                m = rx.search(rx)
                if m is not None:
                    continue
            logger.warning('unexpected property is found: %r, where=%s', k, self.__class__.__name__)

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternPropertiesx0xx1(Visitor):
        _schema_type = 'any'
        _roles = ['field_of_something', 'toplevel_properties']
        _uid = '/examples/11toplevel-pattern-properties.yaml#/patternProperties/^x-'

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Toplevel._PatternPropertiesx0xx1', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_PatternPropertiesx0xx1')
            if self.node is not None:
                self.node.attach(ctx, d, self)


    @reify
    def patternPropertiesx0xx1(self):
        return runtime.resolve_visitor('patternProperties/^x-', cls=Toplevel._PatternPropertiesx0xx1, logger=logger)