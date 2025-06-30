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
rutaArchivo = f"./Logs/{nombreArchivo}"

nombreArchivoSemantico = f"semantico-{usuarioGit}-{fechaHora}.txt"
rutaArchivoSemantico = f"./Logs/{nombreArchivoSemantico}"

arch = open(rutaArchivo, "w", encoding="UTF-8")
archSemantico = open(rutaArchivoSemantico, "w", encoding="UTF-8")
#End_Levin Moran

#reglas en minúscula y tokens en mayúscula

# TODO: Ver que hacer aca

# def p_test(p):
#     '''test : body'''
#     p[0] = p[1]

# Start Kevin Mejia

#Tabla de simbolos
tabla_simbolos = {
    "variables" : {},
    "tipos": {
        "string-func": ["ToUpper", "ToLower"],
        "array-func": ["Length"]
    }
}

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

    # Levin Moran
    nombre = p[1]
    metodo = p[3]

    if nombre not in tabla_simbolos["variables"]:
        archSemantico.write(f"Error semántico: El objeto '{nombre}' no está declarado \n")
    elif metodo in tabla_simbolos["tipos"]["string-func"]:
        p[0] = "str"
    elif metodo in tabla_simbolos["tipos"]["array-func"]:
        p[0] = "int"
    elif metodo in tabla_simbolos["variables"]:
        p[0] = tabla_simbolos["variables"][metodo]
    elif metodo not in tabla_simbolos["variables"]:
        archSemantico.write(f"Error semántico: El método '{metodo}' no está declarado \n")
    else:
        archSemantico.write(f"Error semántico: El método '{metodo}' no es parte de las funciones permitidas \n")


    
        
def p_block(p):
    '''block : LBRACKET body RBRACKET'''
    p[0] = p[1]

# Modified by Levin Moran
def p_body(p):
    '''body : lines SEMICOLON
            | lines SEMICOLON body
            | if
            | loop
            | function'''
    p[0] = p[1]

def p_lines(p):
    '''lines : assignment 
    | expression 
    | declaration
    | return'''
    p[0] = p[1]

def p_funtion(p: yacc.YaccProduction):
    '''function : modifier data_type ID LPAREN declarations RPAREN block
                | modifier VOID ID LPAREN declarations RPAREN block
                | modifier STATIC data_type ID LPAREN declarations RPAREN block
                | modifier STATIC VOID ID LPAREN declarations RPAREN block'''
    
    # Levin Moran
    if len(p) == 8:
        nombre = p[3]
        tipo_retorno = p[2]
        if nombre not in tabla_simbolos["variables"]:
            tabla_simbolos["variables"][nombre] = tipo_retorno
            p[0] = tipo_retorno
        else:   
            archSemantico.write(f"Error semántico: La función '{nombre}' ya está declarada \n")
    else:
        nombre = p[4]
        tipo_retorno = p[3]
        if nombre not in tabla_simbolos["variables"]:
            tabla_simbolos["variables"][nombre] = tipo_retorno
            p[0] = tipo_retorno
        else:   
            archSemantico.write(f"Error semántico: La función '{nombre}' ya está declarada \n")


def p_return(p):
    '''return : RETURN ID
               | RETURN type'''
# End Kevin Mejia
#Start_Levin Moran
def p_lambda_function(p):
    '''lambda_function : LPAREN ID RPAREN ARROW expression
                       | LPAREN ID RPAREN ARROW block'''
    
def p_console_writeline(p):
    '''expression : object_access LPAREN expression RPAREN'''
    if len(p) == 8:
        p[0] = f"{p[1]}.{p[3]}({p[5]})"
    else:
        p[0] = f"{p[1]}.{p[3]}()"

def p_console_readline(p):
    '''expression : object_access LPAREN RPAREN'''
    p[0] = f"{p[1]}.{p[3]}()"

#END_Levin Moran

# Start Kevin Mejia   

# Modified by Levin Moran
def p_if(p):
    '''if : IF LPAREN logical_expression RPAREN block
    | IF LPAREN logical_expression RPAREN block body
    | IF LPAREN logical_expression RPAREN block elseif
    | IF LPAREN logical_expression RPAREN block else'''

def p_elseif(p):
    '''elseif : ELSE IF LPAREN logical_expression RPAREN block
    | ELSE IF LPAREN logical_expression RPAREN block elseif
    | ELSE IF LPAREN logical_expression RPAREN block else'''

# Modified by Levin Moran
def p_else(p):
    '''else : ELSE block
    | ELSE block body'''

# Modified by Levin Moran
def p_loop(p):
    '''loop : while_loop
            | loop_for'''

# End Kevin Mejia
#Start_Levin Moran
def p_loop_for(p):
    '''loop_for : FOR LPAREN assignment SEMICOLON logical_expression SEMICOLON assignment RPAREN block
    | FOR LPAREN assignment SEMICOLON logical_expression SEMICOLON assignment RPAREN block body'''
#End_Levin Moran

