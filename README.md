# Parcial 2 Lenguajes

# Punto 3 - Calculadora de Transformada de Fourier

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
   git clone https://github.com/tuusuario/tu-repo-nombre.git
   cd tu-repo-nombre

2. **Instala los paquetes de Python requeridos**:
   ```bash
   pip install antlr4-python3-runtime numpy

### Genera los archivos de ANTLR (si no lo has hecho ya)

Asegúrate de tener ANTLR instalado. Sigue las instrucciones en la página de ANTLR para la configuración. Ejecuta los siguientes comandos para generar el lexer y el parser:

```bash
antlr4 -Dlanguage=Python3 Fourier.g4

## Uso

1. **Crea un archivo de texto** llamado `programa_fourier.txt` con tus funciones matemáticas y declaraciones de transformada de Fourier.  
   Contenido de ejemplo:
