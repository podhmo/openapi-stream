# generated from examples/07anonymous_nested.yaml
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


class ComplexStructure(Visitor):
    _schema_type = 'object'
    _roles = ['has_name', 'has_properties']
    _uid = '/examples/07anonymous_nested.yaml#/definitions/ComplexStructure'
    _properties = ['people', 'value']
    _links = ['people']

    @reify
    def _properties_visitor_mapping(self):
        return {
            'people': self.people,
        }

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.ComplexStructure', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'ComplexStructure')
        if self.node is not None:
            self.node.attach(ctx, d, self)

        runtime.run_properties(ctx, d, visitor_mapping=self._properties_visitor_mapping)

    # anonymous definition for 'people' (TODO: nodename)
    class _People(Visitor):
        _schema_type = 'array'
        _roles = ['has_extra_properties']
        _uid = '/examples/07anonymous_nested.yaml#/definitions/ComplexStructure/people'
        _extra_properties = ['items']

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.ComplexStructure._People', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_People')
            if self.node is not None:
                self.node.attach(ctx, d, self)

        # anonymous definition for 'items' (TODO: nodename)
        class _Items(Visitor):
            _schema_type = 'object'
            _roles = ['has_properties']
            _uid = '/examples/07anonymous_nested.yaml#/definitions/ComplexStructure/people/items'
            _properties = ['age', 'name']

            @reify
            def node(self):
                return runtime.resolve_node('.nodes.ComplexStructure._People._Items', here=__name__, logger=logger)

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: remove this code

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", '_Items')
                if self.node is not None:
                    self.node.attach(ctx, d, self)


        @reify
        def items(self):
            return runtime.resolve_visitor('items', cls=ComplexStructure._People._Items, logger=logger)


    @reify
    def people(self):
        return runtime.resolve_visitor('people', cls=ComplexStructure._People, logger=logger)



class Toplevel(Visitor):
    _schema_type = 'object'
    _roles = ['has_properties', 'toplevel_properties']
    _uid = '/examples/07anonymous_nested.yaml#/'
    _properties = ['structure']
    _links = ['structure']

    @reify
    def structure(self):
        return runtime.resolve_visitor('structure', cls=ComplexStructure, logger=logger)

    @reify
    def _properties_visitor_mapping(self):
        return {
            'structure': self.structure,
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
