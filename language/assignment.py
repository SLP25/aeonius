from .element import Element
from .pattern import Pattern
from .expression import Expression
from .pattern_match import PatternMatch
from abc import ABC

class Assignment(Element, ABC):
    pass

class AssignmentPattern(Assignment):
    def __init__(self, pattern: Pattern, expression: Expression):
        self.pattern = pattern
        self.expression = expression

    def validate(self, context):
        return True

    def __str__(self):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, AssignmentPattern):
            return False
        
        return self.pattern == obj.pattern and self.expression == obj.expression
    

class AssignmentDefinition(Assignment):
    def __init__(self, identifier: str, patternMatch: PatternMatch):
        self.identifier = identifier
        self.patternMatch = patternMatch

    def validate(self, context):
        return True
    
    def __str__(self):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, AssignmentDefinition):
            return False
        
        return self.identifier == obj.identifier and self.patternMatch == obj.patternMatch
    

class AssignmentOperator(Assignment):
    def __init__(self, identifier: str, patternMatch: PatternMatch):
        self.identifier = identifier
        self.patternMatch = patternMatch

    def validate(self, context):
        return True
    
    def __str__(self):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, AssignmentOperator):
            return False
        
        return self.identifier == obj.identifier and self.patternMatch == obj.patternMatch