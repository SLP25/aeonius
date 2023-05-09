import ply.lex as lex
import bisect

states = (
    ('python', 'exclusive'),
    ('aeonius', 'inclusive'),
)

reserved = {
    "def": "DEF",
    "if": "IF",
    "else": "ELSE",
    "for": "FOR",
    "in": "IN",
    "op": "OP",
    "lambda": "LAMBDA",
    "True": "TRUE",
    "False": "FALSE",
    "None": "NONE",
    # "do": "DO",
    # "<-": "LEFTARROW",
    "->": "RIGHTARROW",
    "=>": "RESULTARROW",
    "*": "UNPACKITER",
    "**": "UNPACKDICT"
}

literals = ":|=()[]{},_"

tokens = [
    "IDENTIFIER",
    "OPIDENTIFIER",
    "INTEGER",
    "FLOAT",
    "STRING",
    "PYTHONCODE",
    "BEGIN",
    "END",
    "WS",
    "EOL",
] + list(reserved.values())


def t_ANY_EOL(t):
    r"(\s*(\#.*)?\n)+"
    t.lexer.lineno += t.value.count('\n')  # so we can track line numbers
    if t.lexer.current_state() == 'aeonius':
        return t


def t_COMMENT(t):
    r"\#.*"


def t_python_BEGIN(t):
    r'"""aeonius'
    t.lexer.begin("aeonius")
    return t


def t_python_PYTHONCODE(t):
    r'.+?(?="""aeonius|\n|$)'
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
    # "([\"']).*?\\2"
    t.value = t.value.strip("\"'")
    return t


def t_OPIDENTIFIER(t):
    r"[\+\-\*/%<=>\$\^&\|\.!?\\]+"
    if len(t.value) == 1 and t.value in literals:
        t.type = t.value
    else:
        # Check for reserved symbols
        t.type = reserved.get(t.value, "OPIDENTIFIER")
    return t


def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    if len(t.value) == 1 and t.value in literals:
        t.type = t.value
    else:
        # Check for reserved words
        t.type = reserved.get(t.value, "IDENTIFIER")
    return t


def t_WS(t):
    r"[ ]+"
    return t

# Error handling rule


def t_ANY_error(t):
    if t.value[0] == '\t':
        print(
            f"lex: '\\t' not expected at line {t.lexer.lineno}. Please indent using spaces")
    else:
        print(
            f"lex: '{t.value[0]}' not expected at line {t.lexer.lineno} (state is {t.lexer.current_state()})")
    t.lexer.skip(1)


def create_token(type, lexpos, lineno, columnno):
    tok = lex.LexToken()
    tok.type = type
    tok.value = None
    tok.lineno = lineno
    tok.columnno = columnno
    tok.lexpos = lexpos
    return tok


def add_columnno(tokens):
    line_breaks = [(1, 0)]  # (lineno, lexpos)

    for t in tokens:
        if t.lineno > line_breaks[-1][0]:
            line_breaks.append((t.lineno, t.lexpos))

        t.columnno = t.lexpos - line_breaks[-1][1] + 1
        if t.type != "WS":
            yield t


def add_indentation(tokens):
    open_scope = False
    line_start = True
    indentation = [1]  # zero indentation = column 1

    for t in tokens:
        if t.type == "EOL":
            line_start = True
            yield t
        elif t.type in ["RIGHTARROW", "RESULTARROW"]:
            if open_scope:
                raise ValueError(
                    f"Repeated arrow not allowed at line {t.lineno}, column {t.columnno}")
            if line_start:
                raise ValueError(
                    f"Illegal arrow at beginning of line at line {t.lineno}, column {t.columnno}")
            open_scope = True
            # line_start = False
            yield t
        elif t.type in ["|"] and not line_start:
            if open_scope:
                raise ValueError(f"Illegal token after arrow at line {t.lineno}, column {t.columnno}")
            yield t
            indentation.append(t.columnno)
            yield create_token("INDENT", t.lexpos, t.lineno, t.columnno)
        else:
            if open_scope:
                if t.columnno <= indentation[-1]:
                    raise ValueError(f"You must indent after arrow at line {t.lineno}, column {t.columnno}")
                indentation.append(t.columnno)
                yield create_token("INDENT", t.lexpos, t.lineno, t.columnno)
            elif line_start:
                if indentation[-1] < t.columnno:
                    indentation.append(t.columnno)
                    yield create_token("INDENT", t.lexpos, t.lineno, t.columnno)
                else:
                    while indentation[-1] > t.columnno:
                        indentation.pop()
                        yield create_token("UNDENT", t.lexpos, t.lineno, t.columnno)
                    if indentation[-1] != t.columnno:
                        raise ValueError(
                            f"Inconsistent indentation at line {t.lineno}, column {t.columnno}")

            line_start = False
            open_scope = False
            yield t

    while indentation.pop() > 1:
        yield create_token("UNDENT", -1, -1, -1)


class MyLexer:
    def __init__(self):
        self.lexer = lex.lex()
        self.lexer.begin("python")
        self.ans = iter(())

    def __inner_iter__(self):
        while t := self.lexer.token():
            yield t

    def input(self, data):
        self.lexer.input(data)
        self.ans = iter(add_indentation(add_columnno(self.__inner_iter__())))

    def token(self):
        return next(self.ans, None)

    @staticmethod
    def tokens():
        return list(set(tokens) - {"WS"}) + ["INDENT", "UNDENT"]


if __name__ == "__main__":
    lexer = MyLexer()

    with open("examples/error", "r") as f:
        lexer.input(f.read())

    while t := lexer.token():
        print(t, t.columnno)
        # input()
