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
arch = open(rutaArchivo, "w", encoding="UTF-8")
#End_Levin Moran

#reglas en minúscula y tokens en mayúscula

def p_program(p):
    'program : assignments'
    p[0] = p[1]

def p_assignments_multiple(p):
    'assignments : assignments assignment'
    p[0] = p[1] + [p[2]]

def p_assignments_single(p):
    'assignments : assignment'
    p[0] = [p[1]]

def p_assignment(p):
    'assignment : ID EQUALS expression SEMICOLON'
    p[0] = f"{p[1]} = {p[3]};"

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    '''factor : INTEGER_TYPE
               | FLOAT_TYPE
               | DOUBLE_TYPE
               | DECIMAL_TYPE'''
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

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

# Build the parser
parser = yacc.yacc()


buffer = ''''''
archivo = open("./Algorithms/LexicTests/BinarySearch.cs", "r", encoding="UTF-8")
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