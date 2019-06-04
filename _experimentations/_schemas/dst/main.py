# generated from examples/separated/main.yaml
from logging import getLogger
from openapi_stream.interfaces import (
    Visitor
)
from openapi_stream import (
    runtime
)
import re
from dictknife.langhelpers import reify
from openapi_stream.context import Context


logger = getLogger(__name__)  # noqa


class Reference(Visitor):
    _schema_type = 'object'
    _roles = ['has_name', 'has_properties']
    _uid = '/examples/separated/definitions/Reference.yaml#/definitions/Reference'
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



class Discriminator(Visitor):
    _schema_type = 'object'
    _roles = ['has_name', 'has_properties']
    _uid = '/examples/separated/definitions/Discriminator.yaml#/definitions/Discriminator'
    _properties = ['mapping', 'propertyName']
    _links = ['mapping']

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Discriminator', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Discriminator')
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if 'mapping' in d:
            ctx.run('mapping', self.mapping.visit, d['mapping'])

    # anonymous definition for 'mapping' (TODO: nodename)
    class _Mapping(Visitor):
        _schema_type = 'object'
        _roles = ['has_extra_properties']
        _uid = '/examples/separated/definitions/Discriminator.yaml#/definitions/Discriminator/mapping'
        _extra_properties = ['additionalProperties']

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Discriminator._Mapping', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_Mapping')
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = 'string'
            _roles = ['field_of_something', 'primitive_type']
            _uid = '/examples/separated/definitions/Discriminator.yaml#/definitions/Discriminator/mapping/additionalProperties'

            @reify
            def node(self):
                return runtime.resolve_node('.nodes.Discriminator._Mapping._AdditionalProperties', here=__name__, logger=logger)

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: simplify

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", '_AdditionalProperties')
                if self.node is not None:
                    self.node.attach(ctx, d, self)


        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor('additionalProperties', cls=Discriminator._Mapping._AdditionalProperties, logger=logger)


    @reify
    def mapping(self):
        return runtime.resolve_visitor('mapping', cls=Discriminator._Mapping, logger=logger)



