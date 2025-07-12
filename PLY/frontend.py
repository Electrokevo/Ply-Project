import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog as fd

from PLY_yacc import *


def open_cs_file():
    # file type
    filetypes = (
        ('text files', '*.cs'),
    )
    f = fd.askopenfile(filetypes=filetypes)
    code_text.delete('1.0', tk.END)
    code_text.insert('1.0', f.read())


def validar_todo():
    validar_lexico()
    validar_sintaxis()
    validar_semantica()

#pasar codigo al ply y conectar la salida de los logs con 'console_text'
def validar_lexico():
    console_text.delete('1.0', tk.END)
    code = code_text.get('1.0', tk.END)
    write_lexic_logs(code)
    archivo = open(rutaArchivoLexic, "r", encoding="UTF-8") 
    logs = archivo.read()
    console_text.insert('1.0', logs)
    archivo.close()

def validar_sintaxis():
    console_text.delete('1.0', tk.END)
    code = code_text.get('1.0', tk.END)
    write_sintactic_logs(code)
    arch = open(rutaArchivo, "r", encoding="UTF-8")
    logs = arch.read()
    console_text.insert('1.0', logs)
    arch.close()

def validar_semantica():
    console_text.delete('1.0', tk.END)
    code = code_text.get('1.0', tk.END)
    write_semantic_logs(code)
    archSemantico = open(rutaArchivoSemantico, "r", encoding="UTF-8")
    logs = archSemantico.read()
    console_text.insert('1.0', logs)
    archSemantico.close()

    pass

# ---------- Setup ----------
root = tk.Tk()
root.title("C#")
root.geometry("1200x800")
root.configure(bg="#121212")

# ---------- Styles ----------
style = ttk.Style()
style.theme_use("clam")

style.configure("TFrame", background="#121212")
style.configure("Sidebar.TFrame", background="#1e1e1e")
style.configure("TLabel", background="#121212", foreground="#eeeeee", font=("Consolas", 12))
style.configure("Sidebar.TLabel", background="#1e1e1e", foreground="#eeeeee", font=("Consolas", 12))
style.configure("TButton", background="#1e1e1e", foreground="#eeeeee", font=("Consolas", 12), relief="flat")
style.map("TButton", background=[("active", "#333333")])

# ---------- Sidebar ----------
sidebar = ttk.Frame(root, style="Sidebar.TFrame", width=150)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Logo (placeholder image path)
logo_image = Image.open("../Ply-Project/PLY/assets/logo.ico")  # <-- Replace with real path
logo_image = logo_image.resize((80, 80))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = ttk.Label(sidebar, image=logo_photo, style="Sidebar.TLabel")
logo_label.image = logo_photo
logo_label.pack(pady=20)

# Sidebar buttons
btn = ttk.Button(sidebar, text="Todo", command=validar_todo, style="TButton")
btn.pack(fill=tk.X, padx=10, pady=5)

btn = ttk.Button(sidebar, text="Lexico", command=validar_lexico, style="TButton")
btn.pack(fill=tk.X, padx=10, pady=5)

btn = ttk.Button(sidebar, text="Sintaxis", command=validar_sintaxis, style="TButton")
btn.pack(fill=tk.X, padx=10, pady=5)

btn = ttk.Button(sidebar, text="Semantica", command=validar_semantica, style="TButton")
btn.pack(fill=tk.X, padx=10, pady=5)

btn = ttk.Button(sidebar, text="Subir archivo", command=open_cs_file, style="TButton")
btn.pack(fill=tk.X, padx=10, pady=5)

# ---------- Main Frame ----------
main_frame = ttk.Frame(root)
main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Title
title = ttk.Label(main_frame, text="C#", font=("Helvetica", 24))
title.pack(pady=10)

# Code Editor
code_frame = ttk.Frame(main_frame)
code_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

code_text = tk.Text(code_frame, wrap="none", bg="#1e1e1e", fg="#eeeeee", insertbackground="#eeeeee", font=("Consolas", 12))
code_text.pack(fill=tk.BOTH, expand=True)

#TODO: LEER ARCHIVO CS Y REEMPLAZAR TEXTO CON EL DEL ARCHIVO
code = '''using System;
Console.WriteLine("Hello World");
int i = 2 + 2;
if (i >= 20 || i < 5)
{
    var arr = new int[5];
    arr[0] = "c";
}
else
{
    string jeje = "";
}
'''
code_text.insert("1.0", code)

# ---------- Console ----------
console_frame = ttk.Frame(main_frame)
console_frame.pack(fill=tk.X, padx=20, pady=10)

console_label = ttk.Label(console_frame, text="Consola", font=("Helvetica", 14))
console_label.pack(anchor="w")

#TODO: CONECTAR LOGS CON LA CONSOLA
console_text = tk.Text(console_frame, height=4, bg="#1a1a1a", fg="#eeeeee", insertbackground="#eeeeee", font=("Consolas", 10))
console_text.pack(fill=tk.X)
console_text.insert("1.0", ">error ")

root.mainloop()
