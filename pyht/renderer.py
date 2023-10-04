from .data.ast import Stmt, Include, Extends, Python, Html
from .lexer import Lexer
from .parser import DefaultParser
from typing import List


class DefaultRenderer:
    @classmethod
    def _render_code(cls, program: List[Stmt]) -> List[str]:
        # amount of times spacing needs to be added
        cls.code = ''
        cls.spacing = ''
        for index, stmt in enumerate(program):
            match stmt.kind:
                case "extends":
                    stmt: Extends
                    rendered = cls.__render_at_file_path(render_name='extends', file_path=stmt.file_path)
                    program += rendered
                case "include":
                    stmt: Include
                    rendered = cls.__render_at_file_path(render_name="include", file_path=stmt.file_path)
                    cls.code += rendered
                case "python":
                    stmt: Python
                    cls.code += f'{cls.spacing}{stmt.code}\n'
                    if ':' in stmt.code:
                        cls.spacing += '    '
                case "html":
                    stmt: Html
                    stmt.code = stmt.code.replace('"', "'")
                    cls.code += f'{cls.spacing}html += "{stmt.code}"\n'
                case "pass":
                    cls.spacing = cls.spacing[:-4]
                

        # PARSE CODE HERE

        return cls.code
    
    @classmethod
    def render(cls, program: List[Stmt], **vars):
        code = cls._render_code(program=program)
        vars['html'] = ''
        exec(code, {}, vars)

        return vars['html']

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
        rendered = DefaultRenderer._render_code(program)

        return rendered
