import typing as t
import inspect
import linecache
from dictknife.langhelpers import reify
from dictknife.jsonknife import path_to_json_pointer
from openapi_stream import Context
from openapi_stream.interfaces import Visitor


class Description:
    def __init__(self, msg: str, *, ctx: Context, visitor: Visitor) -> None:
        self.msg = msg
        self.ctx = ctx
        self.visitor = visitor

    @reify
    def oneline_message(self) -> str:
        ref = path_to_json_pointer(self.ctx.path)
        cls = self.visitor.__class__
        return f"{self.msg} (where ref={ref!r}, visitor={fullname_of_class(cls)!r})"

    @reify
    def schema(self) -> str:
        pass

    @reify
    def walked_visitor_history(self) -> t.List[str]:
        # todo: implementation
        return []

    @reify
    def visitor_source_file(self) -> str:
        return inspect.getfile(self.visitor.__class__)

    @reify
    def visitor_code_lines(self) -> t.List[str]:
        visitor = self.visitor
        lines, lnum = inspect.getsourcelines(visitor.__class__)

        prefix_lines = []
        show_lines = []

        sourcefile = self.visitor_source_file
        if not lines[0].startswith("class "):
            i = 1
            while True:
                lino = lnum - i
                if lino <= 0:
                    break
                line = linecache.getline(sourcefile, lino)
                if line.startswith("class "):
                    prefix_lines.append("...\n")
                    prefix_lines.append(f"{lino:04d}: {line}")
                    break
                if line.lstrip().startswith("class "):
                    prefix_lines.append("...\n")
                    prefix_lines.append(f"{lino:04d}: {line}")
                i += 1
        n = 5
        # for i in range(max(1, lnum - n), lnum + n):
        for lino in range(lnum, lnum + n):
            show_lines.append(f"{lino:04d}: {linecache.getline(sourcefile, lino)}")

        return [
            *["  " + x for x in reversed(prefix_lines)],
            *["  " + x for x in show_lines],
        ]


# xxx:
def fullname_of_class(cls) -> str:
    return f"{cls.__module__}.{cls.__name__}"
