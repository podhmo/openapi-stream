from openapi_stream import main
from openapi_stream.jsonschema import ToplevelVisitor

# python -m openapi_stream.jsonschema

if __name__ == "__main__":
    for ev in main(create_visitor=ToplevelVisitor):
        if "primitive" in ev.roles:
            continue
        print(ev)
