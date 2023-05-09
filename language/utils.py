def ident_str(str, level=4):
    lines = str.splitlines()
    return "\n".join(map(lambda s: (" " * level) + s, lines))


def clean_identifier(identifier: str):
    replacement_table = {
        "*": "times",
        "+": "plus",
        "-": "minus",
        "/": "div",
        "%": "mod",
        "<": "lt",
        "=": "eq",
        ">": "gt",
        "$": "dollar",
        "^": "power",
        ".": "dot",
        "&": "nd",
        "|": "ou",
        "!": "excl"
    }

    for key in replacement_table.keys():
        identifier = identifier.replace(key, replacement_table[key])

    return identifier


def return_name(name):
    return f"return_{name}"
