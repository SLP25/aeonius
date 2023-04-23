import ply.yacc as yacc

from tokenizer import get_lexer, tokens

precedence = [
    ("nonassoc", "EOL"),
    ("nonassoc", '=', "DEF", "OP"),
    ("right", 'RIGHTARROW'),
    #("left", '|'),
    ("left", ','),
    ("left", ':'),
    ("left", "FOR", "IN", "IF", "ELSE"), #TODO: ?
    ("left", "OPIDENTIFIER"),   #TODO: different precedences/associativitites
    ("nonassoc", "IDENTIFIER", "INTEGER", "FLOAT", "STRING", "UNDERSCORE"),
    ("left", '[', ']', '{', '}'),
    ("left", '(', ')'),
    
]

from grammar_rules import *

def p_error(v):
    print(f"Erro sintático no input {v}")


def parse(st):
    lexer = get_lexer()
    parser = yacc.yacc(debug=True)

    return parser.parse(st)