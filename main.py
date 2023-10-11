from pyht.lexer import Lexer
from pyht.parser import DefaultParser
from pyht.renderer import DefaultRenderer

lexer = Lexer()
tokens = lexer.lex_file('test/test.html')
parser = DefaultParser(tokens)
program = parser.parse()
renderer = DefaultRenderer()
# use spacing in this one
code = renderer.generate_pre_code(program)
print(renderer.render_pre(code, test=3))