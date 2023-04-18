import ply.yacc as yacc

from tokenizer import get_lexer, tokens

precedence = [
    ("left", "IF", "ELSE"),
    ("left", "LESSTHAN", "LESSTHANOREQUAL", "EQUALS", "GREATERTHAN", "GREATERTHANOREQUAL"),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIV", "MOD"),
    ("left", "OPENROUNDPAR", "CLOSEROUNDPAR"),
    ("left", "OPENSQUAREBRAC", "CLOSESQUAREBRAC", "OPENCURLYBRAC", "CLOSECURLYBRAC")
]

def p_grammar_empty(v):
    "grammar : "
    v[0] = ""

def p_grammar_python(v):
    "grammar : PYTHONCODE grammar"
    v[0] = v[1] + "\n" + v[2]

def p_grammar_aeonius(v):
    "grammar : aeonius grammar"
    v[0] = v[1] + v[2]

def p_aeonius(v):
    "aeonius : BEGIN code END"
    v[0] = v[2]

def p_code_empty(v):
    "code : "
    v[0] = ""

def p_code_comment(v):
    "code : COMMENT code"
    v[0] = v[2]

def p_code_lambda(v):
    "code : lambda code"
    v[0] = v[1] + "\n" + v[2]

def p_lambda(v):
    "lambda : IDENTIFIER ASSIGN expression"
    v[0] = f"{v[1]} = {v[3]}"

def p_expression_int(v):
    "expression : INTEGER"
    v[0] = str(v[1])

def p_expression_float(v):
    "expression : FLOAT"
    v[0] = str(v[1])

def p_expression_string(v):
    "expression : STRING"
    v[0] = v[1]

def p_expression_identifier(v):
    "expression : IDENTIFIER"
    v[0] = v[1]

def p_expression_sum(v):
    "expression : sum"
    v[0] = v[1]

def p_expression_diff(v):
    "expression : diff"
    v[0] = v[1]

def p_expression_mult(v):
    "expression : mult"
    v[0] = v[1]

def p_expression_div(v):
    "expression : div"
    v[0] = v[1]

def p_expression_mod(v):
    "expression : mod"
    v[0] = v[1]

def p_expression_par(v):
    "expression : OPENROUNDPAR expression CLOSEROUNDPAR"
    v[0] = f"({v[2]})"

def p_expression_less(v):
    "expression : less"
    v[0] = v[1]

def p_expression_less_equal(v):
    "expression : lesseq"
    v[0] = v[1]

def p_expression_equal(v):
    "expression : eq"
    v[0] = v[1]

def p_expression_greater(v):
    "expression : gt"
    v[0] = v[1]

def p_expression_greater_equal(v):
    "expression : gteq"
    v[0] = v[1]

def p_less(v):
    "less : expression LESSTHAN expression"
    v[0] = f"({v[1]} < {v[3]})"

def p_lesseq(v):
    "lesseq : expression LESSTHANOREQUAL expression"
    v[0] = f"({v[1]} <= {v[3]})"

def p_eq(v):
    "eq : expression EQUALS expression"
    v[0] = f"({v[1]} == {v[3]})"

def p_gt(v):
    "gt : expression GREATERTHAN expression"
    v[0] = f"({v[1]} > {v[3]})"

def p_gteq(v):
    "gteq : expression GREATERTHANOREQUAL expression"
    v[0] = f"({v[1]} >= {v[3]})"

def p_sum(v):
    "sum : expression PLUS expression"
    v[0] = f"({v[1]} + {v[3]})"

def p_diff(v):
    "diff : expression MINUS expression"
    v[0] = f"({v[1]} - {v[3]})"

def p_mult(v):
    "mult : expression TIMES expression"
    v[0] = f"({v[1]} * {v[3]})"

def p_div(v):
    "div : expression DIV expression"
    v[0] = f"({v[1]} / {v[3]})"

def p_mod(v):
    "mod : expression MOD expression"
    v[0] = f"({v[1]} % {v[3]})"

def p_expression_if(v):
    "expression : if"
    v[0] = v[1]

def p_if(v):
    "if : expression IF expression ELSE expression"
    v[0] = f"{v[1]} if ({v[3]}) else ({v[5     ]})"

def p_error(v):
    print(v)
    print("Batata")


def parse(st):
    lexer = get_lexer()
    parser = yacc.yacc(debug=True)

    return parser.parse(st)