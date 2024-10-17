from FourierParser import FourierParser
from FourierVisitor import FourierVisitor
import numpy as np

class FourierDFTVisitor(FourierVisitor):

    def __init__(self):
        self.functions = {}  # Para almacenar las funciones definidas
    
    # Visita la declaración de funciones
    def visitFuncionDecl(self, ctx):
        func_name = ctx.ID(0).getText()  # Nombre de la función
        param_name = ctx.ID(1).getText()  # Parámetro (ej: x)
        expression = self.visit(ctx.expr())  # Visitamos la expresión de la función
        self.functions[func_name] = (param_name, expression)
    
    # Visita la Transformada de Fourier
    def visitFourierTransform(self, ctx):
        func_name = ctx.ID(0).getText()  # Obtenemos el nombre de la función
        if func_name in self.functions:
            param_name, expression = self.functions[func_name]
            print(f"Calculando transformada de Fourier para {func_name} con expresión: {expression}")
            self.calcular_transformada_dft(expression)
        else:
            print(f"Error: la función {func_name} no está definida.")

    # Calcula la transformada de Fourier Discreta (DFT)
    def calcular_transformada_dft(self, funcion):
        N = 500  # Número de puntos
        t = np.linspace(0, 1, N)  # Variable de tiempo t
        f_t = eval(funcion, {"np": np, "t": t})  # Evaluamos la función (ej: np.sin(2 * np.pi * t))
        
        transformada = []
        for k in range(N):
            suma_real = 0
            suma_imag = 0
            for n in range(N):
                angulo = -2j * np.pi * k * n / N
                suma_real += f_t[n] * np.cos(angulo.imag)
                suma_imag += f_t[n] * np.sin(angulo.imag)
            transformada.append(suma_real + suma_imag * 1j)
        
        print(f"Transformada de Fourier: {transformada}")

    # Visita expresiones con multiplicación y división
    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*':
            return f"({left} * {right})"
        else:
            return f"({left} / {right})"

    # Visita expresiones con suma y resta
    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            return f"({left} + {right})"
        else:
            return f"({left} - {right})"

    # Visita expresiones que incluyen 'sin'
    def visitSinExpr(self, ctx):
        expr = self.visit(ctx.expr())
        return f"np.sin({expr})"
    
    # Visita números
    def visitNumberExpr(self, ctx):
        return ctx.getText()

    # Visita la constante 'pi'
    def visitPiExpr(self, ctx):
        return "np.pi"  # Devuelve el valor de pi en numpy

    # Visita la variable 'x'
    def visitIdExpr(self, ctx):
        if ctx.getText() == "x":
            return "t"  # Variable 'x' se mapea a 't' en el cálculo
        return ctx.getText()
