class Context():
    next_var = 0

    #TODO: Refactor this to be a lot nicer
    stdlib_symbols = {
        "." : "dot",
        "length": "length",
        "ae_filter": "ae_filter",
        "ae_map": "ae_map",
        "id": "id",
        "fst": "fst",
        "snd": "snd",
        "head": "head",
        "tail": "tail",
        "negate": "negate",
        "flip": "flip",
        "is_number": "is_number",
        "ascii": "ascii",
        "dup": "dup",
        "abs": "abs"
    }

    def __init__(self, function_name="", arg_name="", parent=None):
        self.parent = parent
        self.symbols = {} if parent is None else parent.symbols
        self.function_name = function_name
        self.arg_name = arg_name

    def in_global_scope(self):
        return self.parent is None

    def next_variable(self):
        result = f"var_{Context.next_var}"
        Context.next_var += 1
        return result
