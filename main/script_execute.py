import os
from main.I_lexical.lexer import lexer
from main.I_lexical.token import TokenListPrinter
from main.II_syntactic.parser import Parser
from main.II_syntactic.node import ASTTreePrinter
from main.III_semantic.interpreter import Interpreter
from main.exceptions.interpret_exception import *


def script_execute(path, print_tokens=False, print_ast=False, print_var=False):
    """
    path: relative path from current working directory to the script
    print_tokens: whether to print lexical analysis result or not
    print_ast: whether to print syntactic analysis result or not
    print_var: whether to print executing result or not
    """
    with open(path, "r") as file:
        program = file.read()

    try:
        # lexical analysis
        token_list = lexer(program)
        if print_tokens:
            TokenListPrinter.print(token_list)

        # syntactic analysis
        ast_root = Parser(token_list).parse_statement_list()
        interpreter = Interpreter()
        if print_ast:
            ASTTreePrinter().print(ast_root)

        # semantic analysis and execution
        interpreter.interpret_statement_list(ast_root)
        if print_var:
            print(interpreter.get_variables())
    except SemanticException as e:
        print(e)
        print(f"Error in {path[:-2].split('/')[-1]} (line {e.line})")
    except (LexicalException, SyntacticException) as e:
        {
            'darwin': lambda p: print(os.getcwd() + '/' + p),
            'win32': lambda p: print(os.getcwd() + '\\' + p.replace('/', '\\'), end=' ')
        }[sys.platform](path)
        print(e, end='')


if __name__ == "__main__":
    script_execute("../test_interpreter/test_cases/error_handling/iii_semantic_error/test_10_vertcat_matrix.m")
