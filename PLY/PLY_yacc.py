import ply.lex as lex
import ply.yacc as yacc
from PLY_tokens import *
from PLY_functions import *

#Start_Levin Moran
from subprocess import getoutput
from datetime import datetime

usuarioGit = getoutput("git config user.name")
fechaHora = datetime.now().strftime("%Y_%m_%d-%H_%M_%S") # Formato: 2025_06_13-12_00_00
nombreArchivo = f"sintactico-{usuarioGit}-{fechaHora}.txt"
rutaArchivo = f"../Logs/{nombreArchivo}"
arch = open(rutaArchivo, "w", encoding="UTF-8")
#End_Levin Moran

#reglas en minúscula y tokens en mayúscula

# TODO: Ver que hacer aca

# def p_test(p):
#     '''test : body'''
#     p[0] = p[1]

def p_program(p):
    '''program : usings namespace class
    | namespace class'''
    p[0] = p[1]

def p_usings(p):
    '''usings : using usings
    | using'''
    p[0] = p[1]

def p_using(p):
    '''using : USING CLASSOBJECT SEMICOLON'''
    p[0] = p[1]

def p_namespace(p):
    '''namespace : NAMESPACE CLASSOBJECT SEMICOLON'''

def p_class(p):
    '''class : modifier CLASS CLASSOBJECT block
    | modifier STATIC CLASS CLASSOBJECT block'''
    p[0] = p[1]

def p_object_access(p):
    '''object_access : ID DOT ID
    | CLASSOBJECT DOT CLASSOBJECT
    | ID DOT CLASSOBJECT
    | CLASSOBJECT DOT ID'''

def p_block(p):
    '''block : LBRACKET body RBRACKET'''
    p[0] = p[1]

def p_body(p):
    '''body : lines SEMICOLON
            | lines SEMICOLON body
            | function'''
    p[0] = p[1]

def p_lines(p):
    '''lines : assignment 
    | expression 
    | declaration
    | if
    | loop
    | return'''
    p[0] = p[1]

def p_funtion(p: yacc.YaccProduction):
    '''function : modifier data_type ID LPAREN declarations RPAREN block
                | modifier VOID ID LPAREN declarations RPAREN block
                | modifier STATIC data_type ID LPAREN declarations RPAREN block
                | modifier STATIC VOID ID LPAREN declarations RPAREN block'''

def p_return(p):
    '''return : RETURN ID
               | RETURN type'''

def p_type(p):
    '''type : FLOAT_TYPE
    | DOUBLE_TYPE
    | DECIMAL_TYPE
    | INTEGER_TYPE'''

def p_if(p):
    '''if : IF LPAREN logical_expression RPAREN block
    | IF LPAREN logical_expression RPAREN block elseif
    | IF LPAREN logical_expression RPAREN block else'''

def p_elseif(p):
    '''elseif : ELSE IF LPAREN logical_expression RPAREN block
    | ELSE IF LPAREN logical_expression RPAREN block elseif
    | ELSE IF LPAREN logical_expression RPAREN block else'''

def p_else(p):
    '''else : ELSE block'''

def p_loop(p):
    '''loop : while_loop'''

def p_while_loop(p):
    '''while_loop : WHILE LPAREN logical_expression RPAREN block'''

def p_logical_expression(p):
    '''logical_expression : logical_expression logical_operator logical_factor
    | logical_factor'''

def p_logical_factor(p):
    '''logical_factor : TRUE
    | FALSE
    | ID
    | indexing
    | type
    | object_access
    | LPAREN logical_expression RPAREN'''

def p_logical_operator(p):
    '''logical_operator : OR
    | AND
    | NOT
    | GREATER_THAN
    | LESS_THAN
    | GREATER_EQUALS_THAN
    | LESS_EQUALS_THAN
    | EQUALITY'''


def p_assignment(p):
    '''assignment : ID EQUALS expression
                  | data_type ID EQUALS expression
                  | CLASSOBJECT ID'''

def p_declarations(p):
    '''declarations : declaration
    | declaration COMMA
    | declaration COMMA declarations'''

def p_declaration(p):
    '''declaration : data_type ID'''

def p_expression(p):
    '''expression : expression PLUS term
    | expression MINUS term
    | term'''

def p_term(p):
    '''term : term TIMES factor
    | term DIVIDE factor
    | factor'''
    # if (len(p) == 4):
    #     if (p[2] == '*'):
    #         p[0] = p[1] * p[3]
    #     elif (p[2] == '/'):
    #         p[0] = p[1] / p[3]
    # else:
    #     p[0] = p[1]

def p_factor(p):
    '''factor : type
    | LPAREN expression RPAREN
    | object_access
    | ID
    | indexing'''
    if (len(p) == 4):
        p[0] = [2]
    else :
        p[0] = [1]

def p_modifier(p):
    '''modifier : PUBLIC 
    | PRIVATE 
    | PROTECTED 
    | INTERNAL'''

def p_data_type(p):
    ''' data_type : primitive
    | data_structure'''

def p_primitive(p):
    '''primitive : INT 
    | FLOAT 
    | BOOL 
    | BYTE 
    | CHAR 
    | SBYTE 
    | DECIMAL 
    | DOUBLE 
    | LONG 
    | SHORT 
    | UINT'''

def p_data_structure(p):
    '''data_structure : array'''

def p_array(p):
    '''array : primitive LSQBRACKET RSQBRACKET
    | CLASSOBJECT LSQBRACKET RSQBRACKET'''

def p_indexing(p):
    '''indexing : ID LSQBRACKET INTEGER_TYPE RSQBRACKET
    | ID LSQBRACKET ID RSQBRACKET'''



#Start_Levin Moran

# Error rule for syntax errors
def p_error(p):
    if p:
        arch.write(f"Syntax error at token {p.type}, value '{p.value}'\n")
        parser.errok()
    else:
        arch.write("Syntax error at EOF")

# Build the lexer
lexer = lex.lex()

# # Build the parser
parser = yacc.yacc()


buffer = ''''''
archivo = open("../Algorithms/SyntaxTests/BinarySearch.cs", "r", encoding="UTF-8")
for line in archivo:
  if line.startswith("\ufeff"):
    line = line.strip("\ufeff")
  buffer += line
archivo.close()


asignaciones = parser.parse(buffer)
for asignacion in asignaciones:
    arch.write(f"Asignación correcta: {asignacion}\n")
arch.close()


#End_Levin Moran

# while True:
#    try:
#        s = input('csharp > ')
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(s)
#    print(result)