def ident_str(str, level=4):
    lines = str.splitlines()
    return "\n".join(map(lambda s: (" " * level) + s, lines))