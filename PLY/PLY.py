import ply.lex as lex
from PLY_tokens import *
from PLY_functions import *


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''"abcd"if{
a = 3 + 4 * 10 23.
  + -20 *2 % 5} 'a' [,];
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)


    