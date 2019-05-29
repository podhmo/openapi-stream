# generated from examples/05patternProperties.yaml
from logging import getLogger
from openapi_stream.interfaces import (
    Visitor
)
import re
from openapi_stream import (
    runtime
)
from dictknife.langhelpers import reify
from openapi_stream.context import Context


logger = getLogger(__name__)  # noqa


class Schema(Visitor):
    _schema_type = 'object'
    _roles = ['has_extra_properties', 'has_name', 'has_properties']
    _uid = '/examples/05patternProperties.yaml#/definitions/Schema'
    _properties = ['description', 'type']
    _extra_properties = ['additionalProperties', 'patternProperties']

    @reify
    def _pattern_properties_visitor_pairs(self):
        return [
            (re.compile('^x-'), runtime.resolve_visitor('^x-', cls=Schema._PatternPropertiesx0xx1, logger=logger)),
        ]

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Schema', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Schema')
        if self.node is not None:
            self.node.attach(ctx, d, self)

        runtime.run_pattern_properties(ctx, d, self._pattern_properties_visitor_pairs)

        # additionalProperties
        for k, v in d.items():
            if k in self._properties:
                continue
            for rx, visitor in self._pattern_properties_visitor_pairs:
                m = rx.search(rx)
                if m is not None:
                    continue
            logger.warning('unexpected property is found: %r, where=%s', k, self.__class__.__name__)

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternPropertiesx0xx1(Visitor):
        _schema_type = 'any'
        _roles = ['field_of_something']
        _uid = '/examples/05patternProperties.yaml#/definitions/Schema/patternProperties/^x-'

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._PatternPropertiesx0xx1', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_PatternPropertiesx0xx1')
            if self.node is not None:
                self.node.attach(ctx, d, self)


    @reify
    def patternPropertiesx0xx1(self):
        return runtime.resolve_visitor('patternProperties/^x-', cls=Schema._PatternPropertiesx0xx1, logger=logger)



class Point(Visitor):
    _schema_type = 'integer'
    _roles = ['has_name', 'primitive_type']
    _uid = '/examples/05patternProperties.yaml#/definitions/Point'

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Point', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: simplify

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Point')
        if self.node is not None:
            self.node.attach(ctx, d, self)



class Points(Visitor):
    _schema_type = 'object'
    _roles = ['has_extra_properties', 'has_name']
    _uid = '/examples/05patternProperties.yaml#/definitions/Points'
    _extra_properties = ['patternProperties']

    @reify
    def _pattern_properties_visitor_pairs(self):
        return [
            (re.compile('^point[0-9]+'), runtime.resolve_visitor('^point[0-9]+', cls=Point, logger=logger)),
        ]

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Points', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Points')
        if self.node is not None:
            self.node.attach(ctx, d, self)

        runtime.run_pattern_properties(ctx, d, self._pattern_properties_visitor_pairs)



class Toplevel(Visitor):
    _schema_type = 'object'
    _roles = ['has_properties', 'toplevel_properties']
    _uid = '/examples/05patternProperties.yaml#/'
    _properties = ['points', 'schema']
    _links = ['schema', 'points']

    @reify
    def schema(self):
        return runtime.resolve_visitor('schema', cls=Schema, logger=logger)

    @reify
    def points(self):
        return runtime.resolve_visitor('points', cls=Points, logger=logger)

    @reify
    def _properties_visitor_mapping(self):
        return {
            'schema': self.schema,
            'points': self.points,
        }

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Toplevel', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Toplevel')
        if self.node is not None:
            self.node.attach(ctx, d, self)

        runtime.run_properties(ctx, d, visitor_mapping=self._properties_visitor_mapping)
