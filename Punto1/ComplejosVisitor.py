# Generated from Complejos.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ComplejosParser import ComplejosParser
else:
    from ComplejosParser import ComplejosParser

# This class defines a complete generic visitor for a parse tree produced by ComplejosParser.

class ComplejosVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ComplejosParser#expr.
    def visitExpr(self, ctx:ComplejosParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#addSubExpr.
    def visitAddSubExpr(self, ctx:ComplejosParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#singleTermExpr.
    def visitSingleTermExpr(self, ctx:ComplejosParser.SingleTermExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#singleFactorExpr.
    def visitSingleFactorExpr(self, ctx:ComplejosParser.SingleFactorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:ComplejosParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#parenExpr.
    def visitParenExpr(self, ctx:ComplejosParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#complexNumExpr.
    def visitComplexNumExpr(self, ctx:ComplejosParser.ComplexNumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#complexFull.
    def visitComplexFull(self, ctx:ComplejosParser.ComplexFullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#realOnly.
    def visitRealOnly(self, ctx:ComplejosParser.RealOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ComplejosParser#imagOnly.
    def visitImagOnly(self, ctx:ComplejosParser.ImagOnlyContext):
        return self.visitChildren(ctx)



del ComplejosParser