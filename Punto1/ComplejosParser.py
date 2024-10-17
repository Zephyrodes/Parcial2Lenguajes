# Generated from Complejos.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,5,1,20,8,1,10,1,12,1,23,9,1,1,2,1,2,1,2,1,
        2,1,2,1,2,5,2,31,8,2,10,2,12,2,34,9,2,1,3,1,3,1,3,1,3,1,3,3,3,41,
        8,3,1,4,1,4,1,4,1,4,1,4,3,4,48,8,4,1,4,0,2,2,4,5,0,2,4,6,8,0,2,1,
        0,1,2,1,0,3,4,49,0,10,1,0,0,0,2,13,1,0,0,0,4,24,1,0,0,0,6,40,1,0,
        0,0,8,47,1,0,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,
        6,1,-1,0,14,15,3,4,2,0,15,21,1,0,0,0,16,17,10,2,0,0,17,18,7,0,0,
        0,18,20,3,4,2,0,19,16,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,
        1,0,0,0,22,3,1,0,0,0,23,21,1,0,0,0,24,25,6,2,-1,0,25,26,3,6,3,0,
        26,32,1,0,0,0,27,28,10,2,0,0,28,29,7,1,0,0,29,31,3,6,3,0,30,27,1,
        0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,5,1,0,0,0,34,
        32,1,0,0,0,35,36,5,5,0,0,36,37,3,2,1,0,37,38,5,6,0,0,38,41,1,0,0,
        0,39,41,3,8,4,0,40,35,1,0,0,0,40,39,1,0,0,0,41,7,1,0,0,0,42,43,5,
        7,0,0,43,44,7,0,0,0,44,48,5,9,0,0,45,48,5,7,0,0,46,48,5,9,0,0,47,
        42,1,0,0,0,47,45,1,0,0,0,47,46,1,0,0,0,48,9,1,0,0,0,4,21,32,40,47
    ]