class Schema(Visitor):
    _schema_type = 'object'
    _roles = ['has_extra_properties', 'has_name', 'has_properties']
    _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema'
    _properties = ['additionalProperties', 'allOf', 'anyOf', 'default', 'deprecated', 'description', 'discriminator', 'enum', 'example', 'exclusiveMaximum', 'exclusiveMinimum', 'format', 'items', 'maxItems', 'maxLength', 'maxProperties', 'maximum', 'minItems', 'minLength', 'minProperties', 'minimum', 'multipleOf', 'not', 'nullable', 'oneOf', 'pattern', 'properties', 'readOnly', 'required', 'title', 'type', 'uniqueItems', 'writeOnly']
    _extra_properties = ['additionalProperties', 'patternProperties']
    _links = ['additionalProperties', 'allOf', 'anyOf', 'default', 'discriminator', 'enum', 'example', 'items', 'not', 'oneOf', 'properties', 'required']

    @reify
    def _pattern_properties_regexes(self):
        return [
            (re.compile('^x-'), runtime.resolve_visitor('^x-', cls=Schema._PatternProperties_x, logger=logger)),
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
        if 'additionalProperties' in d:
            ctx.run('additionalProperties', self.additionalProperties.visit, d['additionalProperties'])
        if 'allOf' in d:
            ctx.run('allOf', self.allOf.visit, d['allOf'])
        if 'anyOf' in d:
            ctx.run('anyOf', self.anyOf.visit, d['anyOf'])
        if 'default' in d:
            ctx.run('default', self.default.visit, d['default'])
        if 'discriminator' in d:
            ctx.run('discriminator', self.discriminator.visit, d['discriminator'])
        if 'enum' in d:
            ctx.run('enum', self.enum.visit, d['enum'])
        if 'example' in d:
            ctx.run('example', self.example.visit, d['example'])
        if 'items' in d:
            ctx.run('items', self.items.visit, d['items'])
        if 'not' in d:
            ctx.run('not', self.not_.visit, d['not'])
        if 'oneOf' in d:
            ctx.run('oneOf', self.oneOf.visit, d['oneOf'])
        if 'properties' in d:
            ctx.run('properties', self.properties.visit, d['properties'])
        if 'required' in d:
            ctx.run('required', self.required.visit, d['required'])

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

    @reify
    def discriminator(self):
        return runtime.resolve_visitor('discriminator', cls=Discriminator, logger=logger)

    # anonymous definition for 'not' (TODO: nodename)
    class _Not(Visitor):
        _schema_type = 'oneOf'
        _roles = ['combine_type', 'has_expanded']
        _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/not'
        _xxx_of_definitions = [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._Not', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, '#/definitions/1'):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, '#/definitions/3'):
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

    # anonymous definition for 'enum' (TODO: nodename)
    class _Enum(Visitor):
        _schema_type = 'array'
        _roles = ['has_extra_properties']
        _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/enum'
        _extra_properties = ['items']

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._Enum', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_Enum')
            if self.node is not None:
                self.node.attach(ctx, d, self)


    @reify
    def enum(self):
        return runtime.resolve_visitor('enum', cls=Schema._Enum, logger=logger)

    # anonymous definition for 'allOf' (TODO: nodename)
    class _AllOf(Visitor):
        _schema_type = 'array'
        _roles = ['has_extra_properties']
        _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/allOf'
        _extra_properties = ['items']

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._AllOf', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_AllOf')
            if self.node is not None:
                self.node.attach(ctx, d, self)

        # anonymous definition for 'items' (TODO: nodename)
        class _Items(Visitor):
            _schema_type = 'oneOf'
            _roles = ['combine_type', 'has_expanded']
            _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/allOf/items'
            _xxx_of_definitions = [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]

            @reify
            def node(self):
                return runtime.resolve_node('.nodes.Schema._AllOf._Items', here=__name__, logger=logger)

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, '#/definitions/1'):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, '#/definitions/3'):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError('unexpected value')  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", '_Items')
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor('oneOf0', cls=Schema, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor('oneOf1', cls=Reference, logger=logger)


        @reify
        def items(self):
            return runtime.resolve_visitor('items', cls=Schema._AllOf._Items, logger=logger)


    @reify
    def allOf(self):
        return runtime.resolve_visitor('allOf', cls=Schema._AllOf, logger=logger)

    # anonymous definition for 'anyOf' (TODO: nodename)
    class _AnyOf(Visitor):
        _schema_type = 'array'
        _roles = ['has_extra_properties']
        _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/anyOf'
        _extra_properties = ['items']

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._AnyOf', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_AnyOf')
            if self.node is not None:
                self.node.attach(ctx, d, self)

        # anonymous definition for 'items' (TODO: nodename)
        class _Items(Visitor):
            _schema_type = 'oneOf'
            _roles = ['child_of_xxx_of', 'combine_type', 'has_expanded']
            _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/anyOf/items'
            _xxx_of_definitions = [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]

            @reify
            def node(self):
                return runtime.resolve_node('.nodes.Schema._AnyOf._Items', here=__name__, logger=logger)

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, '#/definitions/1'):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, '#/definitions/3'):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError('unexpected value')  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", '_Items')
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor('oneOf0', cls=Schema, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor('oneOf1', cls=Reference, logger=logger)


        @reify
        def items(self):
            return runtime.resolve_visitor('items', cls=Schema._AnyOf._Items, logger=logger)


    @reify
    def anyOf(self):
        return runtime.resolve_visitor('anyOf', cls=Schema._AnyOf, logger=logger)

    # anonymous definition for 'items' (TODO: nodename)
    class _Items(Visitor):
        _schema_type = 'oneOf'
        _roles = ['combine_type', 'has_expanded']
        _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/items'
        _xxx_of_definitions = [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._Items', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, '#/definitions/1'):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, '#/definitions/3'):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError('unexpected value')  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_Items')
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor('oneOf0', cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor('oneOf1', cls=Reference, logger=logger)


    @reify
    def items(self):
        return runtime.resolve_visitor('items', cls=Schema._Items, logger=logger)

    # anonymous definition for 'oneOf' (TODO: nodename)
    class _OneOf(Visitor):
        _schema_type = 'array'
        _roles = ['has_extra_properties']
        _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/oneOf'
        _extra_properties = ['items']

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._OneOf', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_OneOf')
            if self.node is not None:
                self.node.attach(ctx, d, self)

        # anonymous definition for 'items' (TODO: nodename)
        class _Items(Visitor):
            _schema_type = 'oneOf'
            _roles = ['child_of_xxx_of', 'combine_type', 'has_expanded']
            _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/oneOf/items'
            _xxx_of_definitions = [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]

            @reify
            def node(self):
                return runtime.resolve_node('.nodes.Schema._OneOf._Items', here=__name__, logger=logger)

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, '#/definitions/1'):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, '#/definitions/3'):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError('unexpected value')  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", '_Items')
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor('oneOf0', cls=Schema, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor('oneOf1', cls=Reference, logger=logger)


        @reify
        def items(self):
            return runtime.resolve_visitor('items', cls=Schema._OneOf._Items, logger=logger)


    @reify
    def oneOf(self):
        return runtime.resolve_visitor('oneOf', cls=Schema._OneOf, logger=logger)

    # anonymous definition for 'required' (TODO: nodename)
    class _Required(Visitor):
        _schema_type = 'array'
        _roles = ['has_extra_properties']
        _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/required'
        _extra_properties = ['items']

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._Required', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_Required')
            if self.node is not None:
                self.node.attach(ctx, d, self)


    @reify
    def required(self):
        return runtime.resolve_visitor('required', cls=Schema._Required, logger=logger)

    # anonymous definition for 'properties' (TODO: nodename)
    class _Properties(Visitor):
        _schema_type = 'object'
        _roles = ['field_of_something', 'has_extra_properties']
        _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/properties'
        _extra_properties = ['additionalProperties']

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._Properties', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_Properties')
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
            _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/properties/additionalProperties'
            _xxx_of_definitions = [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]

            @reify
            def node(self):
                return runtime.resolve_node('.nodes.Schema._Properties._AdditionalProperties', here=__name__, logger=logger)

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
            return runtime.resolve_visitor('additionalProperties', cls=Schema._Properties._AdditionalProperties, logger=logger)


    @reify
    def properties(self):
        return runtime.resolve_visitor('properties', cls=Schema._Properties, logger=logger)

    # anonymous definition for 'additionalProperties' (TODO: nodename)
    class _AdditionalProperties(Visitor):
        _schema_type = 'oneOf'
        _roles = ['combine_type', 'field_of_something', 'has_expanded']
        _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/additionalProperties'
        _xxx_of_definitions = [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}, {'$ref': '#/definitions/20'}]

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._AdditionalProperties', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, '#/definitions/1'):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, '#/definitions/3'):
                return ctx.run(None, self.oneOf1.visit, d)
            if _case.when(d, '#/definitions/20'):
                return ctx.run(None, self.oneOf2.visit, d)
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
        def oneOf2(self):
            return runtime.resolve_visitor('oneOf2', cls=Schema._AdditionalProperties._OneOf_2, logger=logger)

        # anonymous definition for 'oneOf/2' (TODO: nodename)
        class _OneOf_2(Visitor):
            _schema_type = 'boolean'
            _roles = ['child_of_xxx_of', 'primitive_type']
            _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/additionalProperties/oneOf/2'

            @reify
            def node(self):
                return runtime.resolve_node('.nodes.Schema._AdditionalProperties._OneOf_2', here=__name__, logger=logger)

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: simplify

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", '_OneOf_2')
                if self.node is not None:
                    self.node.attach(ctx, d, self)


        @reify
        def oneOf_2(self):
            return runtime.resolve_visitor('oneOf/2', cls=Schema._AdditionalProperties._OneOf_2, logger=logger)


    @reify
    def additionalProperties(self):
        return runtime.resolve_visitor('additionalProperties', cls=Schema._AdditionalProperties, logger=logger)

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = 'any'
        _roles = ['field_of_something']
        _uid = '/examples/separated/definitions/Schema.yaml#/definitions/Schema/patternProperties/^x-'

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Schema._PatternProperties_x', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_PatternProperties_x')
            if self.node is not None:
                self.node.attach(ctx, d, self)


    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor('patternProperties/^x-', cls=Schema._PatternProperties_x, logger=logger)



