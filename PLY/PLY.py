import ply.lex as lex
from PLY_tokens import *
from PLY_functions import *

#Start_Levin Moran
from subprocess import getoutput
from datetime import datetime

usuarioGit = getoutput("git config user.name")
fechaHora = datetime.now().strftime("%Y_%m_%d-%H_%M_%S") # Formato: 2025_06_13-12_00_00
nombreArchivo = f"lexic-{usuarioGit}-{fechaHora}.txt"
rutaArchivo = f"./Logs/{nombreArchivo}"
#End_Levin Moran

# Build the lexer
lexer = lex.lex()

'''#Lectura del archivo a tokenizar
#Start_Levin Moran
buffer = ''''''
archivo = open("./Algorithms/LexicTests/BinarySearch.cs", "r", encoding="UTF-8")
for line in archivo:
  if line.startswith("\ufeff"):
    line = line.strip("\ufeff")
  buffer += line
archivo.close()
#End_Levin Moran'''

def write_lexic_logs(code):
    lexer.input(code)

    # Tokenize
    # Modified by Levin Moran
    archivo = open(rutaArchivo, "w", encoding="UTF-8") 
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        archivo.write(f"{tok}\n")
    archivo.close()