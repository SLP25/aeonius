class Context():
    next_var = 0
    def __init__(self, parent = None):
        self.parent = parent
        self.symbols = {}

    def in_global_scope(self):
        return self.parent is None
    
    def next_variable(self):
        result = f"var_{Context.next_var}"
        Context.next_var += 1
        return result