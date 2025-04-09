# Generated from RegExp.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RegExpParser import RegExpParser
else:
    from RegExpParser import RegExpParser

# This class defines a complete listener for a parse tree produced by RegExpParser.
class RegExpListener(ParseTreeListener):

    # Enter a parse tree produced by RegExpParser#prog.
    def enterProg(self, ctx:RegExpParser.ProgContext):
        pass

    # Exit a parse tree produced by RegExpParser#prog.
    def exitProg(self, ctx:RegExpParser.ProgContext):
        pass


    # Enter a parse tree produced by RegExpParser#stat.
    def enterStat(self, ctx:RegExpParser.StatContext):
        pass

    # Exit a parse tree produced by RegExpParser#stat.
    def exitStat(self, ctx:RegExpParser.StatContext):
        pass


    # Enter a parse tree produced by RegExpParser#returnStat.
    def enterReturnStat(self, ctx:RegExpParser.ReturnStatContext):
        pass

    # Exit a parse tree produced by RegExpParser#returnStat.
    def exitReturnStat(self, ctx:RegExpParser.ReturnStatContext):
        pass


    # Enter a parse tree produced by RegExpParser#emptyString.
    def enterEmptyString(self, ctx:RegExpParser.EmptyStringContext):
        pass

    # Exit a parse tree produced by RegExpParser#emptyString.
    def exitEmptyString(self, ctx:RegExpParser.EmptyStringContext):
        pass


    # Enter a parse tree produced by RegExpParser#nestedEXP.
    def enterNestedEXP(self, ctx:RegExpParser.NestedEXPContext):
        pass

    # Exit a parse tree produced by RegExpParser#nestedEXP.
    def exitNestedEXP(self, ctx:RegExpParser.NestedEXPContext):
        pass


    # Enter a parse tree produced by RegExpParser#chain.
    def enterChain(self, ctx:RegExpParser.ChainContext):
        pass

    # Exit a parse tree produced by RegExpParser#chain.
    def exitChain(self, ctx:RegExpParser.ChainContext):
        pass


    # Enter a parse tree produced by RegExpParser#any.
    def enterAny(self, ctx:RegExpParser.AnyContext):
        pass

    # Exit a parse tree produced by RegExpParser#any.
    def exitAny(self, ctx:RegExpParser.AnyContext):
        pass


    # Enter a parse tree produced by RegExpParser#zeroOrMore.
    def enterZeroOrMore(self, ctx:RegExpParser.ZeroOrMoreContext):
        pass

    # Exit a parse tree produced by RegExpParser#zeroOrMore.
    def exitZeroOrMore(self, ctx:RegExpParser.ZeroOrMoreContext):
        pass


    # Enter a parse tree produced by RegExpParser#oneOrMore.
    def enterOneOrMore(self, ctx:RegExpParser.OneOrMoreContext):
        pass

    # Exit a parse tree produced by RegExpParser#oneOrMore.
    def exitOneOrMore(self, ctx:RegExpParser.OneOrMoreContext):
        pass


    # Enter a parse tree produced by RegExpParser#maybe.
    def enterMaybe(self, ctx:RegExpParser.MaybeContext):
        pass

    # Exit a parse tree produced by RegExpParser#maybe.
    def exitMaybe(self, ctx:RegExpParser.MaybeContext):
        pass


    # Enter a parse tree produced by RegExpParser#or.
    def enterOr(self, ctx:RegExpParser.OrContext):
        pass

    # Exit a parse tree produced by RegExpParser#or.
    def exitOr(self, ctx:RegExpParser.OrContext):
        pass


    # Enter a parse tree produced by RegExpParser#and.
    def enterAnd(self, ctx:RegExpParser.AndContext):
        pass

    # Exit a parse tree produced by RegExpParser#and.
    def exitAnd(self, ctx:RegExpParser.AndContext):
        pass


    # Enter a parse tree produced by RegExpParser#concat.
    def enterConcat(self, ctx:RegExpParser.ConcatContext):
        pass

    # Exit a parse tree produced by RegExpParser#concat.
    def exitConcat(self, ctx:RegExpParser.ConcatContext):
        pass


    # Enter a parse tree produced by RegExpParser#contains.
    def enterContains(self, ctx:RegExpParser.ContainsContext):
        pass

    # Exit a parse tree produced by RegExpParser#contains.
    def exitContains(self, ctx:RegExpParser.ContainsContext):
        pass


    # Enter a parse tree produced by RegExpParser#tam.
    def enterTam(self, ctx:RegExpParser.TamContext):
        pass

    # Exit a parse tree produced by RegExpParser#tam.
    def exitTam(self, ctx:RegExpParser.TamContext):
        pass


    # Enter a parse tree produced by RegExpParser#tamMin.
    def enterTamMin(self, ctx:RegExpParser.TamMinContext):
        pass

    # Exit a parse tree produced by RegExpParser#tamMin.
    def exitTamMin(self, ctx:RegExpParser.TamMinContext):
        pass


    # Enter a parse tree produced by RegExpParser#tamMax.
    def enterTamMax(self, ctx:RegExpParser.TamMaxContext):
        pass

    # Exit a parse tree produced by RegExpParser#tamMax.
    def exitTamMax(self, ctx:RegExpParser.TamMaxContext):
        pass


    # Enter a parse tree produced by RegExpParser#prefix.
    def enterPrefix(self, ctx:RegExpParser.PrefixContext):
        pass

    # Exit a parse tree produced by RegExpParser#prefix.
    def exitPrefix(self, ctx:RegExpParser.PrefixContext):
        pass


    # Enter a parse tree produced by RegExpParser#suffix.
    def enterSuffix(self, ctx:RegExpParser.SuffixContext):
        pass

    # Exit a parse tree produced by RegExpParser#suffix.
    def exitSuffix(self, ctx:RegExpParser.SuffixContext):
        pass


    # Enter a parse tree produced by RegExpParser#varExp.
    def enterVarExp(self, ctx:RegExpParser.VarExpContext):
        pass

    # Exit a parse tree produced by RegExpParser#varExp.
    def exitVarExp(self, ctx:RegExpParser.VarExpContext):
        pass



del RegExpParser