# Generated from Complejos.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ComplejosParser import ComplejosParser
else:
    from ComplejosParser import ComplejosParser

# This class defines a complete listener for a parse tree produced by ComplejosParser.
class ComplejosListener(ParseTreeListener):

    # Enter a parse tree produced by ComplejosParser#expr.
    def enterExpr(self, ctx:ComplejosParser.ExprContext):
        pass

    # Exit a parse tree produced by ComplejosParser#expr.
    def exitExpr(self, ctx:ComplejosParser.ExprContext):
        pass


    # Enter a parse tree produced by ComplejosParser#addSubExpr.
    def enterAddSubExpr(self, ctx:ComplejosParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by ComplejosParser#addSubExpr.
    def exitAddSubExpr(self, ctx:ComplejosParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by ComplejosParser#singleTermExpr.
    def enterSingleTermExpr(self, ctx:ComplejosParser.SingleTermExprContext):
        pass

    # Exit a parse tree produced by ComplejosParser#singleTermExpr.
    def exitSingleTermExpr(self, ctx:ComplejosParser.SingleTermExprContext):
        pass


    # Enter a parse tree produced by ComplejosParser#singleFactorExpr.
    def enterSingleFactorExpr(self, ctx:ComplejosParser.SingleFactorExprContext):
        pass

    # Exit a parse tree produced by ComplejosParser#singleFactorExpr.
    def exitSingleFactorExpr(self, ctx:ComplejosParser.SingleFactorExprContext):
        pass


    # Enter a parse tree produced by ComplejosParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:ComplejosParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by ComplejosParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:ComplejosParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by ComplejosParser#parenExpr.
    def enterParenExpr(self, ctx:ComplejosParser.ParenExprContext):
        pass

    # Exit a parse tree produced by ComplejosParser#parenExpr.
    def exitParenExpr(self, ctx:ComplejosParser.ParenExprContext):
        pass


    # Enter a parse tree produced by ComplejosParser#complexNumExpr.
    def enterComplexNumExpr(self, ctx:ComplejosParser.ComplexNumExprContext):
        pass

    # Exit a parse tree produced by ComplejosParser#complexNumExpr.
    def exitComplexNumExpr(self, ctx:ComplejosParser.ComplexNumExprContext):
        pass


    # Enter a parse tree produced by ComplejosParser#complexFull.
    def enterComplexFull(self, ctx:ComplejosParser.ComplexFullContext):
        pass

    # Exit a parse tree produced by ComplejosParser#complexFull.
    def exitComplexFull(self, ctx:ComplejosParser.ComplexFullContext):
        pass


    # Enter a parse tree produced by ComplejosParser#realOnly.
    def enterRealOnly(self, ctx:ComplejosParser.RealOnlyContext):
        pass

    # Exit a parse tree produced by ComplejosParser#realOnly.
    def exitRealOnly(self, ctx:ComplejosParser.RealOnlyContext):
        pass


    # Enter a parse tree produced by ComplejosParser#imagOnly.
    def enterImagOnly(self, ctx:ComplejosParser.ImagOnlyContext):
        pass

    # Exit a parse tree produced by ComplejosParser#imagOnly.
    def exitImagOnly(self, ctx:ComplejosParser.ImagOnlyContext):
        pass



del ComplejosParser