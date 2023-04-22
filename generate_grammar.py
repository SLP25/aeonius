import sys
import itertools
from ply import yacc, lex

literals = ["|", "ε"]
tokens = ['COMMENT', 'NAME', 'TEXT']
t_ignore = " \t\n"

def t_COMMENT(t):
    r'\#.*'

def t_pipe(t):
    r'\|'
    t.type = '|'
    return t

def t_epsilon(t):
    r'ε'
    t.type = 'ε'
    return t

def t_NAME(t):
    r'\w+\s*:'
    t.value = t.value.strip(" \t:")
    return t

def t_TEXT(t):
    r'[^\#\n]+'
    return t

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

def p_grammar1(v):
    "grammar : "
    v[0] = {}

def p_grammar2(v):
    "grammar : grammar symbol"
    v[0] = {**v[1], v[2][0]: v[2][1]}

def p_symbol(v):
    "symbol : NAME rules"
    v[0] = (v[1], v[2])

def p_rules1(v):
    "rules : rule"
    v[0] = [v[1]]

def p_rules2(v):
    "rules : rules '|' rule"
    v[0] = v[1] + [v[3]]

def p_rule1(v):
    "rule : "
    v[0] = ""

def p_rule2(v):
    "rule : 'ε'"
    v[0] = ""

def p_rule3(v):
    "rule : TEXT"
    v[0] = v[1]

def p_error(v):
    print(f"Erro sintático no input {v}")

parser = yacc.yacc()

with f as open("grammar_specification.md", "r"):
    s = f.read()

# Tokenize
#lexer.input(s)
#while tok := lexer.token():
#    print(tok)

grammar = parser.parse(s)

with f as open("grammar_rules.py", "w"):
    for name, rules in grammar.items():
        for i, rule in zip(itertools.count(1), rules):
            f.write(f"""
def p_{name}{i}(v):
    "{name} : {rule}"
    v[0] = "ok"
""")