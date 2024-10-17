import sys
from antlr4 import *
from FourierLexer import FourierLexer
from FourierParser import FourierParser
from FourierDFTVisitor import FourierDFTVisitor 

def main():
    try:
        input_stream = FileStream("programa_fourier.txt")  # File containing the program
        lexer = FourierLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = FourierParser(stream)

        # Parse the program starting from the top-level rule
        tree = parser.prog()  
        visitor = FourierDFTVisitor()  # Create the visitor
        visitor.visit(tree)  # Visit the syntax tree and execute

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