# Start Kevin Mejia
def p_while_loop(p):
    '''while_loop : WHILE LPAREN logical_expression RPAREN block
    | WHILE LPAREN logical_expression RPAREN block body'''

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
# End Kevin Mejia

#Start_Levin Moran
def p_data_structure(p):
    '''data_structure : data_structure_list
                      | data_structure_array'''

def p_data_structure_list(p):   
    '''data_structure_list : LIST LESS_THAN data_type GREATER_THAN ID LSQBRACKET type RSQBRACKET'''
#End_Levin Moran

# Start Kevin Mejia
def p_data_structure_array(p):
    '''data_structure_array : primitive LSQBRACKET RSQBRACKET
    | CLASSOBJECT LSQBRACKET RSQBRACKET'''

def p_assignment(p):
    '''assignment : data_type ID EQUALS expression'''
    
    #Levin Moran
    nombre = p[2]
    tipado = p[1]
    data = p[4]

    if tipado == data:
        tabla_simbolos["variables"][nombre] = data
    else:
        archSemantico.write(f"Error de tipo: variable '{nombre}' declarada como '{tipado}' pero se asigna un valor de tipo '{data}'\n")

def p_assignment_untyped(p):
    '''assignment : ID EQUALS expression'''

def p_assignment_class(p):
    '''assignment_class : CLASSOBJECT ID'''

def p_expression(p):
    '''expression : expression PLUS term
    | expression MINUS term
    | term'''


    # Levin Moran
    numbers = ["int", "float", "double", "decimal"]
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[1] in numbers and p[3] in numbers:
            if p[1] == p[3]:
                p[0] = p[3]
        else:
            archSemantico.write(f"Error de tipo: operación entre '{p[1]}' y '{p[3]}' no permitida \n")


def p_term(p):
    '''term : term TIMES factor
    | term DIVIDE factor
    | factor'''

    # Levin Moran
    numbers = ["int", "float", "double", "decimal"]
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[1] in numbers and p[3] in numbers:
            if p[1] == p[3]:
                p[0] = p[3]
        else:
            archSemantico.write(f"Error de tipo: operación entre '{p[1]}' y '{p[3]}' no permitida \n")
    

def p_factor(p):
    '''factor : type
    | LPAREN expression RPAREN
    | object_access
    | ID
    | indexing'''
    
    # Levin Moran
    if len(p) == 2:
        if p.slice[1].type == "ID":
            if p[1] in tabla_simbolos["variables"]:
                p[0] = tabla_simbolos["variables"][p[1]]
            else:
                archSemantico.write(f"Error semántico: Variable '{p[1]}' no declarada \n")
        else:
            p[0] = p[1]
    else:
        p[0] = p[2]

# Start Kevin Mejia   
# Modified by Levin Moran
def p_type(p):
    '''type : FLOAT_TYPE
    | DOUBLE_TYPE
    | DECIMAL_TYPE
    | INTEGER_TYPE
    | MINUS type'''

    # Levin Moran
    
    if isinstance(p[1], int):
        p[0] = "int"
    elif isinstance(p[1], float) and p.slice[1].type == "DOUBLE_TYPE":
        p[0] = "double"
    elif isinstance(p[1], float) and p.slice[1].type == "DECIMAL_TYPE":
        p[0] = "decimal"
    elif isinstance(p[1], float):
        p[0] = "float"
    elif p.slice[1].type == "MINUS":
        p[0] = p[2]
        
# End Kevin Mejia

def p_declarations(p):
    '''declarations : declaration
    | declaration COMMA
    | declaration COMMA declarations'''

    # Levin Moran
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        p[0] = [p[1]] + "void"
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]

def p_declaration(p):
    '''declaration : data_type ID'''

    nombre = p[2]
    tipado = p[1]

    if nombre not in tabla_simbolos["variables"]:
        tabla_simbolos["variables"][nombre] = tipado
        p[0] = tipado
    else:
        archSemantico.write(f"Error semántico: La variable '{nombre}' ya está declarada \n")

def p_modifier(p):
    '''modifier : PUBLIC 
    | PRIVATE 
    | PROTECTED 
    | INTERNAL'''

def p_data_type(p):
    ''' data_type : primitive
    | data_structure'''

    #Levin Moran
    p[0] = p[1]

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

    #Levin Moran
    p[0] = p[1]


def p_indexing(p):
    '''indexing : ID LSQBRACKET INTEGER_TYPE RSQBRACKET
    | ID LSQBRACKET ID RSQBRACKET'''
# End Kevin Mejia


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
archivo = open("./Algorithms/SyntaxTests/BinarySearch.cs", "r", encoding="UTF-8")
for line in archivo:
  if line.startswith("\ufeff"):
    line = line.strip("\ufeff")
  buffer += line
archivo.close()


asignaciones = parser.parse(buffer)

'''for asignacion in asignaciones:
    arch.write(f"Asignación correcta: {asignacion} \n")'''

for var, tipo in tabla_simbolos["variables"].items():
    archSemantico.write(f"{var}, {tipo}  \n")

arch.close()
archSemantico.close()

#End_Levin Moran