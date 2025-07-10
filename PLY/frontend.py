import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ---------- Setup ----------
root = tk.Tk()
root.title("C#")
root.geometry("1000x600")
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
logo_image = Image.open("assets/logo.ico")  # <-- Replace with real path
logo_image = logo_image.resize((80, 80))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = ttk.Label(sidebar, image=logo_photo, style="Sidebar.TLabel")
logo_label.image = logo_photo
logo_label.pack(pady=20)

# Sidebar buttons
for text in ["Validar todo", "Lexico", "Sintaxis", "Semantica", "Subir archivo"]:
    btn = ttk.Button(sidebar, text=text, style="TButton")
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
sample_code = '''using System;
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
code_text.insert("1.0", sample_code)

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
