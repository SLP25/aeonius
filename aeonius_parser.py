import ply.yacc as yacc

from tokenizer import MyLexer, tokens

#TODO: INDENT, UNDENT, DO, LEFTARROW, PYTHONCODE, BEGIN, END
precedence = [
    ("nonassoc", "EOL"),
    ("nonassoc", '=', "DEF", "OP"),
    ("right", 'RIGHTARROW', '|'),
    ("left", ','),
    ("left", ':'),
    ("nonassoc", "FOR", "IN", "IF", "ELSE"),
    ("left", "OPIDENTIFIER", "UNPACKITER", "UNPACKDICT"),   #TODO: different precedences/associativities
    ("right", "FUNC"),
    ("nonassoc", "IDENTIFIER", "INTEGER", "FLOAT", "STRING", "UNDERSCORE", "TRUE", "FALSE", "NONE"),
    ("left", '[', ']', '{', '}'),
    ("left", '(', ')'),
]

from grammar_rules import *

def p_error(v):
    if v == None:
        print("yacc: unexpected end of file")
    else:
        print(f"yacc: '{v.type}' not expected at line {v.lineno}, column {v.columnno}")


def parse(st):
    parser = yacc.yacc(debug=True)
    return parser.parse(st, lexer=MyLexer())