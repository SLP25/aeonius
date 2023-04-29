from .element import Element
from .pattern import Pattern
from .expression import Expression
from .pattern_match import PatternMatch
from .utils import ident_str
from .context import Context
from abc import ABC

class Assignment(Element, ABC):
    pass

class AssignmentPattern(Assignment):
    def __init__(self, pattern: Pattern, expression: Expression):
        self.pattern = pattern
        self.expression = expression

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return f"{self.pattern.to_python(context)} = {self.expression.to_python(context)}\n"
    
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
    
    def to_python(self, context: Context):
        identifier = self.identifier if context.in_global_scope() else context.next_variable()
        new_context = Context(context)
        return f"def {identifier}:\n{ident_str(self.patternMatch.to_python(new_context))}"
    
    def __eq__(self, obj):
        if not isinstance(obj, AssignmentDefinition):
            return False
        
        return self.identifier == obj.identifier and self.patternMatch == obj.patternMatch
    

class AssignmentOperator(Assignment):
    def __init__(self, identifier: str, patternMatch: PatternMatch):
        self.identifier = identifier
        self.patternMatch = patternMatch

    @staticmethod
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
            ".": "dot"
        }

        for key in replacement_table.keys():
            identifier = identifier.replace(key, replacement_table[key])
        
        return identifier

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        identifier = AssignmentOperator.clean_identifier(self.identifier) if context.in_global_scope() else context.next_variable()
        
        return f"def {identifier}({context.next_variable()}):\n{ident_str(self.patternMatch.to_python(Context(context)))}"
    
    def __eq__(self, obj):
        if not isinstance(obj, AssignmentOperator):
            return False
        
        return self.identifier == obj.identifier and self.patternMatch == obj.patternMatch