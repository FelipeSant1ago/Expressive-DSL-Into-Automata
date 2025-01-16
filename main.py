import sys
from antlr4 import *
from RegExpLexer import RegExpLexer
from RegExpParser import RegExpParser
from MyVisitor import MyVisitor
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from helper_functions import *


def main(argv):
    #Reads the input
    istream = FileStream(argv[1])
    
    #Creates a Lexer that feeds off the input
    lexer = RegExpLexer(istream)

    #Creates a buffer of tokens pulled from the lexer
    stream = CommonTokenStream(lexer)

    #Creates a parser  feeds off the token buffer
    parser = RegExpParser(stream)

    #Begin parsing from the init rule
    tree = parser.prog()

    #Print the tree
    # print(tree.toStringTree(recog=parser))
    # print("==========================")

    #Execute listener
    # walker = ParseTreeWalker()
    # walker.walk(MyListener(), tree)
    # print()

    #Execute visitor
    visitor = MyVisitor()
    expression = visitor.visit(tree)
    dfa1 = regular_expression_into_dfa(expression)
    # print(dfa1)
    # print("==========================")
    automataDefinitionInput = parse_file(2)
    dfa2 = DFA.from_nfa(parse_nfa(automataDefinitionInput))
    # print(dfa2)
    write_dfa_to_file(dfa1,"output.txt")
    equivalence = check_dfa_equivalence(dfa1,dfa2)
    if equivalence == True:
        print("A expressão regular especificada pela DSL é equivalente ao autômato fornecido")
    else:
        print("A expressão regular especificada pela DSL não é equivalente ao autômato fornecido")

   

if __name__ == '__main__':
    main(sys.argv)