# generated from examples/01ref.yaml
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


class Name(Visitor):
    _schema_type = 'string'
    _roles = ['has_name', 'primitive_type']
    _uid = '/examples/01ref.yaml#/definitions/name'

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Name', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: simplify

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Name')
        if self.node is not None:
            self.node.attach(ctx, d, self)



class Person(Visitor):
    _schema_type = 'object'
    _roles = ['has_name', 'has_properties']
    _uid = '/examples/01ref.yaml#/definitions/person'
    _properties = ['age', 'name']
    _links = ['name']

    @reify
    def name(self):
        return runtime.resolve_visitor('name', cls=Name, logger=logger)

    @reify
    def _properties_visitor_mapping(self):
        return {
            'name': self.name,
        }

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Person', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Person')
        if self.node is not None:
            self.node.attach(ctx, d, self)

        runtime.run_properties(ctx, d, visitor_mapping=self._properties_visitor_mapping)



class Toplevel(Visitor):
    _schema_type = 'object'
    _roles = ['has_properties', 'toplevel_properties']
    _uid = '/examples/01ref.yaml#/'
    _properties = ['father']
    _links = ['father']

    @reify
    def father(self):
        return runtime.resolve_visitor('father', cls=Person, logger=logger)

    @reify
    def _properties_visitor_mapping(self):
        return {
            'father': self.father,
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
