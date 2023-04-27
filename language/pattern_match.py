from .element import Element
from .match import Match
from .context import Context
from typing import List

class PatternMatch(Element):
    def __init__(self, match: Match, other_matches: List[Match] = None):
        self.matches = [match]
        if other_matches is not None:
            for m in other_matches:
                self.matches += [m]
                
    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, PatternMatch):
            return False
        
        return self.matches == obj.matches
