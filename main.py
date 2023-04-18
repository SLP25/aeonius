from aeonius_parser import parse

def tokenize(data):
    # Build the lexer
    lexer = Lexer().lexer
    lexer.begin("python")
    # Give the lexer some input
    lexer.input(data)

    res = []

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        res = res + [tok]

    return res


with open("examples/test.txt", "r") as f:
    data = f.read()

#print(data)
#print(tokenize(data))
print(parse(data))