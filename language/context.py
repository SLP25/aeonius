class Context():
    next_var = 0

    stdlib_symbols = {
        "*": "times",
        "+": "plus",
        "++": "plusplus",
        "-": "minus",
        "/": "div",
        "%": "mod",
        "<": "lt",
        "=": "eq",
        "==": "eqeq",
        "<=": "lteq",
        ">=": "gteq",
        ">": "gt",
        "><": "gtlt",
        "<>": "ltgt",
        "$": "dollar",
        "^": "xor",
        ".": "dot",
        "&": "nd",
        "&&": "ndnd",
        "||": "ouou",
        "|": "ou",
        "!": "excl",
        "?": "inter",
        "\\": "bcksl",
        ".": "dot",
        "abs": "abs",
        "ae_filter": "ae_filter",
        "ae_map": "ae_map",
        "ascii": "ascii",
        "dup": "dup",
        "flip": "flip",
        "fst": "fst",
        "get": "get",
        "head": "head",
        "id": "id",
        "is_number": "is_number",
        "length": "length",
        "maximum": "maximum",
        "minimum": "minimum",
        "negate": "negate", 
        "snd": "snd",      
        "tail": "tail",
        "uncurry": "uncurry",
    }

    def __init__(self, function_name="", arg_name="", parent=None):
        self.parent = parent
        self.symbols = {} if parent is None else parent.symbols.copy()
        self.function_name = function_name
        self.arg_name = arg_name

    def in_global_scope(self):
        return self.parent is None

    def next_variable(self):
        result = f"var_{Context.next_var}"
        Context.next_var += 1
        return result

