# Generated from RegExp.g4 by ANTLR 4.13.2
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
        4,1,23,117,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,56,8,3,10,3,12,3,
        59,9,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,68,8,3,10,3,12,3,71,9,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,80,8,3,10,3,12,3,83,9,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,115,8,3,1,3,0,
        0,4,0,2,4,6,0,0,132,0,11,1,0,0,0,2,16,1,0,0,0,4,21,1,0,0,0,6,114,
        1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,1,0,0,0,11,12,
        1,0,0,0,12,14,1,0,0,0,13,11,1,0,0,0,14,15,3,4,2,0,15,1,1,0,0,0,16,
        17,5,20,0,0,17,18,5,1,0,0,18,19,3,6,3,0,19,20,5,22,0,0,20,3,1,0,
        0,0,21,22,5,2,0,0,22,23,3,6,3,0,23,24,5,22,0,0,24,5,1,0,0,0,25,26,
        5,3,0,0,26,115,5,4,0,0,27,28,5,3,0,0,28,29,3,6,3,0,29,30,5,4,0,0,
        30,115,1,0,0,0,31,115,5,21,0,0,32,33,5,5,0,0,33,34,5,3,0,0,34,115,
        5,4,0,0,35,36,5,6,0,0,36,37,5,3,0,0,37,38,3,6,3,0,38,39,5,4,0,0,
        39,115,1,0,0,0,40,41,5,7,0,0,41,42,5,3,0,0,42,43,3,6,3,0,43,44,5,
        4,0,0,44,115,1,0,0,0,45,46,5,8,0,0,46,47,5,3,0,0,47,48,3,6,3,0,48,
        49,5,4,0,0,49,115,1,0,0,0,50,51,5,9,0,0,51,52,5,3,0,0,52,57,3,6,
        3,0,53,54,5,10,0,0,54,56,3,6,3,0,55,53,1,0,0,0,56,59,1,0,0,0,57,
        55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,61,5,4,0,
        0,61,115,1,0,0,0,62,63,5,11,0,0,63,64,5,3,0,0,64,69,3,6,3,0,65,66,
        5,10,0,0,66,68,3,6,3,0,67,65,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,
        69,70,1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,73,5,4,0,0,73,115,1,
        0,0,0,74,75,5,12,0,0,75,76,5,3,0,0,76,81,3,6,3,0,77,78,5,10,0,0,
        78,80,3,6,3,0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,
        0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,4,0,0,85,115,1,0,0,0,86,
        87,5,13,0,0,87,88,5,3,0,0,88,89,3,6,3,0,89,90,5,4,0,0,90,115,1,0,
        0,0,91,92,5,14,0,0,92,93,5,3,0,0,93,94,5,19,0,0,94,115,5,4,0,0,95,
        96,5,15,0,0,96,97,5,3,0,0,97,98,5,19,0,0,98,115,5,4,0,0,99,100,5,
        16,0,0,100,101,5,3,0,0,101,102,5,19,0,0,102,115,5,4,0,0,103,104,
        5,17,0,0,104,105,5,3,0,0,105,106,3,6,3,0,106,107,5,4,0,0,107,115,
        1,0,0,0,108,109,5,18,0,0,109,110,5,3,0,0,110,111,3,6,3,0,111,112,
        5,4,0,0,112,115,1,0,0,0,113,115,5,20,0,0,114,25,1,0,0,0,114,27,1,
        0,0,0,114,31,1,0,0,0,114,32,1,0,0,0,114,35,1,0,0,0,114,40,1,0,0,
        0,114,45,1,0,0,0,114,50,1,0,0,0,114,62,1,0,0,0,114,74,1,0,0,0,114,
        86,1,0,0,0,114,91,1,0,0,0,114,95,1,0,0,0,114,99,1,0,0,0,114,103,
        1,0,0,0,114,108,1,0,0,0,114,113,1,0,0,0,115,7,1,0,0,0,5,11,57,69,
        81,114
    ]

