import operator
import ply.lex as lex
import ply.yacc as yacc
from PLY_tokens import *
from PLY_functions import *

#Start_Levin Moran
from subprocess import getoutput
from datetime import datetime

usuarioGit = getoutput("git config user.name")
fechaHora = datetime.now().strftime("%Y_%m_%d-%H_%M_%S") # Formato: 2025_06_13-12_00_00

nombreArchivoLexic = f"lexic-{usuarioGit}-{fechaHora}.txt"
rutaArchivoLexic = f"../Logs/{nombreArchivoLexic}"

nombreArchivo = f"sintactico-{usuarioGit}-{fechaHora}.txt"
rutaArchivo = f"../Logs/{nombreArchivo}"

nombreArchivoSemantico = f"semantico-{usuarioGit}-{fechaHora}.txt"
rutaArchivoSemantico = f"../Logs/{nombreArchivoSemantico}"

arch = open(rutaArchivo, "w", encoding="UTF-8")
archSemantico = open(rutaArchivoSemantico, "w", encoding="UTF-8")

def write_lexic_logs(code):
    lexer.input(code)

    # Tokenize
    # Modified by Levin Moran
    archivo = open(rutaArchivoLexic, "w", encoding="UTF-8") 
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        archivo.write(f"{tok}\n")
    archivo.close()

def write_sintactic_logs(code):
    global arch
    arch = open(rutaArchivo, "w", encoding="UTF-8")
    parser.parse(code)
    arch.close()

def write_semantic_logs(code):
    global archSemantico
    archSemantico = open(rutaArchivoSemantico, "w", encoding="UTF-8")
    global arch
    arch = open(rutaArchivo, "w", encoding="UTF-8")
    parser.parse(code)
    for var, tipo in tabla_simbolos["variables"].items():
        archSemantico.write(f"{var}, {tipo}  \n")
    archSemantico.close()
    arch.close()



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
    

def p_names(p):
    '''names : ID
    | CLASSOBJECT'''
    p[0] = p[1]

def p_funtion(p: yacc.YaccProduction):
    '''function : modifier data_type names LPAREN declarations RPAREN block
                | modifier VOID names LPAREN declarations RPAREN block
                | modifier STATIC data_type names LPAREN declarations RPAREN block
                | modifier STATIC VOID names LPAREN declarations RPAREN block
                | function body'''
    
    # Levin Moran
    if len(p) == 8:
        nombre = p[3]
        tipo_retorno = p[2]
        if nombre not in tabla_simbolos["variables"]:
            tabla_simbolos["variables"][nombre] = tipo_retorno
            p[0] = tipo_retorno
        else:   
            archSemantico.write(f"Error semántico: La función '{nombre}' ya está declarada \n")
    elif len(p) == 9:
        nombre = p[4]
        tipo_retorno = p[3]
        if nombre not in tabla_simbolos["variables"]:
            tabla_simbolos["variables"][nombre] = tipo_retorno
            p[0] = tipo_retorno
        else:   
            archSemantico.write(f"Error semántico: La función '{nombre}' ya está declarada \n")
    else:
        p[0] = p[1]

def p_return(p):
    '''return : RETURN ID
               | RETURN type
               | RETURN expression'''

def p_function_call(p):
    '''function_call : names LPAREN RPAREN
                     | names LPAREN arguments RPAREN'''
    
def p_arguments(p):
    '''arguments : expression
                 | expression COMMA arguments
                 | names
                 | names COMMA arguments'''

    # Levin Moran
    name = [p[1]]
    if len(p) == 2:
        p[0] = name
    else:
        dato = p[3]
        p[0] = name + dato
        

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
    if p[3] == "bool":
        p[0] = p[3]
    else:
        archSemantico.write(f"Semantic error: The expression between parenthesis doesn't result in a boolean \n")


