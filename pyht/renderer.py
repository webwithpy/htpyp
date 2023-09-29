from .data.render_block import RenderBlock
from .data.ast import Stmt, Include, Extends, Python, Html
from .lexer import Lexer
from .parser import DefaultParser
from typing import List


class DefaultRenderer:
    @classmethod
    def render(cls, program: List[Stmt]) -> List[str]:
        # amount of times spacing needs to be added
        program: List[RenderBlock] = []
        for index, stmt in enumerate(program):
            match stmt.kind:
                case "extends":
                    stmt: Extends
                    rendered = cls.__render_at_file_path(render_name='extends', file_path=stmt.file_path)
                    program += rendered
                case "include":
                    stmt: Include
                    rendered = cls.__render_at_file_path(render_name="include", file_path=stmt.file_path)
                    program += rendered
                case "python":
                    stmt: Python
                    pythonRender = RenderBlock(body=stmt.code)
                    program.append(pythonRender)
                case "html":
                    stmt: Html
                    htmlRender = RenderBlock(body=stmt.code)
                    program.append(htmlRender)
                case "pass":
                    passBlock = RenderBlock(block_type='pass')
                    program.append(passBlock)
                

        # PARSE CODE HERE

        return ""

    @classmethod
    def __build_code_from_program(cls, program):
        ...

    @classmethod
    def __render_at_file_path(cls, render_name: str, file_path: str) -> List[str]:
        """
        when a file is for example extended we will need to parse that one too.
        the rendered python will be placed where the extends happens
        :param render_name: name of the block
        :param file_path: path of the file
        :return:
        """
        lexer = Lexer()
        program = parser.parse()

        tokens = lexer.lex_file(file_path)
        parser = DefaultParser(tokens)
        rendered = DefaultRenderer.render(program)

        return RenderBlock(body=rendered, block_type=render_name)