class RegExpParser ( Parser ):

    grammarFileName = "RegExp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'return'", "'('", "')'", "'Any'", 
                     "'ZeroOrMore'", "'OneOrMore'", "'Maybe'", "'Or'", "','", 
                     "'And'", "'Concat'", "'Contains'", "'Tam'", "'TamMin'", 
                     "'TamMax'", "'Prefix'", "'Suffix'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "VAR", 
                      "CHAIN", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_returnStat = 2
    RULE_exp = 3

    ruleNames =  [ "prog", "stat", "returnStat", "exp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    INT=19
    VAR=20
    CHAIN=21
    NEWLINE=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnStat(self):
            return self.getTypedRuleContext(RegExpParser.ReturnStatContext,0)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegExpParser.StatContext)
            else:
                return self.getTypedRuleContext(RegExpParser.StatContext,i)


        def getRuleIndex(self):
            return RegExpParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = RegExpParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 8
                self.stat()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 14
            self.returnStat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(RegExpParser.VAR, 0)

        def exp(self):
            return self.getTypedRuleContext(RegExpParser.ExpContext,0)


        def NEWLINE(self):
            return self.getToken(RegExpParser.NEWLINE, 0)

        def getRuleIndex(self):
            return RegExpParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = RegExpParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(RegExpParser.VAR)
            self.state = 17
            self.match(RegExpParser.T__0)
            self.state = 18
            self.exp()
            self.state = 19
            self.match(RegExpParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(RegExpParser.ExpContext,0)


        def NEWLINE(self):
            return self.getToken(RegExpParser.NEWLINE, 0)

        def getRuleIndex(self):
            return RegExpParser.RULE_returnStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStat" ):
                listener.enterReturnStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStat" ):
                listener.exitReturnStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStat" ):
                return visitor.visitReturnStat(self)
            else:
                return visitor.visitChildren(self)




    def returnStat(self):

        localctx = RegExpParser.ReturnStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_returnStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(RegExpParser.T__1)
            self.state = 22
            self.exp()
            self.state = 23
            self.match(RegExpParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegExpParser.RULE_exp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TamContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(RegExpParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTam" ):
                listener.enterTam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTam" ):
                listener.exitTam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTam" ):
                return visitor.visitTam(self)
            else:
                return visitor.visitChildren(self)


    class ChainContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAIN(self):
            return self.getToken(RegExpParser.CHAIN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChain" ):
                listener.enterChain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChain" ):
                listener.exitChain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChain" ):
                return visitor.visitChain(self)
            else:
                return visitor.visitChildren(self)


    class OneOrMoreContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(RegExpParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOneOrMore" ):
                listener.enterOneOrMore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOneOrMore" ):
                listener.exitOneOrMore(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOneOrMore" ):
                return visitor.visitOneOrMore(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(RegExpParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class MaybeContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(RegExpParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaybe" ):
                listener.enterMaybe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaybe" ):
                listener.exitMaybe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaybe" ):
                return visitor.visitMaybe(self)
            else:
                return visitor.visitChildren(self)


    class PrefixContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(RegExpParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefix" ):
                listener.enterPrefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefix" ):
                listener.exitPrefix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefix" ):
                return visitor.visitPrefix(self)
            else:
                return visitor.visitChildren(self)


    class TamMinContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(RegExpParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTamMin" ):
                listener.enterTamMin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTamMin" ):
                listener.exitTamMin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTamMin" ):
                return visitor.visitTamMin(self)
            else:
                return visitor.visitChildren(self)


    class ConcatContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(RegExpParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcat" ):
                listener.enterConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcat" ):
                listener.exitConcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat" ):
                return visitor.visitConcat(self)
            else:
                return visitor.visitChildren(self)


    class SuffixContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(RegExpParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuffix" ):
                listener.enterSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuffix" ):
                listener.exitSuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuffix" ):
                return visitor.visitSuffix(self)
            else:
                return visitor.visitChildren(self)


    class AnyContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny" ):
                listener.enterAny(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny" ):
                listener.exitAny(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAny" ):
                return visitor.visitAny(self)
            else:
                return visitor.visitChildren(self)


    class VarExpContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(RegExpParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarExp" ):
                listener.enterVarExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarExp" ):
                listener.exitVarExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarExp" ):
                return visitor.visitVarExp(self)
            else:
                return visitor.visitChildren(self)


    class ContainsContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(RegExpParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContains" ):
                listener.enterContains(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContains" ):
                listener.exitContains(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContains" ):
                return visitor.visitContains(self)
            else:
                return visitor.visitChildren(self)


    class ZeroOrMoreContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(RegExpParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterZeroOrMore" ):
                listener.enterZeroOrMore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitZeroOrMore" ):
                listener.exitZeroOrMore(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitZeroOrMore" ):
                return visitor.visitZeroOrMore(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegExpParser.ExpContext)
            else:
                return self.getTypedRuleContext(RegExpParser.ExpContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class EmptyStringContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyString" ):
                listener.enterEmptyString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyString" ):
                listener.exitEmptyString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyString" ):
                return visitor.visitEmptyString(self)
            else:
                return visitor.visitChildren(self)


    class NestedEXPContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(RegExpParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNestedEXP" ):
                listener.enterNestedEXP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNestedEXP" ):
                listener.exitNestedEXP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNestedEXP" ):
                return visitor.visitNestedEXP(self)
            else:
                return visitor.visitChildren(self)


    class TamMaxContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(RegExpParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTamMax" ):
                listener.enterTamMax(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTamMax" ):
                listener.exitTamMax(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTamMax" ):
                return visitor.visitTamMax(self)
            else:
                return visitor.visitChildren(self)



    def exp(self):

        localctx = RegExpParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = RegExpParser.EmptyStringContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(RegExpParser.T__2)
                self.state = 26
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 2:
                localctx = RegExpParser.NestedEXPContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(RegExpParser.T__2)
                self.state = 28
                self.exp()
                self.state = 29
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 3:
                localctx = RegExpParser.ChainContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(RegExpParser.CHAIN)
                pass

            elif la_ == 4:
                localctx = RegExpParser.AnyContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.match(RegExpParser.T__4)
                self.state = 33
                self.match(RegExpParser.T__2)
                self.state = 34
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 5:
                localctx = RegExpParser.ZeroOrMoreContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 35
                self.match(RegExpParser.T__5)
                self.state = 36
                self.match(RegExpParser.T__2)
                self.state = 37
                self.exp()
                self.state = 38
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 6:
                localctx = RegExpParser.OneOrMoreContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 40
                self.match(RegExpParser.T__6)
                self.state = 41
                self.match(RegExpParser.T__2)
                self.state = 42
                self.exp()
                self.state = 43
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 7:
                localctx = RegExpParser.MaybeContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 45
                self.match(RegExpParser.T__7)
                self.state = 46
                self.match(RegExpParser.T__2)
                self.state = 47
                self.exp()
                self.state = 48
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 8:
                localctx = RegExpParser.OrContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 50
                self.match(RegExpParser.T__8)
                self.state = 51
                self.match(RegExpParser.T__2)
                self.state = 52
                self.exp()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 53
                    self.match(RegExpParser.T__9)
                    self.state = 54
                    self.exp()
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 60
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 9:
                localctx = RegExpParser.AndContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 62
                self.match(RegExpParser.T__10)
                self.state = 63
                self.match(RegExpParser.T__2)
                self.state = 64
                self.exp()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 65
                    self.match(RegExpParser.T__9)
                    self.state = 66
                    self.exp()
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 72
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 10:
                localctx = RegExpParser.ConcatContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 74
                self.match(RegExpParser.T__11)
                self.state = 75
                self.match(RegExpParser.T__2)
                self.state = 76
                self.exp()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 77
                    self.match(RegExpParser.T__9)
                    self.state = 78
                    self.exp()
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 84
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 11:
                localctx = RegExpParser.ContainsContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 86
                self.match(RegExpParser.T__12)
                self.state = 87
                self.match(RegExpParser.T__2)
                self.state = 88
                self.exp()
                self.state = 89
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 12:
                localctx = RegExpParser.TamContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 91
                self.match(RegExpParser.T__13)
                self.state = 92
                self.match(RegExpParser.T__2)
                self.state = 93
                self.match(RegExpParser.INT)
                self.state = 94
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 13:
                localctx = RegExpParser.TamMinContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 95
                self.match(RegExpParser.T__14)
                self.state = 96
                self.match(RegExpParser.T__2)
                self.state = 97
                self.match(RegExpParser.INT)
                self.state = 98
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 14:
                localctx = RegExpParser.TamMaxContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 99
                self.match(RegExpParser.T__15)
                self.state = 100
                self.match(RegExpParser.T__2)
                self.state = 101
                self.match(RegExpParser.INT)
                self.state = 102
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 15:
                localctx = RegExpParser.PrefixContext(self, localctx)
                self.enterOuterAlt(localctx, 15)
                self.state = 103
                self.match(RegExpParser.T__16)
                self.state = 104
                self.match(RegExpParser.T__2)
                self.state = 105
                self.exp()
                self.state = 106
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 16:
                localctx = RegExpParser.SuffixContext(self, localctx)
                self.enterOuterAlt(localctx, 16)
                self.state = 108
                self.match(RegExpParser.T__17)
                self.state = 109
                self.match(RegExpParser.T__2)
                self.state = 110
                self.exp()
                self.state = 111
                self.match(RegExpParser.T__3)
                pass

            elif la_ == 17:
                localctx = RegExpParser.VarExpContext(self, localctx)
                self.enterOuterAlt(localctx, 17)
                self.state = 113
                self.match(RegExpParser.VAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





