import typing as t
import sys
import inspect
import linecache
from dictknife.langhelpers import reify
from dictknife.jsonknife import path_to_json_pointer
from openapi_stream import Context
from openapi_stream.interfaces import Visitor


class Description:
    def __init__(
        self, msg: str, *, ctx: Context, visitor: Visitor, depth: int = 3
    ) -> None:
        self.msg = msg
        self.ctx = ctx
        self.visitor = visitor
        self.depth = depth  # [Description.__init__, Exception.__init__, current]

    @reify
    def oneline_description(self) -> str:
        return f"{self.msg} (where: {self.position_ref!r})"

    @reify
    def position_ref(self) -> str:
        return path_to_json_pointer(self.ctx.path)

    @reify
    def schema(self) -> str:
        pass

    @reify
    def visit_function_history(self) -> t.List[str]:
        return [f"{fn.__qualname__}\n" for fn in self.ctx.fn_history]

    @reify
    def visitor_source_file(self) -> str:
        fname = inspect.getfile(self.visitor.__class__)
        import os

        cwd = os.getcwd()
        if fname.startswith(cwd):
            return fname[len(cwd) + 1:]
        return fname

    @reify
    def visitor_code_lines(self) -> t.List[str]:
        visitor = self.visitor
        sourcefile = self.visitor_source_file

        lines, lnum = inspect.getsourcelines(visitor.__class__)

        prefix = "   "
        higher_scope_lines = []

        if not lines[0].startswith("class "):
            i = 1
            while True:
                lino = lnum - i
                if lino <= 0:
                    break
                line = linecache.getline(sourcefile, lino)
                if line.startswith("class "):
                    higher_scope_lines.append(f"{prefix}...\n")
                    higher_scope_lines.append(f"{prefix}{lino:04d}: {line}")
                    break
                if line.lstrip().startswith("class "):
                    higher_scope_lines.append(f"{prefix}...\n")
                    higher_scope_lines.append(f"{prefix}{lino:04d}: {line}")
                i += 1

        n = 2
        current_scope_lines = []

        for i in range(n):
            lino = lnum + i
            current_scope_lines.append(
                f"{prefix}{lino:04d}: {linecache.getline(sourcefile, lino)}"
            )

        seen = set()
        if visitor == self.ctx.fn_history[-1].__self__:
            current_scope_lines.append(f"{prefix}...\n")
            lines, lnum = inspect.getsourcelines(self.ctx.fn_history[-1])
            for i in range(n):
                lino = lnum + i
                seen.add(lino)
                current_scope_lines.append(
                    f"{prefix}{lino:04d}: {linecache.getline(sourcefile, lino)}"
                )

        frame = sys._getframe(self.depth)  # xxx:
        n = 2
        this_lines = []
        if frame.f_lineno > lino:
            this_lines.append(f"{prefix}...\n")

        for lino in range(max(1, frame.f_lineno - n), frame.f_lineno + n):
            if lino in seen:
                continue
            prefix = "   "
            if lino == frame.f_lineno:
                prefix = "-> "
            this_lines.append(
                f"{prefix}{lino:04d}: {linecache.getline(sourcefile, lino)}"
            )
        return [*reversed(higher_scope_lines), *current_scope_lines, *this_lines]
