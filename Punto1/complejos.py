from antlr4 import *
from ComplejosLexer import ComplejosLexer
from ComplejosParser import ComplejosParser
from ComplejosListener import ComplejosListener
from antlr4.error.ErrorListener import ErrorListener


class ComplejosListenerImpl(ComplejosListener):
    def __init__(self):
        self.stack = []

    # Entrada a una expresión de suma/resta
    def exitAddSubExpr(self, ctx):
        right = self.stack.pop()
        left = self.stack.pop()
        if ctx.getChild(1).getText() == '+':
            self.stack.append(left + right)
        else:
            self.stack.append(left - right)

    # Entrada a una expresión de multiplicación/división
    def exitMulDivExpr(self, ctx):
        right = self.stack.pop()
        left = self.stack.pop()
        if ctx.getChild(1).getText() == '*':
            self.stack.append(left * right)
        else:
            self.stack.append(left / right)

    # Entrada a una expresión compleja completa
    def exitComplexFull(self, ctx):
        real_part = 0
        imag_part = 0

        # Verificar la parte real
        if ctx.REAL_SIGNED():
            real_part = float(ctx.REAL_SIGNED().getText())

        # Verificar la parte imaginaria
        if ctx.IMAG_PART():
            imag_part_str = ctx.IMAG_PART().getText().replace('i', '')
            imag_part = float(imag_part_str)

            # Comprobar si la parte imaginaria tiene un signo negativo
            if '-' in ctx.getText():  # Comprobar si el contexto tiene un signo negativo
                imag_part = -imag_part

        # Agregar el número complejo al stack
        self.stack.append(complex(real_part, imag_part))

    # Entrada a una parte real solamente
    def exitRealOnly(self, ctx):
        real_part = float(ctx.REAL_SIGNED().getText())
        self.stack.append(complex(real_part, 0))

    # Entrada a una parte imaginaria solamente
    def exitImagOnly(self, ctx):
        imag_part = float(ctx.IMAG_PART().getText().replace('i', ''))
        self.stack.append(complex(0, imag_part))

    # Manejo de expresiones entre paréntesis
    def exitParenExpr(self, ctx):
        # Ya debería estar procesado en la pila
        pass


# Error listener para manejar errores de sintaxis
class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at {line}:{column} - {msg}")


def main():
    # Solicitar al usuario que ingrese la expresión
    input_expr = input("Ingrese la expresión compleja (ej. (2 + 7i) + (3 - 4i)): ")

    lexer = ComplejosLexer(InputStream(input_expr))
    lexer.removeErrorListeners()
    lexer.addErrorListener(MyErrorListener())

    stream = CommonTokenStream(lexer)

    parser = ComplejosParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())

    tree = parser.expr()

    # Listener para recorrer el árbol
    listener = ComplejosListenerImpl()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # El resultado final está en el tope de la pila
    result = listener.stack.pop()
    print(f"Resultado: {result}")


if __name__ == "__main__":
    main()


