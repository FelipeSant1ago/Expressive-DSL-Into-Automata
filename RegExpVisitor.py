# Generated from RegExp.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RegExpParser import RegExpParser
else:
    from RegExpParser import RegExpParser

# This class defines a complete generic visitor for a parse tree produced by RegExpParser.

class RegExpVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RegExpParser#prog.
    def visitProg(self, ctx:RegExpParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#stat.
    def visitStat(self, ctx:RegExpParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#returnStat.
    def visitReturnStat(self, ctx:RegExpParser.ReturnStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#emptyString.
    def visitEmptyString(self, ctx:RegExpParser.EmptyStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#nestedEXP.
    def visitNestedEXP(self, ctx:RegExpParser.NestedEXPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#chain.
    def visitChain(self, ctx:RegExpParser.ChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#any.
    def visitAny(self, ctx:RegExpParser.AnyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#zeroOrMore.
    def visitZeroOrMore(self, ctx:RegExpParser.ZeroOrMoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#oneOrMore.
    def visitOneOrMore(self, ctx:RegExpParser.OneOrMoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#maybe.
    def visitMaybe(self, ctx:RegExpParser.MaybeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#or.
    def visitOr(self, ctx:RegExpParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#and.
    def visitAnd(self, ctx:RegExpParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#concat.
    def visitConcat(self, ctx:RegExpParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#contains.
    def visitContains(self, ctx:RegExpParser.ContainsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#tam.
    def visitTam(self, ctx:RegExpParser.TamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#tamMin.
    def visitTamMin(self, ctx:RegExpParser.TamMinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#tamMax.
    def visitTamMax(self, ctx:RegExpParser.TamMaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#prefix.
    def visitPrefix(self, ctx:RegExpParser.PrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#sufix.
    def visitSufix(self, ctx:RegExpParser.SufixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#varExp.
    def visitVarExp(self, ctx:RegExpParser.VarExpContext):
        return self.visitChildren(ctx)



del RegExpParser