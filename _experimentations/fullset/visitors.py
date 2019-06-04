# generated from data/openapi-3.0.json
from logging import getLogger
from openapi_stream.interfaces import Visitor
import re
from openapi_stream import runtime
from dictknife.langhelpers import reify
from openapi_stream.context import Context


logger = getLogger(__name__)  # noqa


class Contact(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/Contact"
    _properties = ["email", "name", "url"]
    _extra_properties = ["additionalProperties", "patternProperties"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=Contact._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Contact", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Contact")
        if self.node is not None:
            self.node.attach(ctx, d, self)

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/Contact/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Contact._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=Contact._PatternProperties_x, logger=logger
        )


class License(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/License"
    _properties = ["name", "url"]
    _extra_properties = ["additionalProperties", "patternProperties"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=License._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.License", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "License")
        if self.node is not None:
            self.node.attach(ctx, d, self)

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/License/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.License._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=License._PatternProperties_x, logger=logger
        )


class Info(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/Info"
    _properties = [
        "contact",
        "description",
        "license",
        "termsOfService",
        "title",
        "version",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["contact", "license"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=Info._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Info", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Info")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "contact" in d:
            ctx.run("contact", self.contact.visit, d["contact"])
        if "license" in d:
            ctx.run("license", self.license.visit, d["license"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    @reify
    def contact(self):
        return runtime.resolve_visitor("contact", cls=Contact, logger=logger)

    @reify
    def license(self):
        return runtime.resolve_visitor("license", cls=License, logger=logger)

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/Info/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Info._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=Info._PatternProperties_x, logger=logger
        )


class ExternalDocumentation(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/ExternalDocumentation"
    _properties = ["description", "url"]
    _extra_properties = ["additionalProperties", "patternProperties"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=ExternalDocumentation._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ExternalDocumentation", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ExternalDocumentation")
        if self.node is not None:
            self.node.attach(ctx, d, self)

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/ExternalDocumentation/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ExternalDocumentation._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=ExternalDocumentation._PatternProperties_x,
            logger=logger,
        )


class ServerVariable(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/ServerVariable"
    _properties = ["default", "description", "enum"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["enum"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=ServerVariable._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ServerVariable", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ServerVariable")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "enum" in d:
            ctx.run("enum", self.enum.visit, d["enum"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'enum' (TODO: nodename)
    class _Enum(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/ServerVariable/enum"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ServerVariable._Enum", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Enum")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def enum(self):
        return runtime.resolve_visitor("enum", cls=ServerVariable._Enum, logger=logger)

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = (
            "/data/openapi-3.0.json#/definitions/ServerVariable/patternProperties/^x-"
        )

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ServerVariable._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=ServerVariable._PatternProperties_x,
            logger=logger,
        )


class Server(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/Server"
    _properties = ["description", "url", "variables"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["variables"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=Server._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Server", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Server")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "variables" in d:
            ctx.run("variables", self.variables.visit, d["variables"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'variables' (TODO: nodename)
    class _Variables(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Server/variables"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Server._Variables", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Variables")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

    @reify
    def variables(self):
        return runtime.resolve_visitor(
            "variables", cls=Server._Variables, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/Server/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Server._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=Server._PatternProperties_x, logger=logger
        )


class SecurityRequirement(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name"]
    _uid = "/data/openapi-3.0.json#/definitions/SecurityRequirement"
    _extra_properties = ["additionalProperties"]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.SecurityRequirement", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "SecurityRequirement")
        if self.node is not None:
            self.node.attach(ctx, d, self)

        # additionalProperties
        for k, v in d.items():
            if k in self._properties:
                continue
            ctx.run(k, self.additional_properties.visit, v)

    # anonymous definition for 'additionalProperties' (TODO: nodename)
    class _AdditionalProperties(Visitor):
        _schema_type = "array"
        _roles = ["field_of_something", "has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/SecurityRequirement/additionalProperties"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.SecurityRequirement._AdditionalProperties",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_AdditionalProperties")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        # anonymous definition for 'items' (TODO: nodename)
        class _Items(Visitor):
            _schema_type = "string"
            _roles = ["field_of_something", "primitive_type"]
            _uid = "/data/openapi-3.0.json#/definitions/SecurityRequirement/additionalProperties/items"

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.SecurityRequirement._AdditionalProperties._Items",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: simplify

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_Items")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

        @reify
        def items(self):
            return runtime.resolve_visitor(
                "items",
                cls=SecurityRequirement._AdditionalProperties._Items,
                logger=logger,
            )

    @reify
    def additionalProperties(self):
        return runtime.resolve_visitor(
            "additionalProperties",
            cls=SecurityRequirement._AdditionalProperties,
            logger=logger,
        )


class Tag(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/Tag"
    _properties = ["description", "externalDocs", "name"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["externalDocs"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=Tag._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Tag", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Tag")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "externalDocs" in d:
            ctx.run("externalDocs", self.externalDocs.visit, d["externalDocs"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    @reify
    def externalDocs(self):
        return runtime.resolve_visitor(
            "externalDocs", cls=ExternalDocumentation, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/Tag/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Tag._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=Tag._PatternProperties_x, logger=logger
        )


class Reference(Visitor):
    _schema_type = "object"
    _roles = ["has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/Reference"
    _properties = ["$ref"]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Reference", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Reference")
        if self.node is not None:
            self.node.attach(ctx, d, self)


class Discriminator(Visitor):
    _schema_type = "object"
    _roles = ["has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/Discriminator"
    _properties = ["mapping", "propertyName"]
    _links = ["mapping"]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.Discriminator", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Discriminator")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "mapping" in d:
            ctx.run("mapping", self.mapping.visit, d["mapping"])

    # anonymous definition for 'mapping' (TODO: nodename)
    class _Mapping(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Discriminator/mapping"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Discriminator._Mapping", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Mapping")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "string"
            _roles = ["field_of_something", "primitive_type"]
            _uid = "/data/openapi-3.0.json#/definitions/Discriminator/mapping/additionalProperties"

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Discriminator._Mapping._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: simplify

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=Discriminator._Mapping._AdditionalProperties,
                logger=logger,
            )

    @reify
    def mapping(self):
        return runtime.resolve_visitor(
            "mapping", cls=Discriminator._Mapping, logger=logger
        )


class XML(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/XML"
    _properties = ["attribute", "name", "namespace", "prefix", "wrapped"]
    _extra_properties = ["additionalProperties", "patternProperties"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=XML._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.XML", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "XML")
        if self.node is not None:
            self.node.attach(ctx, d, self)

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/XML/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.XML._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=XML._PatternProperties_x, logger=logger
        )


class Schema(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/Schema"
    _properties = [
        "additionalProperties",
        "allOf",
        "anyOf",
        "default",
        "deprecated",
        "description",
        "discriminator",
        "enum",
        "example",
        "exclusiveMaximum",
        "exclusiveMinimum",
        "externalDocs",
        "format",
        "items",
        "maxItems",
        "maxLength",
        "maxProperties",
        "maximum",
        "minItems",
        "minLength",
        "minProperties",
        "minimum",
        "multipleOf",
        "not",
        "nullable",
        "oneOf",
        "pattern",
        "properties",
        "readOnly",
        "required",
        "title",
        "type",
        "uniqueItems",
        "writeOnly",
        "xml",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = [
        "required",
        "enum",
        "not",
        "allOf",
        "oneOf",
        "anyOf",
        "items",
        "properties",
        "additionalProperties",
        "default",
        "discriminator",
        "example",
        "externalDocs",
        "xml",
    ]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=Schema._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Schema", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Schema")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "required" in d:
            ctx.run("required", self.required.visit, d["required"])
        if "enum" in d:
            ctx.run("enum", self.enum.visit, d["enum"])
        if "not" in d:
            ctx.run("not", self.not_.visit, d["not"])
        if "allOf" in d:
            ctx.run("allOf", self.allOf.visit, d["allOf"])
        if "oneOf" in d:
            ctx.run("oneOf", self.oneOf.visit, d["oneOf"])
        if "anyOf" in d:
            ctx.run("anyOf", self.anyOf.visit, d["anyOf"])
        if "items" in d:
            ctx.run("items", self.items.visit, d["items"])
        if "properties" in d:
            ctx.run("properties", self.properties.visit, d["properties"])
        if "additionalProperties" in d:
            ctx.run(
                "additionalProperties",
                self.additionalProperties.visit,
                d["additionalProperties"],
            )
        if "default" in d:
            ctx.run("default", self.default.visit, d["default"])
        if "discriminator" in d:
            ctx.run("discriminator", self.discriminator.visit, d["discriminator"])
        if "example" in d:
            ctx.run("example", self.example.visit, d["example"])
        if "externalDocs" in d:
            ctx.run("externalDocs", self.externalDocs.visit, d["externalDocs"])
        if "xml" in d:
            ctx.run("xml", self.xml.visit, d["xml"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    @reify
    def discriminator(self):
        return runtime.resolve_visitor(
            "discriminator", cls=Discriminator, logger=logger
        )

    @reify
    def externalDocs(self):
        return runtime.resolve_visitor(
            "externalDocs", cls=ExternalDocumentation, logger=logger
        )

    @reify
    def xml(self):
        return runtime.resolve_visitor("xml", cls=XML, logger=logger)

    # anonymous definition for 'not' (TODO: nodename)
    class _Not(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/Schema/not"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Schema._Not", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Not")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def not_(self):
        return runtime.resolve_visitor("not", cls=Schema._Not, logger=logger)

    # anonymous definition for 'enum' (TODO: nodename)
    class _Enum(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Schema/enum"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Schema._Enum", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Enum")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def enum(self):
        return runtime.resolve_visitor("enum", cls=Schema._Enum, logger=logger)

    # anonymous definition for 'allOf' (TODO: nodename)
    class _AllOf(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Schema/allOf"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Schema._AllOf", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_AllOf")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        # anonymous definition for 'items' (TODO: nodename)
        class _Items(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Schema/allOf/items"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Schema._AllOf._Items", here=__name__, logger=logger
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_Items")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def items(self):
            return runtime.resolve_visitor(
                "items", cls=Schema._AllOf._Items, logger=logger
            )

    @reify
    def allOf(self):
        return runtime.resolve_visitor("allOf", cls=Schema._AllOf, logger=logger)

    # anonymous definition for 'oneOf' (TODO: nodename)
    class _OneOf(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Schema/oneOf"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Schema._OneOf", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_OneOf")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        # anonymous definition for 'items' (TODO: nodename)
        class _Items(Visitor):
            _schema_type = "oneOf"
            _roles = ["child_of_xxx_of", "combine_type", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Schema/oneOf/items"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Schema._OneOf._Items", here=__name__, logger=logger
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_Items")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def items(self):
            return runtime.resolve_visitor(
                "items", cls=Schema._OneOf._Items, logger=logger
            )

    @reify
    def oneOf(self):
        return runtime.resolve_visitor("oneOf", cls=Schema._OneOf, logger=logger)

    # anonymous definition for 'anyOf' (TODO: nodename)
    class _AnyOf(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Schema/anyOf"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Schema._AnyOf", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_AnyOf")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        # anonymous definition for 'items' (TODO: nodename)
        class _Items(Visitor):
            _schema_type = "oneOf"
            _roles = ["child_of_xxx_of", "combine_type", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Schema/anyOf/items"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Schema._AnyOf._Items", here=__name__, logger=logger
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_Items")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def items(self):
            return runtime.resolve_visitor(
                "items", cls=Schema._AnyOf._Items, logger=logger
            )

    @reify
    def anyOf(self):
        return runtime.resolve_visitor("anyOf", cls=Schema._AnyOf, logger=logger)

    # anonymous definition for 'items' (TODO: nodename)
    class _Items(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/Schema/items"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Schema._Items", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Items")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def items(self):
        return runtime.resolve_visitor("items", cls=Schema._Items, logger=logger)

    # anonymous definition for 'required' (TODO: nodename)
    class _Required(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Schema/required"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Schema._Required", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Required")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def required(self):
        return runtime.resolve_visitor("required", cls=Schema._Required, logger=logger)

    # anonymous definition for 'properties' (TODO: nodename)
    class _Properties(Visitor):
        _schema_type = "object"
        _roles = ["field_of_something", "has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Schema/properties"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Schema._Properties", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Properties")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Schema/properties/additionalProperties"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Schema._Properties._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=Schema._Properties._AdditionalProperties,
                logger=logger,
            )

    @reify
    def properties(self):
        return runtime.resolve_visitor(
            "properties", cls=Schema._Properties, logger=logger
        )

    # anonymous definition for 'additionalProperties' (TODO: nodename)
    class _AdditionalProperties(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "field_of_something", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/Schema/additionalProperties"
        _xxx_of_definitions = [
            {"$ref": "#/definitions/1"},
            {"$ref": "#/definitions/3"},
            {"$ref": "#/definitions/34"},
        ]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Schema._AdditionalProperties", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            if _case.when(d, "#/definitions/34"):
                return ctx.run(None, self.oneOf2.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_AdditionalProperties")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def oneOf2(self):
            return runtime.resolve_visitor(
                "oneOf2", cls=Schema._AdditionalProperties._OneOf_2, logger=logger
            )

        # anonymous definition for 'oneOf/2' (TODO: nodename)
        class _OneOf_2(Visitor):
            _schema_type = "boolean"
            _roles = ["child_of_xxx_of", "primitive_type"]
            _uid = "/data/openapi-3.0.json#/definitions/Schema/additionalProperties/oneOf/2"

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Schema._AdditionalProperties._OneOf_2",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: simplify

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_OneOf_2")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

        @reify
        def oneOf_2(self):
            return runtime.resolve_visitor(
                "oneOf/2", cls=Schema._AdditionalProperties._OneOf_2, logger=logger
            )

    @reify
    def additionalProperties(self):
        return runtime.resolve_visitor(
            "additionalProperties", cls=Schema._AdditionalProperties, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/Schema/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Schema._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=Schema._PatternProperties_x, logger=logger
        )


class ParameterWithSchemaWithExampleInPath(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExampleInPath"
    _properties = [
        "allowEmptyValue",
        "allowReserved",
        "deprecated",
        "description",
        "example",
        "explode",
        "in",
        "name",
        "required",
        "schema",
        "style",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["schema", "example"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=ParameterWithSchemaWithExampleInPath._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ParameterWithSchemaWithExampleInPath", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ParameterWithSchemaWithExampleInPath")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "schema" in d:
            ctx.run("schema", self.schema.visit, d["schema"])
        if "example" in d:
            ctx.run("example", self.example.visit, d["example"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'schema' (TODO: nodename)
    class _Schema(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExampleInPath/schema"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExampleInPath._Schema",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Schema")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def schema(self):
        return runtime.resolve_visitor(
            "schema", cls=ParameterWithSchemaWithExampleInPath._Schema, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExampleInPath/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExampleInPath._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=ParameterWithSchemaWithExampleInPath._PatternProperties_x,
            logger=logger,
        )


class ParameterWithSchemaWithExampleInQuery(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExampleInQuery"
    _properties = [
        "allowEmptyValue",
        "allowReserved",
        "deprecated",
        "description",
        "example",
        "explode",
        "in",
        "name",
        "required",
        "schema",
        "style",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["schema", "example"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=ParameterWithSchemaWithExampleInQuery._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ParameterWithSchemaWithExampleInQuery", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ParameterWithSchemaWithExampleInQuery")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "schema" in d:
            ctx.run("schema", self.schema.visit, d["schema"])
        if "example" in d:
            ctx.run("example", self.example.visit, d["example"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'schema' (TODO: nodename)
    class _Schema(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExampleInQuery/schema"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExampleInQuery._Schema",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Schema")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def schema(self):
        return runtime.resolve_visitor(
            "schema", cls=ParameterWithSchemaWithExampleInQuery._Schema, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExampleInQuery/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExampleInQuery._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=ParameterWithSchemaWithExampleInQuery._PatternProperties_x,
            logger=logger,
        )


class ParameterWithSchemaWithExampleInHeader(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExampleInHeader"
    _properties = [
        "allowEmptyValue",
        "allowReserved",
        "deprecated",
        "description",
        "example",
        "explode",
        "in",
        "name",
        "required",
        "schema",
        "style",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["schema", "example"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=ParameterWithSchemaWithExampleInHeader._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ParameterWithSchemaWithExampleInHeader",
            here=__name__,
            logger=logger,
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ParameterWithSchemaWithExampleInHeader")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "schema" in d:
            ctx.run("schema", self.schema.visit, d["schema"])
        if "example" in d:
            ctx.run("example", self.example.visit, d["example"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'schema' (TODO: nodename)
    class _Schema(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExampleInHeader/schema"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExampleInHeader._Schema",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Schema")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def schema(self):
        return runtime.resolve_visitor(
            "schema", cls=ParameterWithSchemaWithExampleInHeader._Schema, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExampleInHeader/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExampleInHeader._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=ParameterWithSchemaWithExampleInHeader._PatternProperties_x,
            logger=logger,
        )


class ParameterWithSchemaWithExampleInCookie(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExampleInCookie"
    _properties = [
        "allowEmptyValue",
        "allowReserved",
        "deprecated",
        "description",
        "example",
        "explode",
        "in",
        "name",
        "required",
        "schema",
        "style",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["schema", "example"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=ParameterWithSchemaWithExampleInCookie._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ParameterWithSchemaWithExampleInCookie",
            here=__name__,
            logger=logger,
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ParameterWithSchemaWithExampleInCookie")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "schema" in d:
            ctx.run("schema", self.schema.visit, d["schema"])
        if "example" in d:
            ctx.run("example", self.example.visit, d["example"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'schema' (TODO: nodename)
    class _Schema(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExampleInCookie/schema"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExampleInCookie._Schema",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Schema")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def schema(self):
        return runtime.resolve_visitor(
            "schema", cls=ParameterWithSchemaWithExampleInCookie._Schema, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExampleInCookie/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExampleInCookie._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=ParameterWithSchemaWithExampleInCookie._PatternProperties_x,
            logger=logger,
        )


class ParameterWithSchemaWithExample(Visitor):
    _schema_type = "oneOf"
    _roles = ["combine_type", "has_expanded", "has_name"]
    _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExample"
    _xxx_of_definitions = [
        {"$ref": "#/definitions/1"},
        {"$ref": "#/definitions/3"},
        {"$ref": "#/definitions/45"},
        {"$ref": "#/definitions/46"},
    ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ParameterWithSchemaWithExample", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        # for oneOf (xxx: _case is module global)
        if _case.when(d, "#/definitions/1"):
            return ctx.run(None, self.oneOf0.visit, d)
        if _case.when(d, "#/definitions/3"):
            return ctx.run(None, self.oneOf1.visit, d)
        if _case.when(d, "#/definitions/45"):
            return ctx.run(None, self.oneOf2.visit, d)
        if _case.when(d, "#/definitions/46"):
            return ctx.run(None, self.oneOf3.visit, d)
        raise ValueError("unexpected value")  # todo gentle message

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ParameterWithSchemaWithExample")
        if self.node is not None:
            self.node.attach(ctx, d, self)

    @reify
    def oneOf0(self):
        return runtime.resolve_visitor(
            "oneOf0", cls=ParameterWithSchemaWithExampleInPath, logger=logger
        )

    @reify
    def oneOf1(self):
        return runtime.resolve_visitor(
            "oneOf1", cls=ParameterWithSchemaWithExampleInQuery, logger=logger
        )

    @reify
    def oneOf2(self):
        return runtime.resolve_visitor(
            "oneOf2", cls=ParameterWithSchemaWithExampleInHeader, logger=logger
        )

    @reify
    def oneOf3(self):
        return runtime.resolve_visitor(
            "oneOf3", cls=ParameterWithSchemaWithExampleInCookie, logger=logger
        )


class Example(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/Example"
    _properties = ["description", "externalValue", "summary", "value"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["value"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=Example._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Example", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Example")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "value" in d:
            ctx.run("value", self.value.visit, d["value"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/Example/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Example._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=Example._PatternProperties_x, logger=logger
        )


class ParameterWithSchemaWithExamplesInPath(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInPath"
    _properties = [
        "allowEmptyValue",
        "allowReserved",
        "deprecated",
        "description",
        "examples",
        "explode",
        "in",
        "name",
        "required",
        "schema",
        "style",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["schema", "examples"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=ParameterWithSchemaWithExamplesInPath._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ParameterWithSchemaWithExamplesInPath", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ParameterWithSchemaWithExamplesInPath")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "schema" in d:
            ctx.run("schema", self.schema.visit, d["schema"])
        if "examples" in d:
            ctx.run("examples", self.examples.visit, d["examples"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'schema' (TODO: nodename)
    class _Schema(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInPath/schema"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExamplesInPath._Schema",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Schema")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def schema(self):
        return runtime.resolve_visitor(
            "schema", cls=ParameterWithSchemaWithExamplesInPath._Schema, logger=logger
        )

    # anonymous definition for 'examples' (TODO: nodename)
    class _Examples(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInPath/examples"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExamplesInPath._Examples",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Examples")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInPath/examples/additionalProperties"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.ParameterWithSchemaWithExamplesInPath._Examples._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Example, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=ParameterWithSchemaWithExamplesInPath._Examples._AdditionalProperties,
                logger=logger,
            )

    @reify
    def examples(self):
        return runtime.resolve_visitor(
            "examples",
            cls=ParameterWithSchemaWithExamplesInPath._Examples,
            logger=logger,
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInPath/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExamplesInPath._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=ParameterWithSchemaWithExamplesInPath._PatternProperties_x,
            logger=logger,
        )


class ParameterWithSchemaWithExamplesInQuery(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInQuery"
    _properties = [
        "allowEmptyValue",
        "allowReserved",
        "deprecated",
        "description",
        "examples",
        "explode",
        "in",
        "name",
        "required",
        "schema",
        "style",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["schema", "examples"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=ParameterWithSchemaWithExamplesInQuery._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ParameterWithSchemaWithExamplesInQuery",
            here=__name__,
            logger=logger,
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ParameterWithSchemaWithExamplesInQuery")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "schema" in d:
            ctx.run("schema", self.schema.visit, d["schema"])
        if "examples" in d:
            ctx.run("examples", self.examples.visit, d["examples"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'schema' (TODO: nodename)
    class _Schema(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInQuery/schema"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExamplesInQuery._Schema",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Schema")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def schema(self):
        return runtime.resolve_visitor(
            "schema", cls=ParameterWithSchemaWithExamplesInQuery._Schema, logger=logger
        )

    # anonymous definition for 'examples' (TODO: nodename)
    class _Examples(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInQuery/examples"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExamplesInQuery._Examples",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Examples")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInQuery/examples/additionalProperties"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.ParameterWithSchemaWithExamplesInQuery._Examples._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Example, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=ParameterWithSchemaWithExamplesInQuery._Examples._AdditionalProperties,
                logger=logger,
            )

    @reify
    def examples(self):
        return runtime.resolve_visitor(
            "examples",
            cls=ParameterWithSchemaWithExamplesInQuery._Examples,
            logger=logger,
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInQuery/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExamplesInQuery._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=ParameterWithSchemaWithExamplesInQuery._PatternProperties_x,
            logger=logger,
        )


class ParameterWithSchemaWithExamplesInHeader(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInHeader"
    _properties = [
        "allowEmptyValue",
        "allowReserved",
        "deprecated",
        "description",
        "examples",
        "explode",
        "in",
        "name",
        "required",
        "schema",
        "style",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["schema", "examples"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=ParameterWithSchemaWithExamplesInHeader._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ParameterWithSchemaWithExamplesInHeader",
            here=__name__,
            logger=logger,
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ParameterWithSchemaWithExamplesInHeader")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "schema" in d:
            ctx.run("schema", self.schema.visit, d["schema"])
        if "examples" in d:
            ctx.run("examples", self.examples.visit, d["examples"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'schema' (TODO: nodename)
    class _Schema(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInHeader/schema"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExamplesInHeader._Schema",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Schema")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def schema(self):
        return runtime.resolve_visitor(
            "schema", cls=ParameterWithSchemaWithExamplesInHeader._Schema, logger=logger
        )

    # anonymous definition for 'examples' (TODO: nodename)
    class _Examples(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInHeader/examples"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExamplesInHeader._Examples",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Examples")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInHeader/examples/additionalProperties"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.ParameterWithSchemaWithExamplesInHeader._Examples._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Example, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=ParameterWithSchemaWithExamplesInHeader._Examples._AdditionalProperties,
                logger=logger,
            )

    @reify
    def examples(self):
        return runtime.resolve_visitor(
            "examples",
            cls=ParameterWithSchemaWithExamplesInHeader._Examples,
            logger=logger,
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInHeader/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExamplesInHeader._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=ParameterWithSchemaWithExamplesInHeader._PatternProperties_x,
            logger=logger,
        )


class ParameterWithSchemaWithExamplesInCookie(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInCookie"
    _properties = [
        "allowEmptyValue",
        "allowReserved",
        "deprecated",
        "description",
        "examples",
        "explode",
        "in",
        "name",
        "required",
        "schema",
        "style",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["schema", "examples"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=ParameterWithSchemaWithExamplesInCookie._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ParameterWithSchemaWithExamplesInCookie",
            here=__name__,
            logger=logger,
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ParameterWithSchemaWithExamplesInCookie")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "schema" in d:
            ctx.run("schema", self.schema.visit, d["schema"])
        if "examples" in d:
            ctx.run("examples", self.examples.visit, d["examples"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'schema' (TODO: nodename)
    class _Schema(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInCookie/schema"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExamplesInCookie._Schema",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Schema")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def schema(self):
        return runtime.resolve_visitor(
            "schema", cls=ParameterWithSchemaWithExamplesInCookie._Schema, logger=logger
        )

    # anonymous definition for 'examples' (TODO: nodename)
    class _Examples(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInCookie/examples"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExamplesInCookie._Examples",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Examples")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInCookie/examples/additionalProperties"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.ParameterWithSchemaWithExamplesInCookie._Examples._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Example, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=ParameterWithSchemaWithExamplesInCookie._Examples._AdditionalProperties,
                logger=logger,
            )

    @reify
    def examples(self):
        return runtime.resolve_visitor(
            "examples",
            cls=ParameterWithSchemaWithExamplesInCookie._Examples,
            logger=logger,
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamplesInCookie/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithSchemaWithExamplesInCookie._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=ParameterWithSchemaWithExamplesInCookie._PatternProperties_x,
            logger=logger,
        )


class ParameterWithSchemaWithExamples(Visitor):
    _schema_type = "oneOf"
    _roles = ["combine_type", "has_expanded", "has_name"]
    _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchemaWithExamples"
    _xxx_of_definitions = [
        {"$ref": "#/definitions/1"},
        {"$ref": "#/definitions/3"},
        {"$ref": "#/definitions/45"},
        {"$ref": "#/definitions/46"},
    ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ParameterWithSchemaWithExamples", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        # for oneOf (xxx: _case is module global)
        if _case.when(d, "#/definitions/1"):
            return ctx.run(None, self.oneOf0.visit, d)
        if _case.when(d, "#/definitions/3"):
            return ctx.run(None, self.oneOf1.visit, d)
        if _case.when(d, "#/definitions/45"):
            return ctx.run(None, self.oneOf2.visit, d)
        if _case.when(d, "#/definitions/46"):
            return ctx.run(None, self.oneOf3.visit, d)
        raise ValueError("unexpected value")  # todo gentle message

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ParameterWithSchemaWithExamples")
        if self.node is not None:
            self.node.attach(ctx, d, self)

    @reify
    def oneOf0(self):
        return runtime.resolve_visitor(
            "oneOf0", cls=ParameterWithSchemaWithExamplesInPath, logger=logger
        )

    @reify
    def oneOf1(self):
        return runtime.resolve_visitor(
            "oneOf1", cls=ParameterWithSchemaWithExamplesInQuery, logger=logger
        )

    @reify
    def oneOf2(self):
        return runtime.resolve_visitor(
            "oneOf2", cls=ParameterWithSchemaWithExamplesInHeader, logger=logger
        )

    @reify
    def oneOf3(self):
        return runtime.resolve_visitor(
            "oneOf3", cls=ParameterWithSchemaWithExamplesInCookie, logger=logger
        )


class ParameterWithSchema(Visitor):
    _schema_type = "oneOf"
    _roles = ["combine_type", "has_expanded", "has_name"]
    _uid = "/data/openapi-3.0.json#/definitions/ParameterWithSchema"
    _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ParameterWithSchema", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        # for oneOf (xxx: _case is module global)
        if _case.when(d, "#/definitions/1"):
            return ctx.run(None, self.oneOf0.visit, d)
        if _case.when(d, "#/definitions/3"):
            return ctx.run(None, self.oneOf1.visit, d)
        raise ValueError("unexpected value")  # todo gentle message

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ParameterWithSchema")
        if self.node is not None:
            self.node.attach(ctx, d, self)

    @reify
    def oneOf0(self):
        return runtime.resolve_visitor(
            "oneOf0", cls=ParameterWithSchemaWithExample, logger=logger
        )

    @reify
    def oneOf1(self):
        return runtime.resolve_visitor(
            "oneOf1", cls=ParameterWithSchemaWithExamples, logger=logger
        )


class HeaderWithSchemaWithExample(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/HeaderWithSchemaWithExample"
    _properties = [
        "allowEmptyValue",
        "allowReserved",
        "deprecated",
        "description",
        "example",
        "explode",
        "required",
        "schema",
        "style",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["schema", "example"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=HeaderWithSchemaWithExample._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.HeaderWithSchemaWithExample", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "HeaderWithSchemaWithExample")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "schema" in d:
            ctx.run("schema", self.schema.visit, d["schema"])
        if "example" in d:
            ctx.run("example", self.example.visit, d["example"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'schema' (TODO: nodename)
    class _Schema(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/HeaderWithSchemaWithExample/schema"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.HeaderWithSchemaWithExample._Schema",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Schema")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def schema(self):
        return runtime.resolve_visitor(
            "schema", cls=HeaderWithSchemaWithExample._Schema, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/HeaderWithSchemaWithExample/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.HeaderWithSchemaWithExample._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=HeaderWithSchemaWithExample._PatternProperties_x,
            logger=logger,
        )


class HeaderWithSchemaWithExamples(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/HeaderWithSchemaWithExamples"
    _properties = [
        "allowEmptyValue",
        "allowReserved",
        "deprecated",
        "description",
        "examples",
        "explode",
        "required",
        "schema",
        "style",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["schema", "examples"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=HeaderWithSchemaWithExamples._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.HeaderWithSchemaWithExamples", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "HeaderWithSchemaWithExamples")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "schema" in d:
            ctx.run("schema", self.schema.visit, d["schema"])
        if "examples" in d:
            ctx.run("examples", self.examples.visit, d["examples"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'schema' (TODO: nodename)
    class _Schema(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/HeaderWithSchemaWithExamples/schema"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.HeaderWithSchemaWithExamples._Schema",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Schema")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def schema(self):
        return runtime.resolve_visitor(
            "schema", cls=HeaderWithSchemaWithExamples._Schema, logger=logger
        )

    # anonymous definition for 'examples' (TODO: nodename)
    class _Examples(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = (
            "/data/openapi-3.0.json#/definitions/HeaderWithSchemaWithExamples/examples"
        )
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.HeaderWithSchemaWithExamples._Examples",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Examples")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/HeaderWithSchemaWithExamples/examples/additionalProperties"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.HeaderWithSchemaWithExamples._Examples._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Example, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=HeaderWithSchemaWithExamples._Examples._AdditionalProperties,
                logger=logger,
            )

    @reify
    def examples(self):
        return runtime.resolve_visitor(
            "examples", cls=HeaderWithSchemaWithExamples._Examples, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/HeaderWithSchemaWithExamples/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.HeaderWithSchemaWithExamples._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=HeaderWithSchemaWithExamples._PatternProperties_x,
            logger=logger,
        )


class HeaderWithSchema(Visitor):
    _schema_type = "oneOf"
    _roles = ["combine_type", "has_expanded", "has_name"]
    _uid = "/data/openapi-3.0.json#/definitions/HeaderWithSchema"
    _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.HeaderWithSchema", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        # for oneOf (xxx: _case is module global)
        if _case.when(d, "#/definitions/1"):
            return ctx.run(None, self.oneOf0.visit, d)
        if _case.when(d, "#/definitions/3"):
            return ctx.run(None, self.oneOf1.visit, d)
        raise ValueError("unexpected value")  # todo gentle message

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "HeaderWithSchema")
        if self.node is not None:
            self.node.attach(ctx, d, self)

    @reify
    def oneOf0(self):
        return runtime.resolve_visitor(
            "oneOf0", cls=HeaderWithSchemaWithExample, logger=logger
        )

    @reify
    def oneOf1(self):
        return runtime.resolve_visitor(
            "oneOf1", cls=HeaderWithSchemaWithExamples, logger=logger
        )


class HeaderWithContent(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/HeaderWithContent"
    _properties = [
        "allowEmptyValue",
        "content",
        "deprecated",
        "description",
        "required",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["content"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=HeaderWithContent._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.HeaderWithContent", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "HeaderWithContent")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "content" in d:
            ctx.run("content", self.content.visit, d["content"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'content' (TODO: nodename)
    class _Content(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/HeaderWithContent/content"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.HeaderWithContent._Content", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Content")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

    @reify
    def content(self):
        return runtime.resolve_visitor(
            "content", cls=HeaderWithContent._Content, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/HeaderWithContent/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.HeaderWithContent._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=HeaderWithContent._PatternProperties_x,
            logger=logger,
        )


class Header(Visitor):
    _schema_type = "oneOf"
    _roles = ["combine_type", "has_expanded", "has_name"]
    _uid = "/data/openapi-3.0.json#/definitions/Header"
    _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Header", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        # for oneOf (xxx: _case is module global)
        if _case.when(d, "#/definitions/1"):
            return ctx.run(None, self.oneOf0.visit, d)
        if _case.when(d, "#/definitions/3"):
            return ctx.run(None, self.oneOf1.visit, d)
        raise ValueError("unexpected value")  # todo gentle message

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Header")
        if self.node is not None:
            self.node.attach(ctx, d, self)

    @reify
    def oneOf0(self):
        return runtime.resolve_visitor("oneOf0", cls=HeaderWithSchema, logger=logger)

    @reify
    def oneOf1(self):
        return runtime.resolve_visitor("oneOf1", cls=HeaderWithContent, logger=logger)


class Encoding(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/Encoding"
    _properties = ["allowReserved", "contentType", "explode", "headers", "style"]
    _extra_properties = ["additionalProperties"]
    _links = ["headers"]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Encoding", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Encoding")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "headers" in d:
            ctx.run("headers", self.headers.visit, d["headers"])

        # additionalProperties
        for k, v in d.items():
            if k in self._properties:
                continue
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'headers' (TODO: nodename)
    class _Headers(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Encoding/headers"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Encoding._Headers", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Headers")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

    @reify
    def headers(self):
        return runtime.resolve_visitor("headers", cls=Encoding._Headers, logger=logger)


class MediaTypeWithExample(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/MediaTypeWithExample"
    _properties = ["encoding", "example", "schema"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["schema", "example", "encoding"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=MediaTypeWithExample._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.MediaTypeWithExample", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "MediaTypeWithExample")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "schema" in d:
            ctx.run("schema", self.schema.visit, d["schema"])
        if "example" in d:
            ctx.run("example", self.example.visit, d["example"])
        if "encoding" in d:
            ctx.run("encoding", self.encoding.visit, d["encoding"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'schema' (TODO: nodename)
    class _Schema(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/MediaTypeWithExample/schema"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.MediaTypeWithExample._Schema", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Schema")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def schema(self):
        return runtime.resolve_visitor(
            "schema", cls=MediaTypeWithExample._Schema, logger=logger
        )

    # anonymous definition for 'encoding' (TODO: nodename)
    class _Encoding(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/MediaTypeWithExample/encoding"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.MediaTypeWithExample._Encoding", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Encoding")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

    @reify
    def encoding(self):
        return runtime.resolve_visitor(
            "encoding", cls=MediaTypeWithExample._Encoding, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/MediaTypeWithExample/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.MediaTypeWithExample._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=MediaTypeWithExample._PatternProperties_x,
            logger=logger,
        )


class MediaTypeWithExamples(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/MediaTypeWithExamples"
    _properties = ["encoding", "examples", "schema"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["schema", "examples", "encoding"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=MediaTypeWithExamples._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.MediaTypeWithExamples", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "MediaTypeWithExamples")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "schema" in d:
            ctx.run("schema", self.schema.visit, d["schema"])
        if "examples" in d:
            ctx.run("examples", self.examples.visit, d["examples"])
        if "encoding" in d:
            ctx.run("encoding", self.encoding.visit, d["encoding"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'schema' (TODO: nodename)
    class _Schema(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/MediaTypeWithExamples/schema"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.MediaTypeWithExamples._Schema", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Schema")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Schema, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def schema(self):
        return runtime.resolve_visitor(
            "schema", cls=MediaTypeWithExamples._Schema, logger=logger
        )

    # anonymous definition for 'examples' (TODO: nodename)
    class _Examples(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/MediaTypeWithExamples/examples"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.MediaTypeWithExamples._Examples", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Examples")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/MediaTypeWithExamples/examples/additionalProperties"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.MediaTypeWithExamples._Examples._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Example, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=MediaTypeWithExamples._Examples._AdditionalProperties,
                logger=logger,
            )

    @reify
    def examples(self):
        return runtime.resolve_visitor(
            "examples", cls=MediaTypeWithExamples._Examples, logger=logger
        )

    # anonymous definition for 'encoding' (TODO: nodename)
    class _Encoding(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/MediaTypeWithExamples/encoding"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.MediaTypeWithExamples._Encoding", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Encoding")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

    @reify
    def encoding(self):
        return runtime.resolve_visitor(
            "encoding", cls=MediaTypeWithExamples._Encoding, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/MediaTypeWithExamples/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.MediaTypeWithExamples._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=MediaTypeWithExamples._PatternProperties_x,
            logger=logger,
        )


class MediaType(Visitor):
    _schema_type = "oneOf"
    _roles = ["combine_type", "has_expanded", "has_name"]
    _uid = "/data/openapi-3.0.json#/definitions/MediaType"
    _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.MediaType", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        # for oneOf (xxx: _case is module global)
        if _case.when(d, "#/definitions/1"):
            return ctx.run(None, self.oneOf0.visit, d)
        if _case.when(d, "#/definitions/3"):
            return ctx.run(None, self.oneOf1.visit, d)
        raise ValueError("unexpected value")  # todo gentle message

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "MediaType")
        if self.node is not None:
            self.node.attach(ctx, d, self)

    @reify
    def oneOf0(self):
        return runtime.resolve_visitor(
            "oneOf0", cls=MediaTypeWithExample, logger=logger
        )

    @reify
    def oneOf1(self):
        return runtime.resolve_visitor(
            "oneOf1", cls=MediaTypeWithExamples, logger=logger
        )


class ParameterWithContentInPath(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/ParameterWithContentInPath"
    _properties = [
        "allowEmptyValue",
        "content",
        "deprecated",
        "description",
        "in",
        "name",
        "required",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["content"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=ParameterWithContentInPath._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ParameterWithContentInPath", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ParameterWithContentInPath")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "content" in d:
            ctx.run("content", self.content.visit, d["content"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'content' (TODO: nodename)
    class _Content(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithContentInPath/content"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithContentInPath._Content",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Content")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

    @reify
    def content(self):
        return runtime.resolve_visitor(
            "content", cls=ParameterWithContentInPath._Content, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithContentInPath/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithContentInPath._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=ParameterWithContentInPath._PatternProperties_x,
            logger=logger,
        )


class ParameterWithContentNotInPath(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/ParameterWithContentNotInPath"
    _properties = [
        "allowEmptyValue",
        "content",
        "deprecated",
        "description",
        "in",
        "name",
        "required",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["content"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=ParameterWithContentNotInPath._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ParameterWithContentNotInPath", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ParameterWithContentNotInPath")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "content" in d:
            ctx.run("content", self.content.visit, d["content"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'content' (TODO: nodename)
    class _Content(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = (
            "/data/openapi-3.0.json#/definitions/ParameterWithContentNotInPath/content"
        )
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithContentNotInPath._Content",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Content")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

    @reify
    def content(self):
        return runtime.resolve_visitor(
            "content", cls=ParameterWithContentNotInPath._Content, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/ParameterWithContentNotInPath/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ParameterWithContentNotInPath._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=ParameterWithContentNotInPath._PatternProperties_x,
            logger=logger,
        )


class ParameterWithContent(Visitor):
    _schema_type = "oneOf"
    _roles = ["combine_type", "has_expanded", "has_name"]
    _uid = "/data/openapi-3.0.json#/definitions/ParameterWithContent"
    _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ParameterWithContent", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        # for oneOf (xxx: _case is module global)
        if _case.when(d, "#/definitions/1"):
            return ctx.run(None, self.oneOf0.visit, d)
        if _case.when(d, "#/definitions/3"):
            return ctx.run(None, self.oneOf1.visit, d)
        raise ValueError("unexpected value")  # todo gentle message

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ParameterWithContent")
        if self.node is not None:
            self.node.attach(ctx, d, self)

    @reify
    def oneOf0(self):
        return runtime.resolve_visitor(
            "oneOf0", cls=ParameterWithContentInPath, logger=logger
        )

    @reify
    def oneOf1(self):
        return runtime.resolve_visitor(
            "oneOf1", cls=ParameterWithContentNotInPath, logger=logger
        )


class Parameter(Visitor):
    _schema_type = "oneOf"
    _roles = ["combine_type", "has_expanded", "has_name"]
    _uid = "/data/openapi-3.0.json#/definitions/Parameter"
    _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Parameter", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        # for oneOf (xxx: _case is module global)
        if _case.when(d, "#/definitions/1"):
            return ctx.run(None, self.oneOf0.visit, d)
        if _case.when(d, "#/definitions/3"):
            return ctx.run(None, self.oneOf1.visit, d)
        raise ValueError("unexpected value")  # todo gentle message

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Parameter")
        if self.node is not None:
            self.node.attach(ctx, d, self)

    @reify
    def oneOf0(self):
        return runtime.resolve_visitor("oneOf0", cls=ParameterWithSchema, logger=logger)

    @reify
    def oneOf1(self):
        return runtime.resolve_visitor(
            "oneOf1", cls=ParameterWithContent, logger=logger
        )


class RequestBody(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/RequestBody"
    _properties = ["content", "description", "required"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["content"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=RequestBody._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.RequestBody", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "RequestBody")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "content" in d:
            ctx.run("content", self.content.visit, d["content"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'content' (TODO: nodename)
    class _Content(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/RequestBody/content"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.RequestBody._Content", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Content")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

    @reify
    def content(self):
        return runtime.resolve_visitor(
            "content", cls=RequestBody._Content, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/RequestBody/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.RequestBody._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=RequestBody._PatternProperties_x, logger=logger
        )


class LinkWithOperationRef(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/LinkWithOperationRef"
    _properties = ["description", "operationRef", "parameters", "requestBody", "server"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["parameters", "requestBody", "server"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=LinkWithOperationRef._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.LinkWithOperationRef", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "LinkWithOperationRef")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "parameters" in d:
            ctx.run("parameters", self.parameters.visit, d["parameters"])
        if "requestBody" in d:
            ctx.run("requestBody", self.requestBody.visit, d["requestBody"])
        if "server" in d:
            ctx.run("server", self.server.visit, d["server"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    @reify
    def server(self):
        return runtime.resolve_visitor("server", cls=Server, logger=logger)

    # anonymous definition for 'parameters' (TODO: nodename)
    class _Parameters(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/LinkWithOperationRef/parameters"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.LinkWithOperationRef._Parameters", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Parameters")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "any"
            _roles = ["field_of_something"]
            _uid = "/data/openapi-3.0.json#/definitions/LinkWithOperationRef/parameters/additionalProperties"

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.LinkWithOperationRef._Parameters._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: remove this code

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=LinkWithOperationRef._Parameters._AdditionalProperties,
                logger=logger,
            )

    @reify
    def parameters(self):
        return runtime.resolve_visitor(
            "parameters", cls=LinkWithOperationRef._Parameters, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/LinkWithOperationRef/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.LinkWithOperationRef._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=LinkWithOperationRef._PatternProperties_x,
            logger=logger,
        )


class LinkWithOperationId(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/LinkWithOperationId"
    _properties = ["description", "operationId", "parameters", "requestBody", "server"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["parameters", "requestBody", "server"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=LinkWithOperationId._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.LinkWithOperationId", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "LinkWithOperationId")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "parameters" in d:
            ctx.run("parameters", self.parameters.visit, d["parameters"])
        if "requestBody" in d:
            ctx.run("requestBody", self.requestBody.visit, d["requestBody"])
        if "server" in d:
            ctx.run("server", self.server.visit, d["server"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    @reify
    def server(self):
        return runtime.resolve_visitor("server", cls=Server, logger=logger)

    # anonymous definition for 'parameters' (TODO: nodename)
    class _Parameters(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/LinkWithOperationId/parameters"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.LinkWithOperationId._Parameters", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Parameters")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "any"
            _roles = ["field_of_something"]
            _uid = "/data/openapi-3.0.json#/definitions/LinkWithOperationId/parameters/additionalProperties"

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.LinkWithOperationId._Parameters._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: remove this code

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=LinkWithOperationId._Parameters._AdditionalProperties,
                logger=logger,
            )

    @reify
    def parameters(self):
        return runtime.resolve_visitor(
            "parameters", cls=LinkWithOperationId._Parameters, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/LinkWithOperationId/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.LinkWithOperationId._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=LinkWithOperationId._PatternProperties_x,
            logger=logger,
        )


class Link(Visitor):
    _schema_type = "oneOf"
    _roles = ["combine_type", "has_expanded", "has_name"]
    _uid = "/data/openapi-3.0.json#/definitions/Link"
    _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Link", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        # for oneOf (xxx: _case is module global)
        if _case.when(d, "#/definitions/1"):
            return ctx.run(None, self.oneOf0.visit, d)
        if _case.when(d, "#/definitions/3"):
            return ctx.run(None, self.oneOf1.visit, d)
        raise ValueError("unexpected value")  # todo gentle message

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Link")
        if self.node is not None:
            self.node.attach(ctx, d, self)

    @reify
    def oneOf0(self):
        return runtime.resolve_visitor(
            "oneOf0", cls=LinkWithOperationRef, logger=logger
        )

    @reify
    def oneOf1(self):
        return runtime.resolve_visitor("oneOf1", cls=LinkWithOperationId, logger=logger)


class Response(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/Response"
    _properties = ["content", "description", "headers", "links"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["headers", "content", "links"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=Response._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Response", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Response")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "headers" in d:
            ctx.run("headers", self.headers.visit, d["headers"])
        if "content" in d:
            ctx.run("content", self.content.visit, d["content"])
        if "links" in d:
            ctx.run("links", self.links.visit, d["links"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'links' (TODO: nodename)
    class _Links(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Response/links"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Response._Links", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Links")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Response/links/additionalProperties"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Response._Links._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Link, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=Response._Links._AdditionalProperties,
                logger=logger,
            )

    @reify
    def links(self):
        return runtime.resolve_visitor("links", cls=Response._Links, logger=logger)

    # anonymous definition for 'headers' (TODO: nodename)
    class _Headers(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Response/headers"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Response._Headers", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Headers")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Response/headers/additionalProperties"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Response._Headers._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Header, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=Response._Headers._AdditionalProperties,
                logger=logger,
            )

    @reify
    def headers(self):
        return runtime.resolve_visitor("headers", cls=Response._Headers, logger=logger)

    # anonymous definition for 'content' (TODO: nodename)
    class _Content(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Response/content"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Response._Content", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Content")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

    @reify
    def content(self):
        return runtime.resolve_visitor("content", cls=Response._Content, logger=logger)

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/Response/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Response._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=Response._PatternProperties_x, logger=logger
        )


class Responses(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/Responses"
    _properties = ["default"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["default"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("[1-5](?:\\d{2}|XX)"),
                runtime.resolve_visitor(
                    "[1-5](?:\\d{2}|XX)",
                    cls=Responses._PatternProperties_15_d_2_XX,
                    logger=logger,
                ),
            ),
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=Responses._PatternProperties_x, logger=logger
                ),
            ),
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Responses", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Responses")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "default" in d:
            ctx.run("default", self.default.visit, d["default"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'default' (TODO: nodename)
    class _Default(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/Responses/default"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Responses._Default", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Default")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Response, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def default(self):
        return runtime.resolve_visitor("default", cls=Responses._Default, logger=logger)

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/Responses/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Responses._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=Responses._PatternProperties_x, logger=logger
        )

    # anonymous definition for 'patternProperties/[1-5](?:\\d{2}|XX)' (TODO: nodename)
    class _PatternProperties_15_d_2_XX(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "field_of_something", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/Responses/patternProperties/[1-5](?:\\d{2}|XX)"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Responses._PatternProperties_15_d_2_XX",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_15_d_2_XX")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=Response, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def patternProperties_1_5_d_2_XX(self):
        return runtime.resolve_visitor(
            "patternProperties/[1-5](?:\\d{2}|XX)",
            cls=Responses._PatternProperties_15_d_2_XX,
            logger=logger,
        )


class Callback(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name"]
    _uid = "/data/openapi-3.0.json#/definitions/Callback"
    _extra_properties = ["additionalProperties", "patternProperties"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=Callback._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Callback", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Callback")
        if self.node is not None:
            self.node.attach(ctx, d, self)

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            ctx.run(k, self.additional_properties.visit, v)

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/Callback/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Callback._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=Callback._PatternProperties_x, logger=logger
        )


class Operation(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/Operation"
    _properties = [
        "callbacks",
        "deprecated",
        "description",
        "externalDocs",
        "operationId",
        "parameters",
        "requestBody",
        "responses",
        "security",
        "servers",
        "summary",
        "tags",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = [
        "tags",
        "externalDocs",
        "parameters",
        "requestBody",
        "responses",
        "callbacks",
        "security",
        "servers",
    ]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=Operation._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Operation", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Operation")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "tags" in d:
            ctx.run("tags", self.tags.visit, d["tags"])
        if "externalDocs" in d:
            ctx.run("externalDocs", self.externalDocs.visit, d["externalDocs"])
        if "parameters" in d:
            ctx.run("parameters", self.parameters.visit, d["parameters"])
        if "requestBody" in d:
            ctx.run("requestBody", self.requestBody.visit, d["requestBody"])
        if "responses" in d:
            ctx.run("responses", self.responses.visit, d["responses"])
        if "callbacks" in d:
            ctx.run("callbacks", self.callbacks.visit, d["callbacks"])
        if "security" in d:
            ctx.run("security", self.security.visit, d["security"])
        if "servers" in d:
            ctx.run("servers", self.servers.visit, d["servers"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    @reify
    def externalDocs(self):
        return runtime.resolve_visitor(
            "externalDocs", cls=ExternalDocumentation, logger=logger
        )

    @reify
    def responses(self):
        return runtime.resolve_visitor("responses", cls=Responses, logger=logger)

    # anonymous definition for 'tags' (TODO: nodename)
    class _Tags(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Operation/tags"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Operation._Tags", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Tags")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def tags(self):
        return runtime.resolve_visitor("tags", cls=Operation._Tags, logger=logger)

    # anonymous definition for 'servers' (TODO: nodename)
    class _Servers(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Operation/servers"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Operation._Servers", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Servers")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def servers(self):
        return runtime.resolve_visitor("servers", cls=Operation._Servers, logger=logger)

    # anonymous definition for 'security' (TODO: nodename)
    class _Security(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Operation/security"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Operation._Security", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Security")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def security(self):
        return runtime.resolve_visitor(
            "security", cls=Operation._Security, logger=logger
        )

    # anonymous definition for 'callbacks' (TODO: nodename)
    class _Callbacks(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Operation/callbacks"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Operation._Callbacks", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Callbacks")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Operation/callbacks/additionalProperties"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Operation._Callbacks._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Callback, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=Operation._Callbacks._AdditionalProperties,
                logger=logger,
            )

    @reify
    def callbacks(self):
        return runtime.resolve_visitor(
            "callbacks", cls=Operation._Callbacks, logger=logger
        )

    # anonymous definition for 'parameters' (TODO: nodename)
    class _Parameters(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Operation/parameters"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Operation._Parameters", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Parameters")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        # anonymous definition for 'items' (TODO: nodename)
        class _Items(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Operation/parameters/items"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Operation._Parameters._Items", here=__name__, logger=logger
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_Items")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Parameter, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def items(self):
            return runtime.resolve_visitor(
                "items", cls=Operation._Parameters._Items, logger=logger
            )

    @reify
    def parameters(self):
        return runtime.resolve_visitor(
            "parameters", cls=Operation._Parameters, logger=logger
        )

    # anonymous definition for 'requestBody' (TODO: nodename)
    class _RequestBody(Visitor):
        _schema_type = "oneOf"
        _roles = ["combine_type", "has_expanded"]
        _uid = "/data/openapi-3.0.json#/definitions/Operation/requestBody"
        _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Operation._RequestBody", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            # for oneOf (xxx: _case is module global)
            if _case.when(d, "#/definitions/1"):
                return ctx.run(None, self.oneOf0.visit, d)
            if _case.when(d, "#/definitions/3"):
                return ctx.run(None, self.oneOf1.visit, d)
            raise ValueError("unexpected value")  # todo gentle message

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_RequestBody")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        @reify
        def oneOf0(self):
            return runtime.resolve_visitor("oneOf0", cls=RequestBody, logger=logger)

        @reify
        def oneOf1(self):
            return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

    @reify
    def requestBody(self):
        return runtime.resolve_visitor(
            "requestBody", cls=Operation._RequestBody, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/Operation/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Operation._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=Operation._PatternProperties_x, logger=logger
        )


class PathItem(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/PathItem"
    _properties = [
        "$ref",
        "delete",
        "description",
        "get",
        "head",
        "options",
        "parameters",
        "patch",
        "post",
        "put",
        "servers",
        "summary",
        "trace",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = [
        "get",
        "put",
        "post",
        "delete",
        "options",
        "head",
        "patch",
        "trace",
        "servers",
        "parameters",
    ]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=PathItem._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.PathItem", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "PathItem")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "get" in d:
            ctx.run("get", self.get.visit, d["get"])
        if "put" in d:
            ctx.run("put", self.put.visit, d["put"])
        if "post" in d:
            ctx.run("post", self.post.visit, d["post"])
        if "delete" in d:
            ctx.run("delete", self.delete.visit, d["delete"])
        if "options" in d:
            ctx.run("options", self.options.visit, d["options"])
        if "head" in d:
            ctx.run("head", self.head.visit, d["head"])
        if "patch" in d:
            ctx.run("patch", self.patch.visit, d["patch"])
        if "trace" in d:
            ctx.run("trace", self.trace.visit, d["trace"])
        if "servers" in d:
            ctx.run("servers", self.servers.visit, d["servers"])
        if "parameters" in d:
            ctx.run("parameters", self.parameters.visit, d["parameters"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    @reify
    def get(self):
        return runtime.resolve_visitor("get", cls=Operation, logger=logger)

    @reify
    def put(self):
        return runtime.resolve_visitor("put", cls=Operation, logger=logger)

    @reify
    def post(self):
        return runtime.resolve_visitor("post", cls=Operation, logger=logger)

    @reify
    def delete(self):
        return runtime.resolve_visitor("delete", cls=Operation, logger=logger)

    @reify
    def options(self):
        return runtime.resolve_visitor("options", cls=Operation, logger=logger)

    @reify
    def head(self):
        return runtime.resolve_visitor("head", cls=Operation, logger=logger)

    @reify
    def patch(self):
        return runtime.resolve_visitor("patch", cls=Operation, logger=logger)

    @reify
    def trace(self):
        return runtime.resolve_visitor("trace", cls=Operation, logger=logger)

    # anonymous definition for 'servers' (TODO: nodename)
    class _Servers(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/PathItem/servers"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.PathItem._Servers", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Servers")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def servers(self):
        return runtime.resolve_visitor("servers", cls=PathItem._Servers, logger=logger)

    # anonymous definition for 'parameters' (TODO: nodename)
    class _Parameters(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/PathItem/parameters"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.PathItem._Parameters", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Parameters")
            if self.node is not None:
                self.node.attach(ctx, d, self)

        # anonymous definition for 'items' (TODO: nodename)
        class _Items(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/PathItem/parameters/items"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.PathItem._Parameters._Items", here=__name__, logger=logger
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_Items")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Parameter, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Reference, logger=logger)

        @reify
        def items(self):
            return runtime.resolve_visitor(
                "items", cls=PathItem._Parameters._Items, logger=logger
            )

    @reify
    def parameters(self):
        return runtime.resolve_visitor(
            "parameters", cls=PathItem._Parameters, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/PathItem/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.PathItem._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=PathItem._PatternProperties_x, logger=logger
        )


class Paths(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name"]
    _uid = "/data/openapi-3.0.json#/definitions/Paths"
    _extra_properties = ["additionalProperties", "patternProperties"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^\\/"),
                runtime.resolve_visitor("^\\/", cls=PathItem, logger=logger),
            ),
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=Paths._PatternProperties_x, logger=logger
                ),
            ),
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Paths", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Paths")
        if self.node is not None:
            self.node.attach(ctx, d, self)

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/Paths/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Paths._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=Paths._PatternProperties_x, logger=logger
        )


class APIKeySecurityScheme(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/APIKeySecurityScheme"
    _properties = ["description", "in", "name", "type"]
    _extra_properties = ["additionalProperties", "patternProperties"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=APIKeySecurityScheme._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.APIKeySecurityScheme", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "APIKeySecurityScheme")
        if self.node is not None:
            self.node.attach(ctx, d, self)

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/APIKeySecurityScheme/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.APIKeySecurityScheme._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=APIKeySecurityScheme._PatternProperties_x,
            logger=logger,
        )


class NonBearerHTTPSecurityScheme(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/NonBearerHTTPSecurityScheme"
    _properties = ["description", "scheme", "type"]
    _extra_properties = ["additionalProperties", "patternProperties"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=NonBearerHTTPSecurityScheme._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.NonBearerHTTPSecurityScheme", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "NonBearerHTTPSecurityScheme")
        if self.node is not None:
            self.node.attach(ctx, d, self)

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/NonBearerHTTPSecurityScheme/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.NonBearerHTTPSecurityScheme._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=NonBearerHTTPSecurityScheme._PatternProperties_x,
            logger=logger,
        )


class BearerHTTPSecurityScheme(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/BearerHTTPSecurityScheme"
    _properties = ["bearerFormat", "description", "scheme", "type"]
    _extra_properties = ["additionalProperties", "patternProperties"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=BearerHTTPSecurityScheme._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.BearerHTTPSecurityScheme", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "BearerHTTPSecurityScheme")
        if self.node is not None:
            self.node.attach(ctx, d, self)

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/BearerHTTPSecurityScheme/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.BearerHTTPSecurityScheme._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=BearerHTTPSecurityScheme._PatternProperties_x,
            logger=logger,
        )


class HTTPSecurityScheme(Visitor):
    _schema_type = "oneOf"
    _roles = ["combine_type", "has_expanded", "has_name"]
    _uid = "/data/openapi-3.0.json#/definitions/HTTPSecurityScheme"
    _xxx_of_definitions = [{"$ref": "#/definitions/1"}, {"$ref": "#/definitions/3"}]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.HTTPSecurityScheme", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        # for oneOf (xxx: _case is module global)
        if _case.when(d, "#/definitions/1"):
            return ctx.run(None, self.oneOf0.visit, d)
        if _case.when(d, "#/definitions/3"):
            return ctx.run(None, self.oneOf1.visit, d)
        raise ValueError("unexpected value")  # todo gentle message

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "HTTPSecurityScheme")
        if self.node is not None:
            self.node.attach(ctx, d, self)

    @reify
    def oneOf0(self):
        return runtime.resolve_visitor(
            "oneOf0", cls=NonBearerHTTPSecurityScheme, logger=logger
        )

    @reify
    def oneOf1(self):
        return runtime.resolve_visitor(
            "oneOf1", cls=BearerHTTPSecurityScheme, logger=logger
        )


class ImplicitOAuthFlow(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/ImplicitOAuthFlow"
    _properties = ["authorizationUrl", "refreshUrl", "scopes"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["scopes"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=ImplicitOAuthFlow._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ImplicitOAuthFlow", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ImplicitOAuthFlow")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "scopes" in d:
            ctx.run("scopes", self.scopes.visit, d["scopes"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'scopes' (TODO: nodename)
    class _Scopes(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/ImplicitOAuthFlow/scopes"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ImplicitOAuthFlow._Scopes", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Scopes")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "string"
            _roles = ["field_of_something", "primitive_type"]
            _uid = "/data/openapi-3.0.json#/definitions/ImplicitOAuthFlow/scopes/additionalProperties"

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.ImplicitOAuthFlow._Scopes._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: simplify

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=ImplicitOAuthFlow._Scopes._AdditionalProperties,
                logger=logger,
            )

    @reify
    def scopes(self):
        return runtime.resolve_visitor(
            "scopes", cls=ImplicitOAuthFlow._Scopes, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/ImplicitOAuthFlow/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ImplicitOAuthFlow._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=ImplicitOAuthFlow._PatternProperties_x,
            logger=logger,
        )


class PasswordOAuthFlow(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/PasswordOAuthFlow"
    _properties = ["refreshUrl", "scopes", "tokenUrl"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["scopes"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=PasswordOAuthFlow._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.PasswordOAuthFlow", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "PasswordOAuthFlow")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "scopes" in d:
            ctx.run("scopes", self.scopes.visit, d["scopes"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'scopes' (TODO: nodename)
    class _Scopes(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/PasswordOAuthFlow/scopes"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.PasswordOAuthFlow._Scopes", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Scopes")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "string"
            _roles = ["field_of_something", "primitive_type"]
            _uid = "/data/openapi-3.0.json#/definitions/PasswordOAuthFlow/scopes/additionalProperties"

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.PasswordOAuthFlow._Scopes._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: simplify

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=PasswordOAuthFlow._Scopes._AdditionalProperties,
                logger=logger,
            )

    @reify
    def scopes(self):
        return runtime.resolve_visitor(
            "scopes", cls=PasswordOAuthFlow._Scopes, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/PasswordOAuthFlow/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.PasswordOAuthFlow._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=PasswordOAuthFlow._PatternProperties_x,
            logger=logger,
        )


class ClientCredentialsFlow(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/ClientCredentialsFlow"
    _properties = ["refreshUrl", "scopes", "tokenUrl"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["scopes"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=ClientCredentialsFlow._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.ClientCredentialsFlow", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "ClientCredentialsFlow")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "scopes" in d:
            ctx.run("scopes", self.scopes.visit, d["scopes"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'scopes' (TODO: nodename)
    class _Scopes(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/ClientCredentialsFlow/scopes"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ClientCredentialsFlow._Scopes", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Scopes")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "string"
            _roles = ["field_of_something", "primitive_type"]
            _uid = "/data/openapi-3.0.json#/definitions/ClientCredentialsFlow/scopes/additionalProperties"

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.ClientCredentialsFlow._Scopes._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: simplify

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=ClientCredentialsFlow._Scopes._AdditionalProperties,
                logger=logger,
            )

    @reify
    def scopes(self):
        return runtime.resolve_visitor(
            "scopes", cls=ClientCredentialsFlow._Scopes, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/ClientCredentialsFlow/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.ClientCredentialsFlow._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=ClientCredentialsFlow._PatternProperties_x,
            logger=logger,
        )


class AuthorizationCodeOAuthFlow(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/AuthorizationCodeOAuthFlow"
    _properties = ["authorizationUrl", "refreshUrl", "scopes", "tokenUrl"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["scopes"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=AuthorizationCodeOAuthFlow._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.AuthorizationCodeOAuthFlow", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "AuthorizationCodeOAuthFlow")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "scopes" in d:
            ctx.run("scopes", self.scopes.visit, d["scopes"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'scopes' (TODO: nodename)
    class _Scopes(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/AuthorizationCodeOAuthFlow/scopes"
        _extra_properties = ["additionalProperties"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.AuthorizationCodeOAuthFlow._Scopes",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Scopes")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # additionalProperties
            for k, v in d.items():
                if k in self._properties:
                    continue
                ctx.run(k, self.additional_properties.visit, v)

        # anonymous definition for 'additionalProperties' (TODO: nodename)
        class _AdditionalProperties(Visitor):
            _schema_type = "string"
            _roles = ["field_of_something", "primitive_type"]
            _uid = "/data/openapi-3.0.json#/definitions/AuthorizationCodeOAuthFlow/scopes/additionalProperties"

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.AuthorizationCodeOAuthFlow._Scopes._AdditionalProperties",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                return self._visit(ctx, d)  # todo: simplify

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_AdditionalProperties")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

        @reify
        def additionalProperties(self):
            return runtime.resolve_visitor(
                "additionalProperties",
                cls=AuthorizationCodeOAuthFlow._Scopes._AdditionalProperties,
                logger=logger,
            )

    @reify
    def scopes(self):
        return runtime.resolve_visitor(
            "scopes", cls=AuthorizationCodeOAuthFlow._Scopes, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/AuthorizationCodeOAuthFlow/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.AuthorizationCodeOAuthFlow._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=AuthorizationCodeOAuthFlow._PatternProperties_x,
            logger=logger,
        )


class OAuthFlows(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/OAuthFlows"
    _properties = ["authorizationCode", "clientCredentials", "implicit", "password"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["implicit", "password", "clientCredentials", "authorizationCode"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=OAuthFlows._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.OAuthFlows", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "OAuthFlows")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "implicit" in d:
            ctx.run("implicit", self.implicit.visit, d["implicit"])
        if "password" in d:
            ctx.run("password", self.password.visit, d["password"])
        if "clientCredentials" in d:
            ctx.run(
                "clientCredentials",
                self.clientCredentials.visit,
                d["clientCredentials"],
            )
        if "authorizationCode" in d:
            ctx.run(
                "authorizationCode",
                self.authorizationCode.visit,
                d["authorizationCode"],
            )

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    @reify
    def implicit(self):
        return runtime.resolve_visitor("implicit", cls=ImplicitOAuthFlow, logger=logger)

    @reify
    def password(self):
        return runtime.resolve_visitor("password", cls=PasswordOAuthFlow, logger=logger)

    @reify
    def clientCredentials(self):
        return runtime.resolve_visitor(
            "clientCredentials", cls=ClientCredentialsFlow, logger=logger
        )

    @reify
    def authorizationCode(self):
        return runtime.resolve_visitor(
            "authorizationCode", cls=AuthorizationCodeOAuthFlow, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/OAuthFlows/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.OAuthFlows._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=OAuthFlows._PatternProperties_x, logger=logger
        )


class OAuth2SecurityScheme(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/OAuth2SecurityScheme"
    _properties = ["description", "flows", "type"]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = ["flows"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=OAuth2SecurityScheme._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.OAuth2SecurityScheme", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "OAuth2SecurityScheme")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "flows" in d:
            ctx.run("flows", self.flows.visit, d["flows"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    @reify
    def flows(self):
        return runtime.resolve_visitor("flows", cls=OAuthFlows, logger=logger)

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/OAuth2SecurityScheme/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.OAuth2SecurityScheme._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=OAuth2SecurityScheme._PatternProperties_x,
            logger=logger,
        )


class OpenIdConnectSecurityScheme(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/OpenIdConnectSecurityScheme"
    _properties = ["description", "openIdConnectUrl", "type"]
    _extra_properties = ["additionalProperties", "patternProperties"]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-",
                    cls=OpenIdConnectSecurityScheme._PatternProperties_x,
                    logger=logger,
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.OpenIdConnectSecurityScheme", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "OpenIdConnectSecurityScheme")
        if self.node is not None:
            self.node.attach(ctx, d, self)

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/OpenIdConnectSecurityScheme/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.OpenIdConnectSecurityScheme._PatternProperties_x",
                here=__name__,
                logger=logger,
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-",
            cls=OpenIdConnectSecurityScheme._PatternProperties_x,
            logger=logger,
        )


class SecurityScheme(Visitor):
    _schema_type = "oneOf"
    _roles = ["combine_type", "has_expanded", "has_name"]
    _uid = "/data/openapi-3.0.json#/definitions/SecurityScheme"
    _xxx_of_definitions = [
        {"$ref": "#/definitions/1"},
        {"$ref": "#/definitions/3"},
        {"$ref": "#/definitions/45"},
        {"$ref": "#/definitions/46"},
    ]

    @reify
    def node(self):
        return runtime.resolve_node(
            ".nodes.SecurityScheme", here=__name__, logger=logger
        )

    def visit(self, ctx: Context, d: dict):
        # for oneOf (xxx: _case is module global)
        if _case.when(d, "#/definitions/1"):
            return ctx.run(None, self.oneOf0.visit, d)
        if _case.when(d, "#/definitions/3"):
            return ctx.run(None, self.oneOf1.visit, d)
        if _case.when(d, "#/definitions/45"):
            return ctx.run(None, self.oneOf2.visit, d)
        if _case.when(d, "#/definitions/46"):
            return ctx.run(None, self.oneOf3.visit, d)
        raise ValueError("unexpected value")  # todo gentle message

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "SecurityScheme")
        if self.node is not None:
            self.node.attach(ctx, d, self)

    @reify
    def oneOf0(self):
        return runtime.resolve_visitor(
            "oneOf0", cls=APIKeySecurityScheme, logger=logger
        )

    @reify
    def oneOf1(self):
        return runtime.resolve_visitor("oneOf1", cls=HTTPSecurityScheme, logger=logger)

    @reify
    def oneOf2(self):
        return runtime.resolve_visitor(
            "oneOf2", cls=OAuth2SecurityScheme, logger=logger
        )

    @reify
    def oneOf3(self):
        return runtime.resolve_visitor(
            "oneOf3", cls=OpenIdConnectSecurityScheme, logger=logger
        )


class Components(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_name", "has_properties"]
    _uid = "/data/openapi-3.0.json#/definitions/Components"
    _properties = [
        "callbacks",
        "examples",
        "headers",
        "links",
        "parameters",
        "requestBodies",
        "responses",
        "schemas",
        "securitySchemes",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = [
        "schemas",
        "responses",
        "parameters",
        "examples",
        "requestBodies",
        "headers",
        "securitySchemes",
        "links",
        "callbacks",
    ]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=Components._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Components", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Components")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "schemas" in d:
            ctx.run("schemas", self.schemas.visit, d["schemas"])
        if "responses" in d:
            ctx.run("responses", self.responses.visit, d["responses"])
        if "parameters" in d:
            ctx.run("parameters", self.parameters.visit, d["parameters"])
        if "examples" in d:
            ctx.run("examples", self.examples.visit, d["examples"])
        if "requestBodies" in d:
            ctx.run("requestBodies", self.requestBodies.visit, d["requestBodies"])
        if "headers" in d:
            ctx.run("headers", self.headers.visit, d["headers"])
        if "securitySchemes" in d:
            ctx.run("securitySchemes", self.securitySchemes.visit, d["securitySchemes"])
        if "links" in d:
            ctx.run("links", self.links.visit, d["links"])
        if "callbacks" in d:
            ctx.run("callbacks", self.callbacks.visit, d["callbacks"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    # anonymous definition for 'links' (TODO: nodename)
    class _Links(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Components/links"
        _extra_properties = ["patternProperties"]

        @reify
        def _pattern_properties_regexes(self):
            return [
                (
                    re.compile("^[a-zA-Z0-9\\.\\-_]+$"),
                    runtime.resolve_visitor(
                        "^[a-zA-Z0-9\\.\\-_]+$",
                        cls=Components._Links._PatternProperties_aZAZ09,
                        logger=logger,
                    ),
                )
            ]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Components._Links", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Links")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # patternProperties
            for rx, visitor in self._pattern_properties_regexes:
                for k, v in d.items():
                    m = rx.search(k)
                    if m is not None and visitor is not None:
                        ctx.run(k, visitor.visit, v)

        # anonymous definition for 'patternProperties/^[a-zA-Z0-9\\.\\-_]+$' (TODO: nodename)
        class _PatternProperties_aZAZ09(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Components/links/patternProperties/^[a-zA-Z0-9\\.\\-_]+$"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Components._Links._PatternProperties_aZAZ09",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_PatternProperties_aZAZ09")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Reference, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Link, logger=logger)

        @reify
        def patternProperties_a_zA_Z0_9(self):
            return runtime.resolve_visitor(
                "patternProperties/^[a-zA-Z0-9\\.\\-_]+$",
                cls=Components._Links._PatternProperties_aZAZ09,
                logger=logger,
            )

    @reify
    def links(self):
        return runtime.resolve_visitor("links", cls=Components._Links, logger=logger)

    # anonymous definition for 'schemas' (TODO: nodename)
    class _Schemas(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Components/schemas"
        _extra_properties = ["patternProperties"]

        @reify
        def _pattern_properties_regexes(self):
            return [
                (
                    re.compile("^[a-zA-Z0-9\\.\\-_]+$"),
                    runtime.resolve_visitor(
                        "^[a-zA-Z0-9\\.\\-_]+$",
                        cls=Components._Schemas._PatternProperties_aZAZ09,
                        logger=logger,
                    ),
                )
            ]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Components._Schemas", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Schemas")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # patternProperties
            for rx, visitor in self._pattern_properties_regexes:
                for k, v in d.items():
                    m = rx.search(k)
                    if m is not None and visitor is not None:
                        ctx.run(k, visitor.visit, v)

        # anonymous definition for 'patternProperties/^[a-zA-Z0-9\\.\\-_]+$' (TODO: nodename)
        class _PatternProperties_aZAZ09(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Components/schemas/patternProperties/^[a-zA-Z0-9\\.\\-_]+$"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Components._Schemas._PatternProperties_aZAZ09",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_PatternProperties_aZAZ09")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Reference, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Schema, logger=logger)

        @reify
        def patternProperties_a_zA_Z0_9(self):
            return runtime.resolve_visitor(
                "patternProperties/^[a-zA-Z0-9\\.\\-_]+$",
                cls=Components._Schemas._PatternProperties_aZAZ09,
                logger=logger,
            )

    @reify
    def schemas(self):
        return runtime.resolve_visitor(
            "schemas", cls=Components._Schemas, logger=logger
        )

    # anonymous definition for 'headers' (TODO: nodename)
    class _Headers(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Components/headers"
        _extra_properties = ["patternProperties"]

        @reify
        def _pattern_properties_regexes(self):
            return [
                (
                    re.compile("^[a-zA-Z0-9\\.\\-_]+$"),
                    runtime.resolve_visitor(
                        "^[a-zA-Z0-9\\.\\-_]+$",
                        cls=Components._Headers._PatternProperties_aZAZ09,
                        logger=logger,
                    ),
                )
            ]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Components._Headers", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Headers")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # patternProperties
            for rx, visitor in self._pattern_properties_regexes:
                for k, v in d.items():
                    m = rx.search(k)
                    if m is not None and visitor is not None:
                        ctx.run(k, visitor.visit, v)

        # anonymous definition for 'patternProperties/^[a-zA-Z0-9\\.\\-_]+$' (TODO: nodename)
        class _PatternProperties_aZAZ09(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Components/headers/patternProperties/^[a-zA-Z0-9\\.\\-_]+$"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Components._Headers._PatternProperties_aZAZ09",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_PatternProperties_aZAZ09")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Reference, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Header, logger=logger)

        @reify
        def patternProperties_a_zA_Z0_9(self):
            return runtime.resolve_visitor(
                "patternProperties/^[a-zA-Z0-9\\.\\-_]+$",
                cls=Components._Headers._PatternProperties_aZAZ09,
                logger=logger,
            )

    @reify
    def headers(self):
        return runtime.resolve_visitor(
            "headers", cls=Components._Headers, logger=logger
        )

    # anonymous definition for 'examples' (TODO: nodename)
    class _Examples(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Components/examples"
        _extra_properties = ["patternProperties"]

        @reify
        def _pattern_properties_regexes(self):
            return [
                (
                    re.compile("^[a-zA-Z0-9\\.\\-_]+$"),
                    runtime.resolve_visitor(
                        "^[a-zA-Z0-9\\.\\-_]+$",
                        cls=Components._Examples._PatternProperties_aZAZ09,
                        logger=logger,
                    ),
                )
            ]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Components._Examples", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Examples")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # patternProperties
            for rx, visitor in self._pattern_properties_regexes:
                for k, v in d.items():
                    m = rx.search(k)
                    if m is not None and visitor is not None:
                        ctx.run(k, visitor.visit, v)

        # anonymous definition for 'patternProperties/^[a-zA-Z0-9\\.\\-_]+$' (TODO: nodename)
        class _PatternProperties_aZAZ09(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Components/examples/patternProperties/^[a-zA-Z0-9\\.\\-_]+$"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Components._Examples._PatternProperties_aZAZ09",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_PatternProperties_aZAZ09")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Reference, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Example, logger=logger)

        @reify
        def patternProperties_a_zA_Z0_9(self):
            return runtime.resolve_visitor(
                "patternProperties/^[a-zA-Z0-9\\.\\-_]+$",
                cls=Components._Examples._PatternProperties_aZAZ09,
                logger=logger,
            )

    @reify
    def examples(self):
        return runtime.resolve_visitor(
            "examples", cls=Components._Examples, logger=logger
        )

    # anonymous definition for 'responses' (TODO: nodename)
    class _Responses(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Components/responses"
        _extra_properties = ["patternProperties"]

        @reify
        def _pattern_properties_regexes(self):
            return [
                (
                    re.compile("^[a-zA-Z0-9\\.\\-_]+$"),
                    runtime.resolve_visitor(
                        "^[a-zA-Z0-9\\.\\-_]+$",
                        cls=Components._Responses._PatternProperties_aZAZ09,
                        logger=logger,
                    ),
                )
            ]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Components._Responses", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Responses")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # patternProperties
            for rx, visitor in self._pattern_properties_regexes:
                for k, v in d.items():
                    m = rx.search(k)
                    if m is not None and visitor is not None:
                        ctx.run(k, visitor.visit, v)

        # anonymous definition for 'patternProperties/^[a-zA-Z0-9\\.\\-_]+$' (TODO: nodename)
        class _PatternProperties_aZAZ09(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Components/responses/patternProperties/^[a-zA-Z0-9\\.\\-_]+$"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Components._Responses._PatternProperties_aZAZ09",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_PatternProperties_aZAZ09")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Reference, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Response, logger=logger)

        @reify
        def patternProperties_a_zA_Z0_9(self):
            return runtime.resolve_visitor(
                "patternProperties/^[a-zA-Z0-9\\.\\-_]+$",
                cls=Components._Responses._PatternProperties_aZAZ09,
                logger=logger,
            )

    @reify
    def responses(self):
        return runtime.resolve_visitor(
            "responses", cls=Components._Responses, logger=logger
        )

    # anonymous definition for 'callbacks' (TODO: nodename)
    class _Callbacks(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Components/callbacks"
        _extra_properties = ["patternProperties"]

        @reify
        def _pattern_properties_regexes(self):
            return [
                (
                    re.compile("^[a-zA-Z0-9\\.\\-_]+$"),
                    runtime.resolve_visitor(
                        "^[a-zA-Z0-9\\.\\-_]+$",
                        cls=Components._Callbacks._PatternProperties_aZAZ09,
                        logger=logger,
                    ),
                )
            ]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Components._Callbacks", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Callbacks")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # patternProperties
            for rx, visitor in self._pattern_properties_regexes:
                for k, v in d.items():
                    m = rx.search(k)
                    if m is not None and visitor is not None:
                        ctx.run(k, visitor.visit, v)

        # anonymous definition for 'patternProperties/^[a-zA-Z0-9\\.\\-_]+$' (TODO: nodename)
        class _PatternProperties_aZAZ09(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Components/callbacks/patternProperties/^[a-zA-Z0-9\\.\\-_]+$"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Components._Callbacks._PatternProperties_aZAZ09",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_PatternProperties_aZAZ09")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Reference, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Callback, logger=logger)

        @reify
        def patternProperties_a_zA_Z0_9(self):
            return runtime.resolve_visitor(
                "patternProperties/^[a-zA-Z0-9\\.\\-_]+$",
                cls=Components._Callbacks._PatternProperties_aZAZ09,
                logger=logger,
            )

    @reify
    def callbacks(self):
        return runtime.resolve_visitor(
            "callbacks", cls=Components._Callbacks, logger=logger
        )

    # anonymous definition for 'parameters' (TODO: nodename)
    class _Parameters(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Components/parameters"
        _extra_properties = ["patternProperties"]

        @reify
        def _pattern_properties_regexes(self):
            return [
                (
                    re.compile("^[a-zA-Z0-9\\.\\-_]+$"),
                    runtime.resolve_visitor(
                        "^[a-zA-Z0-9\\.\\-_]+$",
                        cls=Components._Parameters._PatternProperties_aZAZ09,
                        logger=logger,
                    ),
                )
            ]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Components._Parameters", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Parameters")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # patternProperties
            for rx, visitor in self._pattern_properties_regexes:
                for k, v in d.items():
                    m = rx.search(k)
                    if m is not None and visitor is not None:
                        ctx.run(k, visitor.visit, v)

        # anonymous definition for 'patternProperties/^[a-zA-Z0-9\\.\\-_]+$' (TODO: nodename)
        class _PatternProperties_aZAZ09(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Components/parameters/patternProperties/^[a-zA-Z0-9\\.\\-_]+$"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Components._Parameters._PatternProperties_aZAZ09",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_PatternProperties_aZAZ09")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Reference, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=Parameter, logger=logger)

        @reify
        def patternProperties_a_zA_Z0_9(self):
            return runtime.resolve_visitor(
                "patternProperties/^[a-zA-Z0-9\\.\\-_]+$",
                cls=Components._Parameters._PatternProperties_aZAZ09,
                logger=logger,
            )

    @reify
    def parameters(self):
        return runtime.resolve_visitor(
            "parameters", cls=Components._Parameters, logger=logger
        )

    # anonymous definition for 'requestBodies' (TODO: nodename)
    class _RequestBodies(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Components/requestBodies"
        _extra_properties = ["patternProperties"]

        @reify
        def _pattern_properties_regexes(self):
            return [
                (
                    re.compile("^[a-zA-Z0-9\\.\\-_]+$"),
                    runtime.resolve_visitor(
                        "^[a-zA-Z0-9\\.\\-_]+$",
                        cls=Components._RequestBodies._PatternProperties_aZAZ09,
                        logger=logger,
                    ),
                )
            ]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Components._RequestBodies", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_RequestBodies")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # patternProperties
            for rx, visitor in self._pattern_properties_regexes:
                for k, v in d.items():
                    m = rx.search(k)
                    if m is not None and visitor is not None:
                        ctx.run(k, visitor.visit, v)

        # anonymous definition for 'patternProperties/^[a-zA-Z0-9\\.\\-_]+$' (TODO: nodename)
        class _PatternProperties_aZAZ09(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Components/requestBodies/patternProperties/^[a-zA-Z0-9\\.\\-_]+$"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Components._RequestBodies._PatternProperties_aZAZ09",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_PatternProperties_aZAZ09")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Reference, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor("oneOf1", cls=RequestBody, logger=logger)

        @reify
        def patternProperties_a_zA_Z0_9(self):
            return runtime.resolve_visitor(
                "patternProperties/^[a-zA-Z0-9\\.\\-_]+$",
                cls=Components._RequestBodies._PatternProperties_aZAZ09,
                logger=logger,
            )

    @reify
    def requestBodies(self):
        return runtime.resolve_visitor(
            "requestBodies", cls=Components._RequestBodies, logger=logger
        )

    # anonymous definition for 'securitySchemes' (TODO: nodename)
    class _SecuritySchemes(Visitor):
        _schema_type = "object"
        _roles = ["has_extra_properties"]
        _uid = "/data/openapi-3.0.json#/definitions/Components/securitySchemes"
        _extra_properties = ["patternProperties"]

        @reify
        def _pattern_properties_regexes(self):
            return [
                (
                    re.compile("^[a-zA-Z0-9\\.\\-_]+$"),
                    runtime.resolve_visitor(
                        "^[a-zA-Z0-9\\.\\-_]+$",
                        cls=Components._SecuritySchemes._PatternProperties_aZAZ09,
                        logger=logger,
                    ),
                )
            ]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Components._SecuritySchemes", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_SecuritySchemes")
            if self.node is not None:
                self.node.attach(ctx, d, self)

            # patternProperties
            for rx, visitor in self._pattern_properties_regexes:
                for k, v in d.items():
                    m = rx.search(k)
                    if m is not None and visitor is not None:
                        ctx.run(k, visitor.visit, v)

        # anonymous definition for 'patternProperties/^[a-zA-Z0-9\\.\\-_]+$' (TODO: nodename)
        class _PatternProperties_aZAZ09(Visitor):
            _schema_type = "oneOf"
            _roles = ["combine_type", "field_of_something", "has_expanded"]
            _uid = "/data/openapi-3.0.json#/definitions/Components/securitySchemes/patternProperties/^[a-zA-Z0-9\\.\\-_]+$"
            _xxx_of_definitions = [
                {"$ref": "#/definitions/1"},
                {"$ref": "#/definitions/3"},
            ]

            @reify
            def node(self):
                return runtime.resolve_node(
                    ".nodes.Components._SecuritySchemes._PatternProperties_aZAZ09",
                    here=__name__,
                    logger=logger,
                )

            def visit(self, ctx: Context, d: dict):
                # for oneOf (xxx: _case is module global)
                if _case.when(d, "#/definitions/1"):
                    return ctx.run(None, self.oneOf0.visit, d)
                if _case.when(d, "#/definitions/3"):
                    return ctx.run(None, self.oneOf1.visit, d)
                raise ValueError("unexpected value")  # todo gentle message

            def _visit(self, ctx: Context, d: dict):
                logger.debug("visit: %s", "_PatternProperties_aZAZ09")
                if self.node is not None:
                    self.node.attach(ctx, d, self)

            @reify
            def oneOf0(self):
                return runtime.resolve_visitor("oneOf0", cls=Reference, logger=logger)

            @reify
            def oneOf1(self):
                return runtime.resolve_visitor(
                    "oneOf1", cls=SecurityScheme, logger=logger
                )

        @reify
        def patternProperties_a_zA_Z0_9(self):
            return runtime.resolve_visitor(
                "patternProperties/^[a-zA-Z0-9\\.\\-_]+$",
                cls=Components._SecuritySchemes._PatternProperties_aZAZ09,
                logger=logger,
            )

    @reify
    def securitySchemes(self):
        return runtime.resolve_visitor(
            "securitySchemes", cls=Components._SecuritySchemes, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something"]
        _uid = "/data/openapi-3.0.json#/definitions/Components/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Components._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=Components._PatternProperties_x, logger=logger
        )


class Toplevel(Visitor):
    _schema_type = "object"
    _roles = ["has_extra_properties", "has_properties", "toplevel_properties"]
    _uid = "/data/openapi-3.0.json#/"
    _properties = [
        "components",
        "externalDocs",
        "info",
        "openapi",
        "paths",
        "security",
        "servers",
        "tags",
    ]
    _extra_properties = ["additionalProperties", "patternProperties"]
    _links = [
        "info",
        "externalDocs",
        "servers",
        "security",
        "tags",
        "paths",
        "components",
    ]

    @reify
    def _pattern_properties_regexes(self):
        return [
            (
                re.compile("^x-"),
                runtime.resolve_visitor(
                    "^x-", cls=Toplevel._PatternProperties_x, logger=logger
                ),
            )
        ]

    @reify
    def node(self):
        return runtime.resolve_node(".nodes.Toplevel", here=__name__, logger=logger)

    def visit(self, ctx: Context, d: dict):
        return self._visit(ctx, d)  # todo: remove this code

    def _visit(self, ctx: Context, d: dict):
        logger.debug("visit: %s", "Toplevel")
        if self.node is not None:
            self.node.attach(ctx, d, self)
        if "info" in d:
            ctx.run("info", self.info.visit, d["info"])
        if "externalDocs" in d:
            ctx.run("externalDocs", self.externalDocs.visit, d["externalDocs"])
        if "servers" in d:
            ctx.run("servers", self.servers.visit, d["servers"])
        if "security" in d:
            ctx.run("security", self.security.visit, d["security"])
        if "tags" in d:
            ctx.run("tags", self.tags.visit, d["tags"])
        if "paths" in d:
            ctx.run("paths", self.paths.visit, d["paths"])
        if "components" in d:
            ctx.run("components", self.components.visit, d["components"])

        # patternProperties
        for rx, visitor in self._pattern_properties_regexes:
            for k, v in d.items():
                m = rx.search(k)
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
            logger.warning(
                "unexpected property is found: %r, where=%s", k, self.__class__.__name__
            )

    @reify
    def info(self):
        return runtime.resolve_visitor("info", cls=Info, logger=logger)

    @reify
    def externalDocs(self):
        return runtime.resolve_visitor(
            "externalDocs", cls=ExternalDocumentation, logger=logger
        )

    @reify
    def paths(self):
        return runtime.resolve_visitor("paths", cls=Paths, logger=logger)

    @reify
    def components(self):
        return runtime.resolve_visitor("components", cls=Components, logger=logger)

    # anonymous definition for 'tags' (TODO: nodename)
    class _Tags(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties", "toplevel_properties"]
        _uid = "/data/openapi-3.0.json#/tags"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Toplevel._Tags", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Tags")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def tags(self):
        return runtime.resolve_visitor("tags", cls=Toplevel._Tags, logger=logger)

    # anonymous definition for 'servers' (TODO: nodename)
    class _Servers(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties", "toplevel_properties"]
        _uid = "/data/openapi-3.0.json#/servers"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Toplevel._Servers", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Servers")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def servers(self):
        return runtime.resolve_visitor("servers", cls=Toplevel._Servers, logger=logger)

    # anonymous definition for 'security' (TODO: nodename)
    class _Security(Visitor):
        _schema_type = "array"
        _roles = ["has_extra_properties", "toplevel_properties"]
        _uid = "/data/openapi-3.0.json#/security"
        _extra_properties = ["items"]

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Toplevel._Security", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return [self._visit(ctx, x) for x in d]

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_Security")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def security(self):
        return runtime.resolve_visitor(
            "security", cls=Toplevel._Security, logger=logger
        )

    # anonymous definition for 'patternProperties/^x-' (TODO: nodename)
    class _PatternProperties_x(Visitor):
        _schema_type = "any"
        _roles = ["field_of_something", "toplevel_properties"]
        _uid = "/data/openapi-3.0.json#/patternProperties/^x-"

        @reify
        def node(self):
            return runtime.resolve_node(
                ".nodes.Toplevel._PatternProperties_x", here=__name__, logger=logger
            )

        def visit(self, ctx: Context, d: dict):
            return self._visit(ctx, d)  # todo: remove this code

        def _visit(self, ctx: Context, d: dict):
            logger.debug("visit: %s", "_PatternProperties_x")
            if self.node is not None:
                self.node.attach(ctx, d, self)

    @reify
    def patternProperties_x(self):
        return runtime.resolve_visitor(
            "patternProperties/^x-", cls=Toplevel._PatternProperties_x, logger=logger
        )


# fmt: off
_case = runtime.Case({'definitions': {'1': {'type': 'object', 'properties': {'title': {'type': 'string'}, 'multipleOf': {'type': 'number', 'minimum': 0, 'exclusiveMinimum': True}, 'maximum': {'type': 'number'}, 'exclusiveMaximum': {'type': 'boolean', 'default': False}, 'minimum': {'type': 'number'}, 'exclusiveMinimum': {'type': 'boolean', 'default': False}, 'maxLength': {'type': 'integer', 'minimum': 0}, 'minLength': {'type': 'integer', 'minimum': 0, 'default': 0}, 'pattern': {'type': 'string', 'format': 'regex'}, 'maxItems': {'type': 'integer', 'minimum': 0}, 'minItems': {'type': 'integer', 'minimum': 0, 'default': 0}, 'uniqueItems': {'type': 'boolean', 'default': False}, 'maxProperties': {'type': 'integer', 'minimum': 0}, 'minProperties': {'type': 'integer', 'minimum': 0, 'default': 0}, 'required': {'type': 'array', 'items': {'type': 'string'}, 'minItems': 1, 'uniqueItems': True}, 'enum': {'type': 'array', 'items': {}, 'minItems': 1}, 'type': {'type': 'string', 'enum': ['array', 'boolean', 'integer', 'number', 'object', 'string']}, 'not': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'allOf': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}}, 'oneOf': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}}, 'anyOf': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}}, 'items': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'properties': {'type': 'object', 'additionalProperties': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}}, 'additionalProperties': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}, {'$ref': '#/definitions/2'}], 'default': True}, 'format': {'type': 'string'}, 'default': {}, 'nullable': {'type': 'boolean', 'default': False}, 'discriminator': {'$ref': '#/definitions/Discriminator'}, 'readOnly': {'type': 'boolean', 'default': False}, 'writeOnly': {'type': 'boolean', 'default': False}, 'example': {}, 'externalDocs': {'$ref': '#/definitions/ExternalDocumentation'}, 'deprecated': {'type': 'boolean', 'default': False}, 'xml': {'$ref': '#/definitions/XML'}}, 'patternProperties': {'^x-': {}}, 'additionalProperties': False}, '2': {'type': 'boolean'}, '3': {'type': 'object', 'required': ['$ref'], 'properties': {'$ref': {'type': 'string', 'format': 'uriref'}}}, '19': {'type': 'object', 'required': ['propertyName'], 'properties': {'propertyName': {'type': 'string'}, 'mapping': {'type': 'object', 'additionalProperties': {'type': 'string'}}}}, '20': {'type': 'object', 'required': ['url'], 'properties': {'url': {'type': 'string', 'format': 'uriref'}}, 'patternProperties': {'^x-': {}}, 'additionalProperties': False}, '21': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'namespace': {'type': 'string', 'format': 'url'}, 'prefix': {'type': 'string'}, 'attribute': {'type': 'boolean', 'default': False}, 'wrapped': {'type': 'boolean', 'default': False}}, 'patternProperties': {'^x-': {}}, 'additionalProperties': False}, '34': {'type': 'boolean'}, '45': {'type': 'object', 'required': ['name', 'in', 'schema'], 'properties': {'name': {'type': 'string'}, 'in': {'type': 'string', 'enum': ['header']}, 'required': {'type': 'boolean', 'default': False}, 'deprecated': {'type': 'boolean', 'default': False}, 'allowEmptyValue': {'type': 'boolean', 'default': False}, 'style': {'type': 'string', 'enum': ['simple'], 'default': 'simple'}, 'explode': {'type': 'boolean'}, 'allowReserved': {'type': 'boolean', 'default': False}, 'schema': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'example': {}}, 'patternProperties': {'^x-': {}}, 'additionalProperties': False}, '46': {'type': 'object', 'required': ['name', 'in', 'schema'], 'properties': {'name': {'type': 'string'}, 'in': {'type': 'string', 'enum': ['cookie']}, 'required': {'type': 'boolean', 'default': False}, 'deprecated': {'type': 'boolean', 'default': False}, 'allowEmptyValue': {'type': 'boolean', 'default': False}, 'style': {'type': 'string', 'enum': ['form'], 'default': 'form'}, 'explode': {'type': 'boolean'}, 'allowReserved': {'type': 'boolean', 'default': False}, 'schema': {'oneOf': [{'$ref': '#/definitions/1'}, {'$ref': '#/definitions/3'}]}, 'example': {}}, 'patternProperties': {'^x-': {}}, 'additionalProperties': False}}})
# fmt: on
