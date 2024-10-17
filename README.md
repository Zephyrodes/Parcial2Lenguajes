# Parcial 2 Lenguajes

## Punto 1 - Evaluador de Números Complejos

Este punto es un evaluador de expresiones de números complejos utilizando ANTLR y Python. Permite realizar operaciones como suma, resta, multiplicación y división en números complejos ingresados en forma textual.

## Características

- Soporte para operaciones básicas de números complejos: suma, resta, multiplicación y división.
- Entrada de expresiones complejas a través de la consola.
- Manejo de partes reales e imaginarias, incluyendo números negativos y diferentes formatos de entrada.
- Uso de ANTLR para el análisis y la evaluación de expresiones.

## Requisitos

- Python 3.12
- ANTLR 4.13.2

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Zephyrodes/Parcial2Lenguajes.git
   cd Parcial2Lenguajes/Punto1
   
2. Configuración del Entorno Virtual e Instalación de Dependencias

 **Crea un entorno virtual** con el siguiente comando:
   ```bash
   python3 -m venv myenv
   ```
**Activa el entorno virtual** con el siguiente comando:
   ```bash
   source myenv/bin/activate
   ```

3. **Instala los paquetes de Python requeridos**:
   ```bash
   pip install antlr4-python3-runtime
   ```
   
### Genera los archivos de ANTLR (si no lo has hecho ya)

Asegúrate de tener ANTLR instalado. Sigue las instrucciones en la página de ANTLR para la configuración. Ejecuta los siguientes comandos para generar el lexer y el parser:

```bash
antlr4 -Dlanguage=Python3 Complejos.g4 -listener
```
## Uso

1. Ejecuta el script principal:

   ```bash
   python3 complejos.py
   ```

2. Ingresar Expresión Compleja

Cuando el programa lo solicite, ingresa una expresión con números complejos. Ejemplo:

```bash
   (2 + 7i) + (3 - 4i)
```

3.Después de ingresar la expresión, el programa calculará y mostrará el resultado. Ejemplo:

```bash
Resultado: (5 + 3j)
```

## Punto 2 - Funciones MAP y FILTER en Python

Este proyecto implementa un lenguaje sencillo que soporta dos funciones principales, `MAP` y `FILTER`, utilizando ANTLR para generar el parser y Python como lenguaje objetivo. Las funciones permiten operar sobre objetos iterables, como listas y tuplas.

## Características

- **MAP**: Aplica una función a cada elemento de un objeto iterable y devuelve una nueva colección con los resultados.
  - Ejemplo: `MAP(double, [1, 2, 3])` devuelve `[2, 4, 6]`
  
- **FILTER**: Filtra los elementos de una colección según una función condicional, devolviendo una nueva colección con los elementos que cumplen la condición.
  - Ejemplo: `FILTER(is_even, (1, 2, 3, 4))` devuelve `[2, 4]`

## Estructura del Proyecto

```plaintext
.
├── IterableFunctions.g4        # Archivo de gramática ANTLR
├── IterableFunctionsLexer.py   # Lexer generado por ANTLR
├── IterableFunctionsParser.py  # Parser generado por ANTLR
├── IterableFunctionsVisitor.py # Visitor generado por ANTLR
├── Main.py                     # Archivo principal de ejecución
└── README.md                   # Documentación del proyecto
```

## Requisitos

- Python 3.12
- ANTLR 4.13.2

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Zephyrodes/Parcial2Lenguajes.git
   cd Parcial2Lenguajes/Punto2
   
2. Configuración del Entorno Virtual e Instalación de Dependencias

 **Crea un entorno virtual** con el siguiente comando:
   ```bash
   python3 -m venv myenv
   ```
**Activa el entorno virtual** con el siguiente comando:
   ```bash
   source myenv/bin/activate
   ```

3. **Instala los paquetes de Python requeridos**:
   ```bash
   pip install antlr4-python3-runtime
   ```
   
### Genera los archivos de ANTLR (si no lo has hecho ya)

