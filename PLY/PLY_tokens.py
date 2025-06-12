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
