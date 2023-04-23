import ply.lex as lex

states = (
   ('python','exclusive'),
   ('aeonius','inclusive'),
)

reserved = {
    "def": "DEF",
    "if": "IF",
    "else": "ELSE",
    "for": "FOR",
    "in": "IN",
    "op": "OP",
    "lambda": "LAMBDA",
    #"None": "NONE",
    #"True": "TRUE",
    #"False": "FALSE",
    "where": "WHERE",
    "do": "DO",
    "return": "RETURN",
}

literals = ":|=()[]{},_"

tokens = [
    "IDENTIFIER",
    "OPIDENTIFIER",
    "INTEGER",
    "FLOAT",
    "LEFTARROW",
    "RIGHTARROW",
    "UNDERSCORE",
    #"KEYARGS",
    "STRING",
    "PYTHONCODE",
    "BEGIN",
    "END",
    "EOL",
] + list(reserved.values())

# Regular expression rules for simple tokens
#t_PLUS = r"\+"
#t_MINUS = r"-"
#t_TIMES = r"\*"
#t_DIV = r"/"
#t_MOD = r"%"
#t_EQUALS = r"=="
#t_LESSTHAN = r"<"
#t_LESSTHANOREQUAL = r"<="
#t_GREATERTHAN = r">"
#t_GREATERTHANOREQUAL = r">="

def t_ANY_EOL(t):
    r"(\n\s*(\#.*)?)+"
    t.lexer.lineno += t.value.count('\n') #so we can track line numbers
    if t.lexer.current_state() == 'aeonius':
        return t

def t_COMMENT(t):
    r"\#.*"

def t_python_BEGIN(t):
    r'"""Aeonius'
    t.lexer.begin("aeonius")
    return t

def t_python_PYTHONCODE(t):
    r".+"
    return t

def t_aeonius_END(t):
    r'"""'
    t.lexer.begin("python")
    return t

def t_INTEGER(t):
    r"-?\d+"
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r"-?\d+\.\d+"
    t.value = float(t.value)
    return t

def t_STRING(t):
    "(\"[^\"\\n]*\")|('[^'\\n]*')"
    #"([\"']).*?\\2"
    t.value = t.value.strip("\"'")
    return t

def t_LEFTARROW(t):
    r"<-"
    return t

def t_RIGHTARROW(t):
    r"->"
    return t

#TODO: unpacking (*args and **kargs)
#def t_KEYARGS(t):
#    r"\*\*"
#    return t

def t_OPIDENTIFIER(t):
    r"[\+\-\*/%<=>\$\^]+"
    if len(t.value) == 1 and t.value in literals:
        t.type = t.value
    return t

def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    if len(t.value) == 1 and t.value in literals:
        t.type = t.value
    else:
        t.type = reserved.get(t.value, "IDENTIFIER")  # Check for reserved words
    return t


# A string containing ignored characters (spaces and tabs)
t_aeonius_ignore = " \t"

# Error handling rule
def t_ANY_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno} (state is {t.lexer.current_state()})")
    t.lexer.skip(1)



def get_lexer():
    lexer = lex.lex()
    lexer.begin("python")
    return lexer

def tokenize(data):
    # Build the lexer
    lexer = get_lexer()
    # Give the lexer some input
    lexer.input(data)

    res = []

    # Tokenize
    while tok := lexer.token():
        res.append(tok)

    return res


with open("examples/test.txt", "r") as f:
    data = f.read()

#for x in tokenize(data):
#    print(x)
#    input()

