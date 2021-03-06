# generated from examples/02one-of.yaml
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


class One(Visitor):
    _schema_type = 'object'
    _roles = ['has_name', 'has_properties']
    _uid = '/examples/02one-of.yaml#/definitions/one'
    _properties = ['one']

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.One', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'One')
        if self.node is not None:
            self.node.attach(ctx, d, self)



class Twotwo(Visitor):
    _schema_type = 'object'
    _roles = ['has_name', 'has_properties']
    _uid = '/examples/02one-of.yaml#/definitions/twotwo'
    _properties = ['two']

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Twotwo', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Twotwo')
        if self.node is not None:
            self.node.attach(ctx, d, self)



class Value(Visitor):
    _schema_type = 'oneOf'
    _roles = ['combine_type', 'has_expanded', 'has_name']
    _uid = '/examples/02one-of.yaml#/definitions/value'
    _xxx_of_definitions = [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/2'}]

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Value', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        # for oneOf (xxx: _case is module global)
        if _case.when(d, '#/definitions/1'):
            return ctx.run(None, self.oneOf0.visit, d)
        if _case.when(d, '#/definitions/2'):
            return ctx.run(None, self.oneOf1.visit, d)
        raise ValueError('unexpected value')  # todo gentle message

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Value')
        if self.node is not None:
            self.node.attach(ctx, d, self)

    @reify
    def oneOf0(self):
        return runtime.resolve_visitor('oneOf0', cls=One, logger=logger)

    @reify
    def oneOf1(self):
        return runtime.resolve_visitor('oneOf1', cls=Twotwo, logger=logger)



class Toplevel(Visitor):
    _schema_type = 'object'
    _roles = ['has_properties', 'toplevel_properties']
    _uid = '/examples/02one-of.yaml#/'
    _properties = ['value']
    _links = ['value']

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Toplevel', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Toplevel')
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if 'value' in d:
            ctx.run('value', self.value.visit, d['value'])

    @reify
    def value(self):
        return runtime.resolve_visitor('value', cls=Value, logger=logger)



# fmt: off
_case = runtime.Case({'definitions': {'1': {'type': 'object', 'properties': {'one': {'type': 'string'}}}, '2': {'type': 'object', 'properties': {'two': {'type': 'string'}}}}})
# fmt: on
