from pyht.lexer import Lexer
from pyht.parser import DefaultParser

lexer = Lexer()
tokens = lexer.lex_file('test/test.html')
print(tokens)
parser = DefaultParser(tokens)
print(parser.parse())