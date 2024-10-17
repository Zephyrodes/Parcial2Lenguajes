import sys
from antlr4 import *
from IterableFunctionsLexer import IterableFunctionsLexer
from IterableFunctionsParser import IterableFunctionsParser

# Funciones de ejemplo para MAP y FILTER
def double(x):
    return x * 2

def is_even(x):
    return x % 2 == 0

def execute_map(func_name, iterable):
    func = globals().get(func_name)
    if func and callable(func):
        return [func(item) for item in iterable]
    else:
        raise ValueError(f"Function {func_name} is not defined.")

def execute_filter(func_name, iterable):
    func = globals().get(func_name)
    if func and callable(func):
        return [item for item in iterable if func(item)]
    else:
        raise ValueError(f"Function {func_name} is not defined.")

# Visitor para procesar el árbol de sintaxis
class IterableFunctionsVisitor(ParseTreeVisitor):
    def visitMapFunction(self, ctx):
        func_name = ctx.IDENTIFIER(0).getText()  # Obtenemos el nombre de la función
        iterable = self.visit(ctx.iterable())
        return execute_map(func_name, iterable)
    
    def visitFilterFunction(self, ctx):
        func_name = ctx.IDENTIFIER(0).getText()  # Obtenemos el nombre de la función condicional
        iterable = self.visit(ctx.iterable())
        return execute_filter(func_name, iterable)
    
    def visitList(self, ctx):
        return [int(item.getText()) for item in ctx.expression()]  # Convierte a entero
    
    def visitTuple(self, ctx):
        return [int(item.getText()) for item in ctx.expression()]  # Convierte a entero

# Función principal
def main():
    input_stream = InputStream(input("Ingrese el código: "))
    lexer = IterableFunctionsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = IterableFunctionsParser(stream)
    
    tree = parser.program()  # Analiza el árbol de sintaxis
    visitor = IterableFunctionsVisitor()
    result = visitor.visit(tree)
    
    # Asegúrate de imprimir solo si hay un resultado
    if result is not None:
        print("Resultado:", result)
    else:
        print("No hay resultado")

if __name__ == '__main__':
    main()

