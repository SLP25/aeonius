from .element import Element
from .pattern import Pattern
from .expression import Expression
from .context import Context
from typing import List

class Match(Element):
    def __init__(self, patterns: List[Pattern], expression: Expression):
        self.patterns = patterns
        self.expression = expression

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, Match):
            return False
        
        return self.patterns == obj.patterns and self.expression == obj.expression