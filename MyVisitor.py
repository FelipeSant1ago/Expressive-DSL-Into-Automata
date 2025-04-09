# Generated from RegExp.g4 by ANTLR 4.13.2
from antlr4 import *
from RegExpParser import RegExpParser
from RegExpVisitor import RegExpVisitor

# This class defines a complete generic visitor for a parse tree produced by RegExpParser.

class MyVisitor(RegExpVisitor):
    
    def __init__(self):
      self.memory = {}

    # Visit a parse tree produced by RegExpParser#prog.
    def visitProg(self, ctx:RegExpParser.ProgContext):
      self.visitChildren(ctx)
      fullExpression = self.visit(ctx.returnStat())
    #   print(fullExpression)
      return fullExpression

    # Visit a parse tree produced by RegExpParser#stat.
    def visitStat(self, ctx:RegExpParser.StatContext):
        variable = ctx.VAR().getText()
        value = self.visit(ctx.exp())
        self.memory[variable] = value
        return value
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#returnStat.
    def visitReturnStat(self, ctx:RegExpParser.ReturnStatContext):
        return self.visit(ctx.exp())


    # Visit a parse tree produced by RegExpParser#emptyString.
    def visitEmptyString(self, ctx:RegExpParser.EmptyStringContext):
        self.visitChildren(ctx)
        return "()"

    # Visit a parse tree produced by RegExpParser#nestedEXP.
    def visitNestedEXP(self, ctx:RegExpParser.NestedEXPContext):
        return '(' +  self.visit(ctx.exp()) + ')'


    # Visit a parse tree produced by RegExpParser#chain.
    def visitChain(self, ctx:RegExpParser.ChainContext):
        return ctx.CHAIN().getText()


    # Visit a parse tree produced by RegExpParser#any.
    def visitAny(self, ctx:RegExpParser.AnyContext):
        return '.'


    # Visit a parse tree produced by RegExpParser#zeroOrMore.
    def visitZeroOrMore(self, ctx:RegExpParser.ZeroOrMoreContext):
        return '(' + self.visit(ctx.exp()) + ')*'
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#oneOrMore.
    def visitOneOrMore(self, ctx:RegExpParser.OneOrMoreContext):
        return '(' + self.visit(ctx.exp()) + ')+'
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by RegExpParser#maybe.
    def visitMaybe(self, ctx:RegExpParser.MaybeContext):
        return '(' + self.visit(ctx.exp()) + ')?'
        # return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#varExp.
    def visitVarExp(self, ctx:RegExpParser.VarExpContext):
        variableId = ctx.VAR().getText()
        if variableId in self.memory:
            return self.memory[variableId]
        print(f"Variable {variableId} does not exist")
        return 0


    # Visit a parse tree produced by RegExpParser#or.
    def visitOr(self, ctx:RegExpParser.OrContext):
        finalExp = ""
        for i in range(len(ctx.exp())):
            if i == len(ctx.exp()) -1:
                finalExp += '(' + self.visit(ctx.exp(i)) +')'
            else:
                finalExp += '(' + self.visit(ctx.exp(i)) +') |'
                
        return finalExp


    # Visit a parse tree produced by RegExpParser#and.
    def visitAnd(self, ctx:RegExpParser.AndContext):
        finalExp = ""
        for i in range(len(ctx.exp())):
            if i == len(ctx.exp()) -1:
                finalExp += '(' + self.visit(ctx.exp(i)) +')'
            else:
                finalExp += '(' + self.visit(ctx.exp(i)) +') &'
                
        return finalExp


    # Visit a parse tree produced by RegExpParser#concat.
    def visitConcat(self, ctx:RegExpParser.ConcatContext):
        finalExp = ""
        for i in range(len(ctx.exp())):
          finalExp += '(' + self.visit(ctx.exp(i)) +')'
                
        return finalExp
    
     # Visit a parse tree produced by RegExpParser#contains.
    def visitContains(self, ctx:RegExpParser.ContainsContext):
        value = self.visit(ctx.exp())
        return ".*" + value + ".*"



    # Visit a parse tree produced by RegExpParser#tam.
    def visitTam(self, ctx:RegExpParser.TamContext):
        tam = int(ctx.INT().getText())
        aux = ""
        for i in range(tam):
            aux += '.'
        
        return aux



    # Visit a parse tree produced by RegExpParser#tamMin.
    def visitTamMin(self, ctx:RegExpParser.TamMinContext):
        tam = int(ctx.INT().getText())
        aux = ""
        for i in range(tam):
            aux += '.'
        aux += '.*'
        return aux


    # Visit a parse tree produced by RegExpParser#tamMax.
    def visitTamMax(self, ctx:RegExpParser.TamMaxContext):
        tam = int(ctx.INT().getText())
        aux = ""
        for i in range(tam):
            aux += '.?'
        return aux


    # Visit a parse tree produced by RegExpParser#prefix.
    def visitPrefix(self, ctx:RegExpParser.PrefixContext):
        value = self.visit(ctx.exp())
        return value  + ".*"


    # Visit a parse tree produced by RegExpParser#sufix.
    def visitSuffix(self, ctx:RegExpParser.SuffixContext):
        value = self.visit(ctx.exp())
        return ".*" + value



del RegExpParser