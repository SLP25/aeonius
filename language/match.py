from .element import Element
from .context import Context
from .expression import Expression
from typing import List, Tuple

class Match(Element):
    pass


class MultiCondMatch(Match):
    def __init__(self, matches: List[Tuple[Expression, Match]]):
        self.matches = matches

    def validate(self, context):
        return True
    
    def to_python(self, context: Context) -> str:
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, MultiCondMatch):
            return False
        
        return self.matches == obj.matches

class MatchFunctionBody(Match):
    def __init__(self, body):
        self.body = body

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, MatchFunctionBody):
            return False
        
        return self.body == obj.body
    
class MatchExpression(Match):
    def __init__(self, body: Expression):
        self.body = body

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, MatchExpression):
            return False
        
        return self.body == obj.body
    
class MatchCondition(Match):
    def __init__(self, body: MultiCondMatch):
        self.body = body

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, MatchCondition):
            return False
        
        return self.body == obj.body