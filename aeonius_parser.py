import ply.yacc as yacc

from tokenizer import MyLexer, tokens

precedence = [
    ("nonassoc", "EOL"),
    ("nonassoc", '=', "DEF", "OP"),
    ("right", 'RIGHTARROW', '|'),
    ("left", ','),
    ("left", ':'),
    ("nonassoc", "FOR", "IN", "IF", "ELSE"),
    ("left", "OPIDENTIFIER"),   #TODO: different precedences/associativities
    ("nonassoc", "IDENTIFIER", "INTEGER", "FLOAT", "STRING", "UNDERSCORE", "TRUE", "FALSE", "NONE"),
    ("left", '[', ']', '{', '}'),
    ("left", '(', ')'),
]

from grammar_rules import *

def p_error(v):
    print(f"Erro sintático no input '{v.type}' (linha {v.lineno}, coluna {v.columnno})")


def parse(st):
    parser = yacc.yacc(debug=True)
    return parser.parse(st, lexer=MyLexer())