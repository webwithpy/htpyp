from pyht.lexer import Lexer
from pyht.parser import DefaultParser
from pyht.renderer import DefaultRenderer

lexer = Lexer()
tokens = lexer.lex_file('test/test.html')
parser = DefaultParser(tokens)
program = parser.parse()
renderer = DefaultRenderer()
print(renderer.render(program))