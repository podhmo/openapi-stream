# generated from examples/03one-of.yaml
from logging import getLogger
from openapi_stream.interfaces import (
    Visitor
)
from openapi_stream import (
    runtime
)
from dictknife.langhelpers import reify
from openapi_stream.context import Context
import re


logger = getLogger(__name__)  # noqa


class Reference(Visitor):
    _schema_type = 'object'
    _roles = ['has_name', 'has_properties']
    _uid = '/examples/03one-of.yaml#/definitions/Reference'
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
    _roles = ['has_name', 'has_properties']
    _uid = '/examples/03one-of.yaml#/definitions/Schema'
    _properties = ['additionalProperties', 'patternProperties', 'properties', 'type']
    _links = ['patternProperties', 'properties', 'additionalProperties']

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Schema', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Schema')
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if 'patternProperties' in d:
            ctx.run('patternProperties', self.patternProperties.visit, d['patternProperties'])
        if 'properties' in d:
            ctx.run('properties', self.properties.visit, d['properties'])
        if 'additionalProperties' in d:
            ctx.run('additionalProperties', self.additionalProperties.visit, d['additionalProperties'])

    # anonymous definition for 'properties' (TODO: nodename)
    class _Properties(Visitor):
        _schema_type = 'object'
        _roles = ['field_of_something', 'has_extra_properties']
        _uid = '/examples/03one-of.yaml#/definitions/Schema/properties'
        _extra_properties = ['patternProperties']

        @reify
        def _pattern_properties_regexes(self):
            return [
                (re.compile('^[a-zA-Z0-9\\.\\-_]+$'), runtime.resolve_visitor('^[a-zA-Z0-9\\.\\-_]+$', cls=Schema._Properties._PatternProperties_aZAZ09, logger=logger)),
            ]

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._Properties', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_Properties')
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # patternProperties
            for rx, visitor in self._pattern_properties_regexes:
                for k, v in d.items():
                    m = rx.search(rx)
                    if m is not None and visitor is not None:
                        ctx.run(k, visitor.visit, v)

        # anonymous definition for 'patternProperties/^[a-zA-Z0-9\\.\\-_]+$' (TODO: nodename)
        class _PatternProperties_aZAZ09(Visitor):
            _schema_type = 'oneOf'
            _roles = ['combine_type', 'field_of_something', 'has_expanded']
            _uid = '/examples/03one-of.yaml#/definitions/Schema/properties/patternProperties/^[a-zA-Z0-9\\.\\-_]+$'
            _xxx_of_definitions = [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]

            @reify
            def node(self):
                return runtime.resolve_node('.nodes.Schema._Properties._PatternProperties_aZAZ09', here=__name__, logger=logger)

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, '#/definitions/1'):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, '#/definitions/3'):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError('unexpected value')  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", '_PatternProperties_aZAZ09')
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor('oneOf0', cls=Schema, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor('oneOf1', cls=Reference, logger=logger)


        @reify
        def patternProperties_a_zA_Z0_9(self):
            return runtime.resolve_visitor('patternProperties/^[a-zA-Z0-9\\.\\-_]+$', cls=Schema._Properties._PatternProperties_aZAZ09, logger=logger)


    @reify
    def properties(self):
        return runtime.resolve_visitor('properties', cls=Schema._Properties, logger=logger)

    # anonymous definition for 'patternProperties' (TODO: nodename)
    class _PatternProperties(Visitor):
        _schema_type = 'object'
        _roles = ['field_of_something', 'has_extra_properties']
        _uid = '/examples/03one-of.yaml#/definitions/Schema/patternProperties'
        _extra_properties = ['additionalProperties']

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._PatternProperties', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_PatternProperties')
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = 'oneOf'
            _roles = ['combine_type', 'field_of_something', 'has_expanded']
            _uid = '/examples/03one-of.yaml#/definitions/Schema/patternProperties/additionalProperties'
            _xxx_of_definitions = [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]

            @reify
            def node(self):
                return runtime.resolve_node('.nodes.Schema._PatternProperties._AdditionalProperties', here=__name__, logger=logger)

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, '#/definitions/1'):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, '#/definitions/3'):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError('unexpected value')  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", '_AdditionalProperties')
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor('oneOf0', cls=Schema, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor('oneOf1', cls=Reference, logger=logger)


        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor('additionalProperties', cls=Schema._PatternProperties._AdditionalProperties, logger=logger)


    @reify
    def patternProperties(self):
        return runtime.resolve_visitor('patternProperties', cls=Schema._PatternProperties, logger=logger)

    # anonymous definition for 'additionalProperties' (TODO: nodename)
    class _AdditionalProperties(Visitor):
        _schema_type = 'oneOf'
        _roles = ['combine_type', 'field_of_something', 'has_expanded']
        _uid = '/examples/03one-of.yaml#/definitions/Schema/additionalProperties'
        _xxx_of_definitions = [{'$ref': '#/definitions/15'}, {'$ref': '#/definitions/3'}, {'$ref': '#/definitions/3'}]

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._AdditionalProperties', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, '#/definitions/15'):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, '#/definitions/3'):
                return ctx.run(None, self.oneOf1.visit, d)
            if _case.when(d, '#/definitions/3'):
                return ctx.run(None, self.oneOf2.visit, d)
            raise ValueError('unexpected value')  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_AdditionalProperties')
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor('oneOf0', cls=Schema._AdditionalProperties._OneOf_0, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor('oneOf1', cls=Schema, logger=logger)

        @reify
        def oneOf2(self):
            return runtime.resolve_visitor('oneOf2', cls=Reference, logger=logger)

        # anonymous definition for 'oneOf/0' (TODO: nodename)
        class _OneOf_0(Visitor):
            _schema_type = 'boolean'
            _roles = ['child_of_xxx_of', 'primitive_type']
            _uid = '/examples/03one-of.yaml#/definitions/Schema/additionalProperties/oneOf/0'

            @reify
            def node(self):
                return runtime.resolve_node('.nodes.Schema._AdditionalProperties._OneOf_0', here=__name__, logger=logger)

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: simplify

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", '_OneOf_0')
                if self.node is not None:
                    self.node.attach(ctx, d, self)


        @reify
        def oneOf_0(self):
            return runtime.resolve_visitor('oneOf/0', cls=Schema._AdditionalProperties._OneOf_0, logger=logger)


    @reify
    def additionalProperties(self):
        return runtime.resolve_visitor('additionalProperties', cls=Schema._AdditionalProperties, logger=logger)



class Toplevel(Visitor):
    _schema_type = 'object'
    _roles = ['has_properties', 'toplevel_properties']
    _uid = '/examples/03one-of.yaml#/'
    _properties = ['definitions', 'properties', 'type']
    _links = ['definitions', 'properties']

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Toplevel', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Toplevel')
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if 'definitions' in d:
            ctx.run('definitions', self.definitions.visit, d['definitions'])
        if 'properties' in d:
            ctx.run('properties', self.properties.visit, d['properties'])

    # anonymous definition for 'properties' (TODO: nodename)
    class _Properties(Visitor):
        _schema_type = 'object'
        _roles = ['has_extra_properties', 'toplevel_properties']
        _uid = '/examples/03one-of.yaml#/properties'
        _extra_properties = ['patternProperties']

        @reify
        def _pattern_properties_regexes(self):
            return [
                (re.compile('^[a-zA-Z0-9\\.\\-_]+$'), runtime.resolve_visitor('^[a-zA-Z0-9\\.\\-_]+$', cls=Toplevel._Properties._PatternProperties_aZAZ09, logger=logger)),
            ]

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Toplevel._Properties', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_Properties')
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # patternProperties
            for rx, visitor in self._pattern_properties_regexes:
                for k, v in d.items():
                    m = rx.search(rx)
                    if m is not None and visitor is not None:
                        ctx.run(k, visitor.visit, v)

        # anonymous definition for 'patternProperties/^[a-zA-Z0-9\\.\\-_]+$' (TODO: nodename)
        class _PatternProperties_aZAZ09(Visitor):
            _schema_type = 'oneOf'
            _roles = ['combine_type', 'field_of_something', 'has_expanded', 'toplevel_properties']
            _uid = '/examples/03one-of.yaml#/properties/patternProperties/^[a-zA-Z0-9\\.\\-_]+$'
            _xxx_of_definitions = [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]

            @reify
            def node(self):
                return runtime.resolve_node('.nodes.Toplevel._Properties._PatternProperties_aZAZ09', here=__name__, logger=logger)

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, '#/definitions/1'):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, '#/definitions/3'):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError('unexpected value')  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", '_PatternProperties_aZAZ09')
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor('oneOf0', cls=Schema, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor('oneOf1', cls=Reference, logger=logger)


        @reify
        def patternProperties_a_zA_Z0_9(self):
            return runtime.resolve_visitor('patternProperties/^[a-zA-Z0-9\\.\\-_]+$', cls=Toplevel._Properties._PatternProperties_aZAZ09, logger=logger)


    @reify
    def properties(self):
        return runtime.resolve_visitor('properties', cls=Toplevel._Properties, logger=logger)

    # anonymous definition for 'definitions' (TODO: nodename)
    class _Definitions(Visitor):
        _schema_type = 'object'
        _roles = ['has_extra_properties']
        _uid = '/examples/03one-of.yaml#/definitions'
        _extra_properties = ['patternProperties']

        @reify
        def _pattern_properties_regexes(self):
            return [
                (re.compile('^[a-zA-Z0-9\\.\\-_]+$'), runtime.resolve_visitor('^[a-zA-Z0-9\\.\\-_]+$', cls=Schema, logger=logger)),
            ]

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Toplevel._Definitions', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_Definitions')
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # patternProperties
            for rx, visitor in self._pattern_properties_regexes:
                for k, v in d.items():
                    m = rx.search(rx)
                    if m is not None and visitor is not None:
                        ctx.run(k, visitor.visit, v)


    @reify
    def definitions(self):
        return runtime.resolve_visitor('definitions', cls=Toplevel._Definitions, logger=logger)



# fmt: off
_case = runtime.Case({'definitions': {'1': {'type': 'object', 'properties': {'type': {'type': 'string'}, 'patternProperties': {'type': 'object', 'additionalProperties': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}}, 'properties': {'type': 'object', 'patternProperties': {'^[a-zA-Z0-9\\.\\-_]+$': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}}}, 'additionalProperties': {'oneOf': [{'$ref': '#/definitions/2'}, {'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}}, 'required': ['type']}, '2': {'type': 'boolean'}, '3': {'type': 'object', 'properties': {'$ref': {'type': 'string', 'format': 'uniref'}}, 'required': ['$ref']}, '15': {'type': 'boolean'}}})
# fmt: on
