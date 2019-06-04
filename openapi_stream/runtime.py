import sys
from importlib import import_module
from dictknife.jsonknife import access_by_json_pointer, path_to_json_pointer
from openapi_stream import Context


class MismatchError(ValueError):
    def __init__(self, msg: str, *, ctx: Context, visitor=None) -> None:
        ref = path_to_json_pointer(ctx.path)
        super().__init__(
            f"{msg} (where ref={ref!r}, visitor={fullname_of_class(visitor.__class__)!r})"
        )
        self.ctx = ctx


def fullname_of_class(cls):
    return f"{cls.__module__}.{cls.__name__}"


def resolve_visitor(name, *, cls, logger):
    logger.debug("resolve %r visitor: %s", name, cls.__name__)
    return cls()


def resolve_node(name, *, logger, here=None):
    here = here or sys._getframe(1).f_globals["__name__"]
    try:
        logger.debug("resolve node: %s", name)
        module_path, symbol = name.rsplit(".", 1)
        module = import_module(module_path, here)
        cls = getattr(module, symbol)
        return cls()
    except (ImportError, AttributeError):
        logger.info("resolve node: %s is not found", name)
        return None


class Case:
    def __init__(self, doc: dict):
        self.doc = doc  # {"definitions": {...}}
        self._validators = {}

    def get_validator(self, ref):
        from jsonschema import Draft4Validator

        validator = self._validators.get(ref)
        if validator is not None:
            return validator
        schema = access_by_json_pointer(self.doc, ref)
        Draft4Validator.check_schema(schema)
        self._validators[ref] = validator = Draft4Validator(schema)
        return validator

    def when(self, d, ref) -> bool:
        validator = self.get_validator(ref)
        # errors = list(validator.iter_errors(d))
        # if not errors:
        #     return True
        # import json
        # print("@", json.dumps(d), errors)
        # return False
        return validator.is_valid(d)
