import ply.lex as lex


#Valor en mayúscula porque se usará en el retorno del token
reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'for' : 'FOR',
   "return" : "RETURN"

}

# List of token names.   This is always required
tokens = (
    "FLOAT",
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULE',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'SEMICOLON',
    "LBRACKET",
    "RBRACKET",
    "ID",
    "STRING",
    "CHAR",
    "LSQBRACKET",
    "RSQBRACKET",
    "COMMA"

) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_MODULE = r'%'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_LBRACKET = r"{"
t_RBRACKET = r"}"
t_COMMA = r","
t_LSQBRACKET = r"\["
t_RSQBRACKET = r"\]"

def t_FLOAT(t):
    r'\d+\.\d*'
    t.value = float(t.value)    
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_STRING(t):
    r'".*"'
    t.value = str(t.value)    
    return t

def t_CHAR(t):
    r'\'.\''
    t.value = str(t.value)    
    return t



def t_ID(t):
    r'[a-z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

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


    