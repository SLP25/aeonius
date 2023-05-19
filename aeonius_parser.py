from grammar_rules import *
import ply.yacc as yacc

from tokenizer import MyLexer

tokens = MyLexer.tokens()

# TODO: INDENT, UNDENT, DO, LEFTARROW, PYTHONCODE, BEGIN, END
precedence = [
    ("nonassoc", "EOL"),
    ("nonassoc", '=', "DEF", "OP"),
    ("right", "RIGHTARROW", '|'),
    ("nonassoc", "RESULTARROW"),
    ("left", ','),
    ("left", ':'),
    ("nonassoc", "FOR", "IN", "IF", "ELSE"),
    ("left", "OPIDENT_L1"), #                   == != < > <= >=
    ("right", "OPIDENT_R1"),
    ("left", "OPIDENT_L2"), #                   || && | &
    ("right", "OPIDENT_R2"),
    ("nonassoc", "OPIDENT"), #                  unspecified
    ("left", "OPIDENT_L3"), #                   + -
    ("right", "OPIDENT_R3"),
    ("left", "OPIDENT_L4", "UNPACKITER"), #     * / %
    ("right", "OPIDENT_R4"),
    ("left", "OPIDENT_L5", "UNPACKDICT"), #     **
    ("right", "OPIDENT_R5"),
    ("nonassoc", "PRIMITIVE", "INTEGER", "FLOAT", "STRING",
     "TRUE", "FALSE", "NONE", '_', "IDENTIFIER"),
    ("left", '[', ']', '{', '}'),
    ("left", '(', ')'),
    ("left", "FUNC"),
]


def p_error(v):
    if v == None:
        print("yacc: unexpected end of file")
    else:
        print(
            f"yacc: '{v.type}' not expected at line {v.lineno}, column {v.columnno}")


def parse(st):
    parser = yacc.yacc(debug=True)
    return parser.parse(st, lexer=MyLexer())
