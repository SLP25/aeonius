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
    # TODO: different precedences/associativities
    ("left", "OPIDENTIFIER", "UNPACKITER", "UNPACKDICT"),
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
