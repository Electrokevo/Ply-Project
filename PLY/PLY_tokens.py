#Valor en mayúscula porque se usará en el retorno del token

#Start_Levin Moran
reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'for' : 'FOR',
   "return" : "RETURN",
   "do" : "DO",
   "void" : "VOID",
   "class" : "CLASS",
   "new" : "NEW",
   "using" : "USING",
   "var" : "VAR",
   "true" : "TRUE",
   "false" : "FALSE",
   "static" : "STATIC",
   "in" : "IN",
   "list" : "LIST",
   "namespace" : "NAMESPACE",
   
   #Modificadores de acceso
   "public" : "PUBLIC",
   "private" : "PRIVATE",
   "protected" : "PROTECTED",
   "internal" : "INTERNAL",
   "file" : "FILE",
   
   #Datos primitivos
   "bool": "BOOL",
   "byte": "BYTE",
   "sbyte": "SBYTE",
   "char": "CHAR",
   "decimal": "DECIMAL",
   "double": "DOUBLE",
   "float": "FLOAT",
   "int": "INT",
   "uint": "UINT",
   "nint": "NINT",
   "nuint": "NUINT",
   "long": "LONG",
   "ulong": "ULONG",
   "short": "SHORT",
   "ushort": "USHORT"

}

# List of token names.   This is always required
tokens = (
    "FLOAT_TYPE",
    "DOUBLE_TYPE",
    "DECIMAL_TYPE",
    'INTEGER_TYPE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULE',
    'EQUALITY',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'SEMICOLON',
    "LBRACKET",
    "RBRACKET",
    "ID",
    "STRING",
    "CHARACTER",
    "LSQBRACKET",
    "RSQBRACKET",
    "COMMA",
    "CLASSOBJECT",
    "DOT",
    "OR",
    "AND",
    "NOT",
    "GREATER_THAN",
    "LESS_THAN",
    "GREATER_EQUALS_THAN",
    "LESS_EQUALS_THAN",
    "PLUS_EQUAL",
    "MINUS_EQUAL",
    "TIMES_EQUAL",
    "DIVIDE_EQUAL",
    "MODULE_EQUAL",
    "ARROW",
) + tuple(reserved.values())

# Ignorar comentarios de línea
t_ignore_COMMENTLINE = r'//.*'

# Ignorar comentarios de bloque
def t_COMMENTBLOCK(t):
    r'/\*[\s\S]*?\*/'
    pass

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_MODULE = r'%'
t_EQUALITY = r'=='
t_EQUALS = r'='
t_SEMICOLON = r';'
t_LBRACKET = r"{"
t_RBRACKET = r"}"
t_COMMA = r","
t_LSQBRACKET = r"\["
t_RSQBRACKET = r"\]"
t_CLASSOBJECT = r"[A-Z][a-zA-Z_]*"
t_DOT = r"\."
#Start_Kevin Mejia
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_GREATER_EQUALS_THAN = r'>='
t_LESS_EQUALS_THAN = r'<='
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'-='
t_TIMES_EQUAL = r'\*='
t_DIVIDE_EQUAL = r'/='
t_MODULE_EQUAL = r'%='
t_ARROW = r'=>'
#End_Kevin Mejia


#End_Levin Moran