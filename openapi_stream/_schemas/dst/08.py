# generated from examples/08anonymous_one-of.yaml
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


class PositiveInt(Visitor):
    _schema_type = 'integer'
    _roles = ['has_name', 'new_type']
    _uid = '/examples/08anonymous_one-of.yaml#/definitions/positiveInt'

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.PositiveInt', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'PositiveInt')
        if self.node is not None:
            self.node.attach(ctx, d, self)



class Structure(Visitor):
    _schema_type = 'object'
    _roles = ['has_name', 'has_properties']
    _uid = '/examples/08anonymous_one-of.yaml#/definitions/structure'
    _properties = ['xof']
    _links = ['xof']

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Structure', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Structure')
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if 'xof' in d:
            ctx.run('xof', self.xof.visit, d['xof'])

    # anonymous definition for 'xof' (TODO: nodename)
    class _Xof(Visitor):
        _schema_type = 'oneOf'
        _roles = ['combine_type', 'has_expanded']
        _uid = '/examples/08anonymous_one-of.yaml#/definitions/structure/xof'
        _xxx_of_definitions = [{'$ref': '#/definitions/2'}, {'$ref': '#/definitions/3'}, {'$ref': '#/definitions/1'}]

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Structure._Xof', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, '#/definitions/2'):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, '#/definitions/3'):
                return ctx.run(None, self.oneOf1.visit, d)
            if _case.when(d, '#/definitions/1'):
                return ctx.run(None, self.oneOf2.visit, d)
            raise ValueError('unexpected value')  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_Xof')
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor('oneOf0', cls=Structure._Xof._OneOfx00, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor('oneOf1', cls=Structure._Xof._OneOfx01, logger=logger)

        @reify
        def oneOf2(self):
            return runtime.resolve_visitor('oneOf2', cls=PositiveInt, logger=logger)

        # anonymous definition for 'oneOf/0' (TODO: nodename)
        class _OneOfx00(Visitor):
            _schema_type = 'unknown'
            _roles = ['child_of_xxx_of']
            _uid = '/examples/08anonymous_one-of.yaml#/definitions/structure/xof/oneOf/0'

            @reify
            def node(self):
                return runtime.resolve_node('.nodes.Structure._Xof._OneOfx00', here=__name__, logger=logger)

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: remove this code

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", '_OneOfx00')
                if self.node is not None:
                    self.node.attach(ctx, d, self)


        @reify
        def oneOfx00(self):
            return runtime.resolve_visitor('oneOf/0', cls=Structure._Xof._OneOfx00, logger=logger)

        # anonymous definition for 'oneOf/1' (TODO: nodename)
        class _OneOfx01(Visitor):
            _schema_type = 'object'
            _roles = ['child_of_xxx_of', 'has_properties']
            _uid = '/examples/08anonymous_one-of.yaml#/definitions/structure/xof/oneOf/1'
            _properties = ['value']

            @reify
            def node(self):
                return runtime.resolve_node('.nodes.Structure._Xof._OneOfx01', here=__name__, logger=logger)

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: remove this code

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", '_OneOfx01')
                if self.node is not None:
                    self.node.attach(ctx, d, self)


        @reify
        def oneOfx01(self):
            return runtime.resolve_visitor('oneOf/1', cls=Structure._Xof._OneOfx01, logger=logger)


    @reify
    def xof(self):
        return runtime.resolve_visitor('xof', cls=Structure._Xof, logger=logger)



class Toplevel(Visitor):
    _schema_type = 'object'
    _roles = ['has_properties', 'toplevel_properties']
    _uid = '/examples/08anonymous_one-of.yaml#/'
    _properties = ['structure']
    _links = ['structure']

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Toplevel', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Toplevel')
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if 'structure' in d:
            ctx.run('structure', self.structure.visit, d['structure'])

    @reify
    def structure(self):
        return runtime.resolve_visitor('structure', cls=Structure, logger=logger)



# fmt: off
_case = runtime.Case({'definitions': {'1': {'type': 'integer', 'minimum': 0}, '2': {'type': 'bool'}, '3': {'type': 'object', 'properties': {'value': {'type': 'integer'}}}}})
# fmt: on
