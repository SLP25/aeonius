from .element import Element
from .assignment import Assignment
from .context import Context
from typing import List

class Language(Element):
    pass


class Grammar(Element):
    def __init__(self, snippets: List[Language]):
        self.snippets = snippets

    def validate(self, context: Context):
        return True
    
    def to_python(self, context: Context):
        return "\n".join(map(lambda s: s.to_python(context), self.snippets))
    
    def __eq__(self, obj):
        return isinstance(obj, Grammar)
    
class Code(Element):
    def __init__(self, assignments: List[Assignment]):
        self.assignments = assignments

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        return "\n".join(map(lambda s: s.to_python(context), self.assignments))
    
    def __eq__(self, obj):
        if not isinstance(obj, Code):
            return False
        
        return self.assignments == obj.assignments

class Aeonius(Language):
    def __init__(self, code: Code):
        self.code = code
    
    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        return self.code.to_python(context)
    
    def __eq__(self, obj):
        if not isinstance(obj, Aeonius):
            return False
        
        return self.code == obj.code
    
class Python(Language):
    def __init__(self, code: str):
        self.code = code
    
    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        return self.code
    
    def __eq__(self, obj):
        if not isinstance(obj, Python):
            return False
        
        return self.code == obj.code