from .data.ast import Stmt
from typing import List
from .lexer import Lexer
from .parser import DefaultParser
from .data.ast import Include, Extends


class DefaultRenderer:
    @classmethod
    def render(cls, program: List[Stmt]) -> List[str]:
        # amount of times spacing needs to be added
        spacing: int = 0
        program: List[List[str]] = []
        code: List[str] = []
        for index, stmt in enumerate(program):
            if stmt.kind == "extends":
                stmt: Extends
                # still need 2 find where 2 throw code in extend
                rendered = cls.__render_at_fpath(f_path=stmt.f_path)
                code += rendered
            elif stmt.kind == "include":
                stmt: Include

        if len(code) > 0:
            program.append(code)

        return code

    @classmethod
    def __render_at_fpath(cls, f_path) -> List[str]:
        """
        :param f_path: file path
        :return:
        """
        lexer = Lexer()
        tokens = lexer.lex_file(f_path)
        parser = DefaultParser(tokens)
        program = parser.parse()
        rendered = DefaultRenderer.render(program)

        return rendered
