import sys
from antlr4 import *
from MapFunctionLexer import MapFunctionLexer
from MapFunctionParser import MapFunctionParser

class MapFunctionExecutor(ParseTreeVisitor):
    def visitProgram(self, ctx):
        function = self.visit(ctx.function())
        iterable = self.visit(ctx.iterable())
        print(f"Function: {function}")
        print(f"Iterable: {iterable}")

        if function is None or iterable is None:
            print("Error: Función o iterable es None.")
            return None

        try:
            result = list(map(function, iterable))
            print(f"Result: {result}")
            return result
        except Exception as e:
            print(f"Error aplicando la función: {e}")
            return None

    def visitFunction(self, ctx):
        params = [p.getText() for p in ctx.param()]
        expression = ctx.expression().getText()
        print(f"Params: {params}")
        print(f"Expression: {expression}")

        try:
            lambda_func = eval(f"lambda {', '.join(params)}: {expression}")
            print(f"Created lambda: {lambda_func}")
            return lambda_func
        except Exception as e:
            print(f"Error creando lambda: {e}")
            return None

    def visitItem_list(self, ctx):
        values = [self.visit(expr) for expr in ctx.expression()]
        print(f"Item list values: {values}")
        return values

    def visitExpression(self, ctx):
        if ctx.NUMBER():
            print(f"Visiting Number: {ctx.NUMBER().getText()}")
            return int(ctx.NUMBER().getText())
        elif ctx.ID():
            print(f"Visiting ID: {ctx.ID().getText()}")
            return ctx.ID().getText()
        elif ctx.operator():
            print("Visiting Operator...")
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            operator = ctx.operator().getText()
            print(f"Operator: {operator}, Left: {left}, Right: {right}")
            return f"({left} {operator} {right})"
        elif ctx.getChildCount() == 3:
            return self.visit(ctx.expression(0))

def main(argv):
    if len(argv) < 2:
        print("Por favor, proporciona un archivo de entrada.")
        return
    input_stream = FileStream(argv[1])
    lexer = MapFunctionLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MapFunctionParser(stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))
    executor = MapFunctionExecutor()
    result = executor.visit(tree)
    print(f"Final Result: {result}")

if __name__ == '__main__':
    main(sys.argv)

