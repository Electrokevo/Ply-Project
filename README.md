# 🧠 Analizador Léxico, Sintáctico y Semántico para C#

**Autores:** Levin Morán, Kevin Mejía

---

## 📃 Intrucciones

El archivo a ejecutar es PLY.py, se lo puede ejecutar con el siguiente comando dentro de la carpeta PLY:

`python frontend.py`

Al ejecutarlo no se deberia mostrar nada en consola, pero se crea un nuevo archivo en la carpeta logs, con el nombre del usuario que clono el repositoria y la fecha.

Este archivo contiene todos los tokens que el lexer analizo, incluye informacion como el tipo de token, su valor y la posicion del mismo.

Las librererias necesarias para ejecutar el programa son:
-tkinter: usado para la UI (viene por defecto en python, pero en algunos casos hay que activarlo)
-pillow: usado para insertar las imagenes (el logo)

Nota: Por alguna razon al clonar el repositorio la carpeta de logs y de los algoritmos se clona dentro o fuera de la carpeta PLY, por lo que en caso de recibir un error al ejecutar el archivo PLY.py, por favor intente cambiar el path de los archivos en el mismo PLY.py

## 📌 Introducción

C# es un lenguaje de programación moderno, innovador, de código abierto, multiplataforma y orientado a objetos. Se encuentra entre los cinco lenguajes más utilizados en GitHub. Algunas de sus características más destacadas incluyen:

- Seguridad de tipos  
- Soporte para genéricos  
- Coincidencia de patrones  
- Programación asincrónica  
- Registros (records)  
- Y mucho más...  

> "C# es el lenguaje más popular para la plataforma .NET, la cual permite crear aplicaciones para dispositivos móviles, de escritorio, servidores, IoT, y la nube."  
> — *Bill Wagner, .NET Docs*

---

## 🛠️ Tecnologías utilizadas

### 🔹 PLY (Python Lex-Yacc)

PLY es una implementación en Python de las herramientas clásicas de construcción de compiladores **Lex** y **Yacc**. Está diseñada para ser educativa y mantener una alta fidelidad con los algoritmos y estructuras originales, especialmente el algoritmo **LALR(1)** (Look-Ahead LR parser) utilizado por Yacc.

Características principales:

- Compatibilidad con LALR(1)
- Validación y diagnóstico detallado de errores
- Informes útiles para depurar analizadores
- Ideal para uso académico y educativo

---

## 🧩 Descripción del Proyecto

Este proyecto consiste en la implementación de un **analizador para el lenguaje de programación C#**, encargado de realizar análisis en tres niveles:

### 🔍 Análisis Léxico

- Identificación de **tokens**
- Detección de **errores léxicos**
- Eliminación de **comentarios**

### 🧱 Análisis Sintáctico

- Uso de **gramáticas formales**
- Detección de **errores sintácticos**
- Creación de **árboles de sintaxis abstracta (AST)**

### 📐 Análisis Semántico

- Verificación de **compatibilidad de tipos**
- Validación del **retorno de funciones**
- Uso correcto de **estructuras de control**

---

## 📁 Estructura del Proyecto

/Ply-Project/<br>
├── /Algorithms/ # Solucion para algoritmos de c#<br>
│   	├── BinarySearch.cs<br>
│   	├── QuickSort.cs<br>
│   	└── Program.cs<br>
├── /PLY/ # Solucion para el project<br>
│   	└── Program.cs<br>
└── README.md # Este archivo<br>

---

## 📚 Referencias

- .NET (n.d.). *Documentación oficial de .NET y C#*  
- Bill Wagner (n.d.). *Introducción a C# y .NET*  
- Josiastech (n.d.). *PLY: Python Lex-Yacc implementation*
