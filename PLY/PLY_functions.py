from PLY_tokens import *

def t_FLOATNUM(t):
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

def t_CHARACTER(t):
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
# Modified by Levin Moran
def t_error(t):
    message = ("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return message