Asegúrate de tener ANTLR instalado. Sigue las instrucciones en la página de ANTLR para la configuración. Ejecuta los siguientes comandos para generar el lexer y el parser:

```bash
antlr4 -Dlanguage=Python3 IterableFunctions.g4
```
## Uso

1. Ejecuta el script principal:

   ```bash
   python3 main.py
   ```

2. Introduce el código con el formato correcto en la consola. Ejemplos:

```bash
   MAP(double, [1, 2, 3, 4, 5])
```

```bash
   FILTER(is_even, (1, 2, 3, 4, 5))
```

## Punto 3 - Calculadora de Transformada de Fourier

En este punto se encuentra una aplicación en Python que calcula la Transformada de Fourier Discreta (DFT) de funciones matemáticas utilizando ANTLR para el análisis sintáctico. Permite a los usuarios definir funciones, aplicar transformadas de Fourier y evaluar expresiones como seno, coseno y funciones exponenciales.

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Descripción de la Gramática](#descripción-de-la-gramática)
- [Ejemplos](#ejemplos)

## Características

- Definir funciones matemáticas utilizando una sintaxis simple.
- Realizar la Transformada de Fourier Discreta (DFT) sobre funciones definidas.
- Contiene varias operaciones matemáticas, incluyendo adición, sustracción, multiplicación, división y exponentiación.

## Requisitos

- Python 3.12
- ANTLR 4.13.2
- NumPy

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Zephyrodes/Parcial2Lenguajes.git
   cd Parcial2Lenguajes/Punto3

2. Configuración del Entorno Virtual e Instalación de Dependencias

 **Crea un entorno virtual** con el siguiente comando:
   ```bash
   python3 -m venv myenv
   ```
**Activa el entorno virtual** con el siguiente comando:
   ```bash
   source myenv/bin/activate
   ```

3. **Instala los paquetes de Python requeridos**:
   ```bash
   pip install antlr4-python3-runtime numpy
   ```
   
### Genera los archivos de ANTLR (si no lo has hecho ya)

Asegúrate de tener ANTLR instalado. Sigue las instrucciones en la página de ANTLR para la configuración. Ejecuta los siguientes comandos para generar el lexer y el parser:

```bash
antlr4 -Dlanguage=Python3 Fourier.g4 -listener -visitor
```

## Uso

1. **Crea un archivo de texto** llamado `programa_fourier.txt` con tus funciones matemáticas y declaraciones de transformada de Fourier.  
Contenido de ejemplo:
   
```bash
funcion f(x) = sin(2 * pi * x); transformada de F(f);
```

2. **Ejecuta el programa**:
```bash
python3 FourierEjecut.py programa_fourier.txt
```


## Descripción de la Gramática

La gramática para este proyecto está definida en `Fourier.g4` e incluye reglas para:

- **Expresiones matemáticas** (suma, resta, multiplicación, división, potencia).
- **Declaraciones de funciones**.
- **Declaraciones de transformadas de Fourier**.
- **Uso de constantes** como `pi` y funciones incorporadas como `sin`, `cos` y `exp`.

### Reglas Clave de la Gramática

- **Expresiones**: Pueden estar compuestas de números, variables y operaciones matemáticas.
- **Declaraciones de Funciones**: Definen una función con parámetros y una expresión.
- **Transformada de Fourier**: Especifica una función para calcular su transformada de Fourier.

- 
## Ejemplos

### Ejemplo 1: Función Seno

```plaintext
funcion f(x) = sin(2 * pi * x);
transformada de F(f);
```
### Ejemplo 2: Función Coseno
```plaintext
funcion g(x) = cos(3 * pi * x);
transformada de G(g);
```
### Ejemplo 3: Combinación de Funciones
```plaintext
funcion h(x) = sin(2 * pi * x) + cos(3 * pi * x);
transformada de H(h);
```
### Ejemplo 4: Función con Potencia
```plaintext
funcion j(x) = (sin(2 * pi * x))^2;
transformada de J(j);
```