class Components(Visitor):
    _schema_type = 'object'
    _roles = ['has_name', 'has_properties']
    _uid = '/examples/separated/definitions/Components.yaml#/definitions/Components'
    _properties = ['additionalProperties', 'description', 'patternProperties', 'schemas']
    _links = ['patternProperties', 'schemas']

    @reify
    def node(self):
        return runtime.resolve_node('.nodes.Components', here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", 'Components')
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if 'patternProperties' in d:
            ctx.run('patternProperties', self.patternProperties.visit, d['patternProperties'])
        if 'schemas' in d:
            ctx.run('schemas', self.schemas.visit, d['schemas'])

    # anonymous definition for 'schemas' (TODO: nodename)
    class _Schemas(Visitor):
        _schema_type = 'object'
        _roles = ['has_extra_properties']
        _uid = '/examples/separated/definitions/Components.yaml#/definitions/Components/schemas'
        _extra_properties = ['patternProperties']

        @reify
        def _pattern_properties_regexes(self):
            return [
                (re.compile('^[a-zA-Z0-9\\.\\-_]+$'), runtime.resolve_visitor('^[a-zA-Z0-9\\.\\-_]+$', cls=Components._Schemas._PatternProperties_aZAZ09, logger=logger)),
            ]

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Components._Schemas', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_Schemas')
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
            _uid = '/examples/separated/definitions/Components.yaml#/definitions/Components/schemas/patternProperties/^[a-zA-Z0-9\\.\\-_]+$'
            _xxx_of_definitions = [{'$ref': '#/definitions/33'}, {'$ref': '#/definitions/34'}]

            @reify
            def node(self):
                return runtime.resolve_node('.nodes.Components._Schemas._PatternProperties_aZAZ09', here=__name__, logger=logger)

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, '#/definitions/33'):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, '#/definitions/34'):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError('unexpected value')  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", '_PatternProperties_aZAZ09')
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor('oneOf0', cls=Reference, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor('oneOf1', cls=Schema, logger=logger)


        @reify
        def patternProperties_a_zA_Z0_9(self):
            return runtime.resolve_visitor('patternProperties/^[a-zA-Z0-9\\.\\-_]+$', cls=Components._Schemas._PatternProperties_aZAZ09, logger=logger)


    @reify
    def schemas(self):
        return runtime.resolve_visitor('schemas', cls=Components._Schemas, logger=logger)

    # anonymous definition for 'patternProperties' (TODO: nodename)
    class _PatternProperties(Visitor):
        _schema_type = 'unknown'
        _roles = ['field_of_something']
        _uid = '/examples/separated/definitions/Components.yaml#/definitions/Components/patternProperties'

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Components._PatternProperties', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_PatternProperties')
            if self.node is not None:
                self.node.attach(ctx, d, self)


    @reify
    def patternProperties(self):
        return runtime.resolve_visitor('patternProperties', cls=Components._PatternProperties, logger=logger)



