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
    "FLOATNUM",
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
    "CHARACTER",
    "LSQBRACKET",
    "RSQBRACKET",
    "COMMA",
    "CLASSOBJECT",
    "DOT"

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
t_CLASSOBJECT = r"[A-Z][a-zA-Z_]*"
t_DOT = r"\."


#End_Levin Moran