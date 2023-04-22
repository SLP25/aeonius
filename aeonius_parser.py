import ply.yacc as yacc

from tokenizer import get_lexer, tokens

precedence = [
    ("left", "IF", "ELSE"),
    #("left", "LESSTHAN", "LESSTHANOREQUAL", "EQUALS", "GREATERTHAN", "GREATERTHANOREQUAL"),
    #("left", "PLUS", "MINUS"),
    #("left", "TIMES", "DIV", "MOD"),
    ("left", '(', ')'),
    ("left", '[', ']', '{', '}')
]

from grammar_rules import *

def p_error(v):
    print(f"Erro sintático no input {v}")


def parse(st):
    lexer = get_lexer()
    parser = yacc.yacc(debug=True)

    return parser.parse(st)