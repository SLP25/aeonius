import ply.lex as lex

reserved = {
    'def': 'DEF',
   'if' : 'IF',
   'else' : 'ELSE',
   'for' : 'FOR',
   'in': "IN",
   'op': "OP",
   'lambda': "LAMBDA",
   'None': "NONE",
   'True': "TRUE",
   'False': "FALSE",
   'where': "WHERE",
   'do': "DO",
   'return': "RETURN"
}


tokens = [
    'IDENTIFIER',
    'COLON',
    'INTEGER',
    'FLOAT',
    'LEFTARROW',
    'RIGHTARROW',
    'COMMENT',
    'BEGIN',
    'END',
    'UNDERSCORE',
    'DIV',
    'PIPE',
    'MOD',
    'ASSIGN',
    'EQUALS',
    'LESSTHAN',
    'LESSTHANOREQUAL',
    'GREATERTHAN',
    'GREATERTHANOREQUAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'OPENROUNDPAR',
    'CLOSEROUNDPAR',
    'OPENSQUAREBRAC',
    'CLOSESQUAREBRAC',
    'OPENCURLYBRAC',
    'CLOSECURLYBRAC',
    'COMMA',
    'KEYARGS',
    'DOUBLEQUOTE',
    'SINGLEQUOTE',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS   = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIV  = r'/'
t_MOD = r'%'
t_COLON = r':'
t_LEFTARROW = r'<-'
t_RIGHTARROW = r'->'
t_COMMENT = r'\#.*'
t_UNDERSCORE = r'_'
t_PIPE = r'\|'
t_ASSIGN = r'='
t_EQUALS = r'=='
t_LESSTHAN = r'<'
t_LESSTHANOREQUAL = r'<='
t_GREATERTHAN = r'>'
t_GREATERTHANOREQUAL = r'>='
t_OPENROUNDPAR = r'\('
t_CLOSEROUNDPAR = r'\)'
t_OPENCURLYBRAC = r'\{'
t_CLOSECURLYBRAC = r'\}'
t_OPENSQUAREBRAC = r'\['
t_CLOSESQUAREBRAC = r'\]'
t_COMMA = r','
t_KEYARGS = r'\*\*'
t_DOUBLEQUOTE = r'"'
t_SINGLEQUOTE = r"'"

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t

def t_BEGIN(t):
    r'"""Aeonius'
    return t

def t_END(t):
    r'"""'
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+.\d+'
    t.value = float(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)


def tokenize(data):
    # Build the lexer
    lexer = lex.lex()

    # Give the lexer some input
    lexer.input(data)

    res = []

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        res = res + [tok]

    return res


with open("examples/aeonius_spec_no_python", "r") as f:
    data = f.read()

# data = """
# \"\"\"Aeonius

# #definição de funções (pattern match, underscore)
# def f:
#     0 -> _ -> 0
#     x -> 0 -> 1000000
#          y -> x / y
# """

print(tokenize(data))