def p_elseif(p):
    '''elseif : ELSE IF LPAREN logical_expression RPAREN block
    | ELSE IF LPAREN logical_expression RPAREN block elseif
    | ELSE IF LPAREN logical_expression RPAREN block else'''
    if p[4] == "bool":
        p[0] = p[3]
    else:
        archSemantico.write(f"Semantic error: The expression between parenthesis doesn't result in a boolean \n")

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
    | loop_for body'''

    # Levin Moran
    if len(p) == 3:
        p[0] = p[1]
    else:
        if p[5] != "bool":
            archSemantico.write(f"Error semántico: La expresión en paréntesis retorna {p[5]}\n")

#End_Levin Moran

# Start Kevin Mejia
def p_while_loop(p: yacc.Production):
    '''while_loop : WHILE LPAREN logical_expression RPAREN block
    | WHILE LPAREN logical_expression RPAREN block body'''
    #start kevin mejia
    if p[3] == "bool":
        p[0] = p[3]
    else:
        archSemantico.write(f"Error semántico: La expresión en paréntesis retorna {p[3]}")
    #end kevin mejia

def p_logical_expression(p):
    '''logical_expression : logical_factor logical_operator logical_expression
    | logical_expression logical_operator logical_expression
    | logical_factor'''
    #start kevin mejia
    if len(p) == 2:
        p[0] = p[1]
    else:
        operator = p[2]
        if operator == "||" or operator == "&&":
            type1 = p[1]
            type2 = p[3]
            if type1 != "bool":
                archSemantico.write(f"Semantic error: Type {type1} is not allow with operator {operator}\n")
            elif type2 != "bool":
                archSemantico.write(f"Semantic error: Type {type2} is not allow with operator {operator}\n")
            else:
                p[0] = "bool"
        elif operator == ">" or operator == ">=" or operator == "<" or operator == "<=":
            allowed_types = ["int", "float", "double", "decimal", "short", "long", "byte"]
            type1 = p[1]
            type2 = p[3]
            if type1 not in allowed_types:
                archSemantico.write(f"Semantic error: Type {type1} is not allow with operator {operator}\n")
            elif type2 not in allowed_types:
                archSemantico.write(f"Semantic error: Type {type2} is not allow with operator {operator}\n")
            else:
                p[0] = "bool"
        elif operator == "==" or operator == "!=":
            allowed_types = ["int", "float", "double", "decimal", "short", "long", "byte"]
            type1 = p[1]
            type2 = p[3]
            if type1 in allowed_types and type2 in allowed_types:
                p[0] = "bool"
            elif type1 == "string" and type2 == "string":
                p[0] = "bool"
            elif type1 == "bool" and type2 == "bool":
                p[0] = "bool"
            else:
                archSemantico.write(f"Semantic error: Type {type1} and type {type2} cannot use operator {operator}\n")
        else:
            archSemantico.write(f"Semantic error: Operator {operator} isn't recognize\n")
    #end kevin mejia

def p_logical_factor(p):
    '''logical_factor : TRUE
    | FALSE
    | ID
    | indexing
    | type
    | object_access
    | LPAREN logical_expression RPAREN'''
    #start kevin mejia
    if len(p) == 4:
        p[0] = p[2]
    else:
        type = p[1]
        if type in tabla_simbolos["variables"]:
            p[0] = tabla_simbolos["variables"][p[1]]
        elif isinstance(type, bool) or type == "bool":
            p[0] = "bool"
        elif isinstance(type, int) or type == "int":
            p[0] = "int"
        elif isinstance(type, float) or type == "float":
            p[0] = "float"
        elif isinstance(type, str) or type == "string":
            p[0] = "string"
        else:
            archSemantico.write(f"Semantic error: type {type} not recognized \n")
    #end kevin mejia

def p_logical_operator(p):
    '''logical_operator : OR
    | AND
    | NOT
    | GREATER_THAN
    | LESS_THAN
    | GREATER_EQUALS_THAN
    | LESS_EQUALS_THAN
    | EQUALITY
    | DIFFERENT'''
    p[0] = p[1]
# End Kevin Mejia

#Start_Levin Moran
def p_data_structure(p):
    '''data_structure : data_structure_list
                      | data_structure_array'''
    p[0] = p[1]

def p_data_structure_list(p):   
    '''data_structure_list : LIST LESS_THAN data_type GREATER_THAN'''
    
    #Levin Moran
    p[0] = p[3]
#End_Levin Moran

# Start Kevin Mejia
def p_data_structure_array(p):
    '''data_structure_array : primitive LSQBRACKET RSQBRACKET
    | CLASSOBJECT LSQBRACKET RSQBRACKET'''
    p[0] = p[1]

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
    '''assignment : ID EQUALS expression
                | indexing EQUALS expression'''

    # Levin Moran
    nombre = p[1]
    data = p[3]

    if nombre not in tabla_simbolos["variables"]:
        archSemantico.write(f"Error semántico: Variable '{nombre}' no declarada \n")
    else:
        tipado = tabla_simbolos["variables"][nombre]
        if tipado == data:
            tabla_simbolos["variables"][nombre] = data
        else:
            archSemantico.write(f"Error de tipo: variable '{nombre}' declarada como '{tipado}' pero se asigna un valor de tipo '{data}'\n")


def p_assignment_plus_one(p):
    '''assignment : ID PLUSONE'''
    
    # Levin Moran
    nombre = p[1]

    if nombre not in tabla_simbolos["variables"]:
        archSemantico.write(f"Error semántico: Variable '{nombre}' no declarada \n")
    else:
        tipado = tabla_simbolos["variables"][nombre]
        numbers = ["int", "float", "double", "decimal"]
        if tipado in numbers:
            tabla_simbolos["variables"][nombre] = tipado
        else:
            archSemantico.write(f"Error de tipo: variable '{nombre}' de tipo '{tipado}' no puede ser incrementada \n")

def p_assignment_class(p):
    '''assignment : CLASSOBJECT ID'''
    
    
    # Levin Moran
    nombre = p[2]
    clase = p[1]

    if nombre not in tabla_simbolos["variables"]:
        tabla_simbolos["variables"][nombre] = clase
    else:
        archSemantico.write(f"Error semántico: La clase '{nombre}' ya está declarada \n")

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
    | LSQBRACKET arguments RSQBRACKET
    | object_access
    | ID
    | indexing
    | function_call
    | STRING'''
    
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
        data = p[2]
        if not isinstance(data, list):
            p[0] = p[2]
        else:
            type_list = data[0]
            if len(data) != 1:
                for item in data:
                    if item != type_list:
                        type_list = "Object"
            p[0] = type_list

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
        p[0] = [p[1]] + ["void"]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]

def p_declaration(p):
    '''declaration : data_type ID'''

    # Levin Moran
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
    p[0] = p[1]

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
    | ID LSQBRACKET ID RSQBRACKET
    | ID LSQBRACKET expression RSQBRACKET'''
    #start kevin mejia
    if isinstance(p[3], int):
        #Se devuelve p[0] porque nos interesa el tipo de dato de la lista, dado que p[3] ya sabemos que es int
         p[0] = tabla_simbolos["variables"][p[1]]
    elif p[3] in tabla_simbolos["variables"]:
        tipo = tabla_simbolos["variables"][p[3]]
        if tipo != "int":
            archSemantico.write(f"Semantic error: {p[3]} isn't an integer type.\n")
        else:
            #Lo mismo de arriba pero ahora con variable
            p[0] = tabla_simbolos["variables"][p[1]]
    else:
         archSemantico.write(f"Semantic error: {p[3]} isn't an integer type.\n")
    #end kevin mejia
# End Kevin Mejia


#Start_Levin Moran

# Error rule for syntax errors
def p_error(p):
    if p:
        arch.write(f"Syntax error at token {p.type}, value '{p.value}, at line {p.lineno}'\n")
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


arch.close()
archSemantico.close()

#End_Levin Moran