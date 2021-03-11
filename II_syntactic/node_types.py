from enum import Enum


# Abstract Syntax Tree Node Type
class ASTNodeType(Enum):
    PROGRAM = "PROGRAM"

    # Statements
    DCL_STMT = "DECLARATION STATEMENT"
    ASS_STMT = "ASSIGNMENT STATEMENT"
    EXP_STMT = "EXPRESSION STATEMENT"

    # Expressions
    LOR_EXP = "LOGIC OR EXPRESSION"
    LAN_EXP = "LOGIC AND EXPRESSION"
    EQL_EXP = "EQUAL EXPRESSION"
    REL_EXP = "RELATIONAL EXPRESSION"
    ADD_EXP = "ADDITIVE EXPRESSION"
    MUL_EXP = "MULTIPLICATIVE EXPRESSION"
    UNY_EXP = "UNARY EXPRESSION"
    PRI_EXP = "PRIMARY EXPRESSION"

    # Literals
    NUM_LIT = "NUMBER LITERAL"

    ID = "IDENTIFIER"
