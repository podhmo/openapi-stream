from openapi_stream import main
from visitors import Toplevel

if __name__ == "__main__":
    for ev in main(create_visitor=Toplevel):
        if "primitive" in ev.roles:
            continue
        print(ev)
