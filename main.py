from htpyp.lexer import Lexer
from htpyp.parser import DefaultParser
from htpyp.renderer import DefaultRenderer

lexer = Lexer()
tokens = lexer.lex_file('test/test.html')
parser = DefaultParser(tokens)
program = parser.parse()
renderer = DefaultRenderer()
# use spacing in this one
code = renderer.generate_pre_code(program)
print(renderer.render_pre(code, test=3))