class ComplejosParser ( Parser ):

    grammarFileName = "Complejos.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "REAL_SIGNED", 
                      "REAL", "IMAG_PART", "WS" ]

    RULE_expr = 0
    RULE_complex_expr = 1
    RULE_complex_term = 2
    RULE_complex_factor = 3
    RULE_complex_number = 4

    ruleNames =  [ "expr", "complex_expr", "complex_term", "complex_factor", 
                   "complex_number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    REAL_SIGNED=7
    REAL=8
    IMAG_PART=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def complex_expr(self):
            return self.getTypedRuleContext(ComplejosParser.Complex_exprContext,0)


        def EOF(self):
            return self.getToken(ComplejosParser.EOF, 0)

        def getRuleIndex(self):
            return ComplejosParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ComplejosParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.complex_expr(0)
            self.state = 11
            self.match(ComplejosParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Complex_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComplejosParser.RULE_complex_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddSubExprContext(Complex_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplejosParser.Complex_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def complex_expr(self):
            return self.getTypedRuleContext(ComplejosParser.Complex_exprContext,0)

        def complex_term(self):
            return self.getTypedRuleContext(ComplejosParser.Complex_termContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class SingleTermExprContext(Complex_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplejosParser.Complex_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def complex_term(self):
            return self.getTypedRuleContext(ComplejosParser.Complex_termContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleTermExpr" ):
                listener.enterSingleTermExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleTermExpr" ):
                listener.exitSingleTermExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleTermExpr" ):
                return visitor.visitSingleTermExpr(self)
            else:
                return visitor.visitChildren(self)



    def complex_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ComplejosParser.Complex_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_complex_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ComplejosParser.SingleTermExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 14
            self.complex_term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 21
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ComplejosParser.AddSubExprContext(self, ComplejosParser.Complex_exprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_complex_expr)
                    self.state = 16
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 17
                    _la = self._input.LA(1)
                    if not(_la==1 or _la==2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 18
                    self.complex_term(0) 
                self.state = 23
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Complex_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComplejosParser.RULE_complex_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SingleFactorExprContext(Complex_termContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplejosParser.Complex_termContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def complex_factor(self):
            return self.getTypedRuleContext(ComplejosParser.Complex_factorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleFactorExpr" ):
                listener.enterSingleFactorExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleFactorExpr" ):
                listener.exitSingleFactorExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleFactorExpr" ):
                return visitor.visitSingleFactorExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(Complex_termContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplejosParser.Complex_termContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def complex_term(self):
            return self.getTypedRuleContext(ComplejosParser.Complex_termContext,0)

        def complex_factor(self):
            return self.getTypedRuleContext(ComplejosParser.Complex_factorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)



    def complex_term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ComplejosParser.Complex_termContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_complex_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ComplejosParser.SingleFactorExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 25
            self.complex_factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ComplejosParser.MulDivExprContext(self, ComplejosParser.Complex_termContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_complex_term)
                    self.state = 27
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 28
                    _la = self._input.LA(1)
                    if not(_la==3 or _la==4):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 29
                    self.complex_factor() 
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Complex_factorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComplejosParser.RULE_complex_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComplexNumExprContext(Complex_factorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplejosParser.Complex_factorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def complex_number(self):
            return self.getTypedRuleContext(ComplejosParser.Complex_numberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplexNumExpr" ):
                listener.enterComplexNumExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplexNumExpr" ):
                listener.exitComplexNumExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexNumExpr" ):
                return visitor.visitComplexNumExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(Complex_factorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplejosParser.Complex_factorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def complex_expr(self):
            return self.getTypedRuleContext(ComplejosParser.Complex_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def complex_factor(self):

        localctx = ComplejosParser.Complex_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_complex_factor)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = ComplejosParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(ComplejosParser.T__4)
                self.state = 36
                self.complex_expr(0)
                self.state = 37
                self.match(ComplejosParser.T__5)
                pass
            elif token in [7, 9]:
                localctx = ComplejosParser.ComplexNumExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.complex_number()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Complex_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ComplejosParser.RULE_complex_number

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RealOnlyContext(Complex_numberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplejosParser.Complex_numberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REAL_SIGNED(self):
            return self.getToken(ComplejosParser.REAL_SIGNED, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRealOnly" ):
                listener.enterRealOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRealOnly" ):
                listener.exitRealOnly(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRealOnly" ):
                return visitor.visitRealOnly(self)
            else:
                return visitor.visitChildren(self)


    class ComplexFullContext(Complex_numberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplejosParser.Complex_numberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REAL_SIGNED(self):
            return self.getToken(ComplejosParser.REAL_SIGNED, 0)
        def IMAG_PART(self):
            return self.getToken(ComplejosParser.IMAG_PART, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplexFull" ):
                listener.enterComplexFull(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplexFull" ):
                listener.exitComplexFull(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplexFull" ):
                return visitor.visitComplexFull(self)
            else:
                return visitor.visitChildren(self)


    class ImagOnlyContext(Complex_numberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ComplejosParser.Complex_numberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IMAG_PART(self):
            return self.getToken(ComplejosParser.IMAG_PART, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImagOnly" ):
                listener.enterImagOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImagOnly" ):
                listener.exitImagOnly(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImagOnly" ):
                return visitor.visitImagOnly(self)
            else:
                return visitor.visitChildren(self)



    def complex_number(self):

        localctx = ComplejosParser.Complex_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_complex_number)
        self._la = 0 # Token type
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = ComplejosParser.ComplexFullContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(ComplejosParser.REAL_SIGNED)
                self.state = 43
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 44
                self.match(ComplejosParser.IMAG_PART)
                pass

            elif la_ == 2:
                localctx = ComplejosParser.RealOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(ComplejosParser.REAL_SIGNED)
                pass

            elif la_ == 3:
                localctx = ComplejosParser.ImagOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.match(ComplejosParser.IMAG_PART)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.complex_expr_sempred
        self._predicates[2] = self.complex_term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def complex_expr_sempred(self, localctx:Complex_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def complex_term_sempred(self, localctx:Complex_termContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




