# 🧠 Analizador Léxico, Sintáctico y Semántico para C#

**Autores:** Levin Morán, Kevin Mejía

---

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

C:.
├───Algorithms
│   ├───BinarySearch.cs
│   ├───QuickSort.cs
│   └───Program.cs
└───Ply
    └───PLY.py

---

## 📚 Referencias

- .NET (n.d.). *Documentación oficial de .NET y C#*  
- Bill Wagner (n.d.). *Introducción a C# y .NET*  
- Josiastech (n.d.). *PLY: Python Lex-Yacc implementation*