class Toplevel(Visitor):
    _schema_type = 'object'
    _roles = ['has_extra_properties', 'has_properties', 'toplevel_properties']
    _uid = '/examples/separated/main.yaml#/'
    _properties = ['components', 'openapi']
    _extra_properties = ['additionalProperties', 'patternProperties']
    _links = ['components']

    @reify
    def _pattern_properties_regexes(self):
        return [
            (re.compile('^x-'), runtime.resolve_visitor('^x-', cls=Toplevel._PatternProperties_x, logger=logger)),
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
        if 'components' in d:
            ctx.run('components', self.components.visit, d['components'])

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

    @reify
    def components(self):
        return runtime.resolve_visitor('components', cls=Components, logger=logger)

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = 'any'
        _roles = ['field_of_something', 'toplevel_properties']
        _uid = '/examples/separated/main.yaml#/patternProperties/^x-'

        @reify
        def node(self):
            return runtime.resolve_node('.nodes.Toplevel._PatternProperties_x', here=__name__, logger=logger)

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", '_PatternProperties_x')
            if self.node is not None:
                self.node.attach(ctx, d, self)


    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor('patternProperties/^x-', cls=Toplevel._PatternProperties_x, logger=logger)



# fmt: off
_case = runtime.Case({'definitions': {'1': {'additionalProperties': False, 'patternProperties': {'^x-': {}}, 'properties': {'additionalProperties': {'default': True, 'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}, {'$ref': '#/definitions/2'}]}, 'allOf': {'items': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'type': 'array'}, 'anyOf': {'items': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'type': 'array'}, 'default': {}, 'deprecated': {'default': False, 'type': 'boolean'}, 'discriminator': {'$ref': 'Discriminator.yaml#/definitions/Discriminator'}, 'enum': {'items': {}, 'minItems': 1, 'type': 'array'}, 'example': {}, 'exclusiveMaximum': {'default': False, 'type': 'boolean'}, 'exclusiveMinimum': {'default': False, 'type': 'boolean'}, 'format': {'type': 'string'}, 'items': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'maxItems': {'minimum': 0, 'type': 'integer'}, 'maxLength': {'minimum': 0, 'type': 'integer'}, 'maxProperties': {'minimum': 0, 'type': 'integer'}, 'maximum': {'type': 'number'}, 'minItems': {'default': 0, 'minimum': 0, 'type': 'integer'}, 'minLength': {'default': 0, 'minimum': 0, 'type': 'integer'}, 'minProperties': {'default': 0, 'minimum': 0, 'type': 'integer'}, 'minimum': {'type': 'number'}, 'multipleOf': {'exclusiveMinimum': True, 'minimum': 0, 'type': 'number'}, 'not': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'nullable': {'default': False, 'type': 'boolean'}, 'oneOf': {'items': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'type': 'array'}, 'pattern': {'format': 'regex', 'type': 'string'}, 'properties': {'additionalProperties': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'type': 'object'}, 'readOnly': {'default': False, 'type': 'boolean'}, 'required': {'items': {'type': 'string'}, 'minItems': 1, 'type': 'array', 'uniqueItems': True}, 'title': {'type': 'string'}, 'type': {'enum': ['array', 'boolean', 'integer', 'number', 'object', 'string'], 'type': 'string'}, 'uniqueItems': {'default': False, 'type': 'boolean'}, 'writeOnly': {'default': False, 'type': 'boolean'}}, 'type': 'object'}, '2': {'type': 'boolean'}, '3': {'properties': {'$ref': {'format': 'uriref', 'type': 'string'}}, 'required': ['$ref'], 'type': 'object'}, '11': {'properties': {'mapping': {'additionalProperties': {'type': 'string'}, 'type': 'object'}, 'propertyName': {'type': 'string'}}, 'required': ['propertyName'], 'type': 'object'}, '20': {'type': 'boolean'}, '33': {'properties': {'$ref': {'format': 'uriref', 'type': 'string'}}, 'required': ['$ref'], 'type': 'object'}, '34': {'additionalProperties': False, 'patternProperties': {'^x-': {}}, 'properties': {'additionalProperties': {'default': True, 'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}, {'$ref': '#/definitions/2'}]}, 'allOf': {'items': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'type': 'array'}, 'anyOf': {'items': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'type': 'array'}, 'default': {}, 'deprecated': {'default': False, 'type': 'boolean'}, 'discriminator': {'$ref': '#/definitions/11'}, 'enum': {'items': {}, 'minItems': 1, 'type': 'array'}, 'example': {}, 'exclusiveMaximum': {'default': False, 'type': 'boolean'}, 'exclusiveMinimum': {'default': False, 'type': 'boolean'}, 'format': {'type': 'string'}, 'items': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'maxItems': {'minimum': 0, 'type': 'integer'}, 'maxLength': {'minimum': 0, 'type': 'integer'}, 'maxProperties': {'minimum': 0, 'type': 'integer'}, 'maximum': {'type': 'number'}, 'minItems': {'default': 0, 'minimum': 0, 'type': 'integer'}, 'minLength': {'default': 0, 'minimum': 0, 'type': 'integer'}, 'minProperties': {'default': 0, 'minimum': 0, 'type': 'integer'}, 'minimum': {'type': 'number'}, 'multipleOf': {'exclusiveMinimum': True, 'minimum': 0, 'type': 'number'}, 'not': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'nullable': {'default': False, 'type': 'boolean'}, 'oneOf': {'items': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'type': 'array'}, 'pattern': {'format': 'regex', 'type': 'string'}, 'properties': {'additionalProperties': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'type': 'object'}, 'readOnly': {'default': False, 'type': 'boolean'}, 'required': {'items': {'type': 'string'}, 'minItems': 1, 'type': 'array', 'uniqueItems': True}, 'title': {'type': 'string'}, 'type': {'enum': ['array', 'boolean', 'integer', 'number', 'object', 'string'], 'type': 'string'}, 'uniqueItems': {'default': False, 'type': 'boolean'}, 'writeOnly': {'default': False, 'type': 'boolean'}}, 'type': 'object'}, '35': {'type': 'boolean'}}})
# fmt: on
