from enum import Enum


# Abstract Syntax Tree Node Type
class ASTNodeType(Enum):
    # Program
    STMT_LIST = "STATEMENT LIST"

    # Statements
    ASS_STMT = "ASSIGNMENT STATEMENT"
    EXP_STMT = "EXPRESSION STATEMENT"
    CLR_STMT = "CLEAR STATEMENT"
    SEL_STMT = "SELECTION STATEMENT"
    ITR_STMT = "ITERATION STATEMENT"
    JMP_STMT = "JUMP STATEMENT"

    # Statement Components
    EO_STMT = "END OF STATEMENT"
    ID_LIST = "IDENTIFIER LIST"
    SEL_ClS = "SELECTION CLAUSE"
    ITR_CLS = "ITERATION CLAUSE"

    # Expressions
    ASS_EXP = "ASSIGNMENT EXPRESSION"
    CLN_EXP = "COLON EXPRESSION"
    BSO_EXP = "BINARY SCALAR OPERATOR EXPRESSION"
    MML_EXP = "MATRIX MULTIPLICATION EXPRESSION"
    MRD_EXP = "MATRIX RIGHT DIVISION EXPRESSION"
    MLD_EXP = "MATRIX LEFT DIVISION EXPRESSION"
    PRE_EXP = "PREFIX EXPRESSION"
    PST_EXP = "POSTFIX EXPRESSION"
    PRI_EXP = "PRIMARY EXPRESSION"
    ARR_EXP = "ARRAY EXPRESSION"

    # Primary
    IDENTIFIER = "IDENTIFIER"
    NUMBER_LIT = "NUMBER LITERAL"
    STRING_LIT = "STRING LITERAL"
    VECTOR_LIT = "CHAR ARRAY LITERAL"
    ARRAY_LIST = "ARRAY LIST"
    INDEX_LIST = "INDEX LIST"
