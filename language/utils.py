from typing import List, Tuple

def concat(list):
    res = []

    for l in list:
        res += l

    return res

def ident_str(str, level=4):
    lines = str.splitlines()
    return "\n".join(map(lambda s: (" " * level) + s, lines))

def pipe_validate(values: List[Tuple[bool, List[str]]]) -> Tuple[bool, List[str]]:
    return not any(map(lambda v: not v[0], values)), concat(list(map(lambda v: v[1], values)))

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
