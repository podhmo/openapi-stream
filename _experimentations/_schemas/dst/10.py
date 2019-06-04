# generated from examples/10use-reserved-word.yaml
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


class Reference(Visitor):
    _schema_type = 'object'
    _roles = ['has_name', 'has_properties']
    _uid = '/examples/10use-reserved-word.yaml#/definitions/Reference'
    _properties = ['$ref']

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Reference', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Reference')
        if self.node is not None:
            self.node.attach(ctx, d, self)



class Schema(Visitor):
    _schema_type = 'object'
    _roles = ['has_extra_properties', 'has_name', 'has_properties']
    _uid = '/examples/10use-reserved-word.yaml#/definitions/Schema'
    _properties = ['not', 'title']
    _extra_properties = ['additionalProperties']
    _links = ['not']

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Schema', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Schema')
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if 'not' in d:
            ctx.run('not', self.not_.visit, d['not'])

        # additionalProperties
        for k, v in d.items():
            if k in self._properties:
                continue
            logger.warning('unexpected property is found: %r, where=%s', k, self.__class__.__name__)

    # anonymous definition for 'not' (TODO: nodename)
    class _Not(Visitor):
        _schema_type = 'oneOf'
        _roles = ['combine_type', 'has_expanded']
        _uid = '/examples/10use-reserved-word.yaml#/definitions/Schema/not'
        _xxx_of_definitions = [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/2'}]

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._Not', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, '#/definitions/1'):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, '#/definitions/2'):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError('unexpected value')  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_Not')
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor('oneOf0', cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor('oneOf1', cls=Reference, logger=logger)


    @reify
    def not_(self):
        return runtime.resolve_visitor('not', cls=Schema._Not, logger=logger)



class Toplevel(Visitor):
    _schema_type = 'object'
    _roles = ['has_extra_properties', 'has_properties', 'toplevel_properties']
    _uid = '/examples/10use-reserved-word.yaml#/'
    _properties = ['schema', 'version']
    _extra_properties = ['additionalProperties']
    _links = ['schema']

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Toplevel', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Toplevel')
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if 'schema' in d:
            ctx.run('schema', self.schema.visit, d['schema'])

        # additionalProperties
        for k, v in d.items():
            if k in self._properties:
                continue
            logger.warning('unexpected property is found: %r, where=%s', k, self.__class__.__name__)

    @reify
    def schema(self):
        return runtime.resolve_visitor('schema', cls=Schema, logger=logger)



# fmt: off
_case = runtime.Case({'definitions': {'1': {'additionalProperties': False, 'properties': {'not': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/2'}]}, 'title': {'type': 'string'}}, 'type': 'object'}, '2': {'properties': {'$ref': {'format': 'uriref', 'type': 'string'}}, 'required': ['$ref'], 'type': 'object'}}})
# fmt: on
