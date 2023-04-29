import sys
import itertools
from ply import yacc, lex
import grammar_rules
import inspect

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

with open("grammar_specification.md", "r") as f:
    s = f.read()

# Tokenize
#lexer.input(s)
#while tok := lexer.token():
#    print(tok)

grammar = parser.parse(s)
output = "from language import *\n"

for name, rules in grammar.items():
    for i, rule in zip(itertools.count(1), rules):
        funcname = f"p_{name}_{i}"
        description = f'"{name} : {rule}"'
        semantic = 'v[0] = "ok"'

        if func := getattr(grammar_rules, funcname, None):
            lines = inspect.getsource(func).split('\n', 2)
            if description == lines[1].strip():
                semantic = lines[2].strip()

        output += f"""
def {funcname}(v):
    {description}
    {semantic}
"""

with open("grammar_rules.py", "w") as f:
    f.write(output)