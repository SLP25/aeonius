from language.context import Context
from .element import Element
from .pattern import Pattern
from .expression import Expression
from .utils import ident_str
from .context import Context
from .grammar import Code
from .pattern_match import MultiPatternMatch
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


class FunctionBody(Element):
    def __init__(self, code: Code, multiPattern: MultiPatternMatch):
        self.code = code
        self.multiPattern = multiPattern

    def validate(self, context):
        return True

    def to_python(self, context: Context) -> str:
        return self.code.to_python(context) + "\n" + self.multiPattern.to_python(context) + '\nreturn y'

    def __eq__(self, obj):
        if not isinstance(obj, FunctionBody):
            return False

        return self.code == obj.code and self.multiPattern == obj.multiPattern


class AssignmentDefinition(Assignment):
    def __init__(self, identifier: str, functionBody: FunctionBody):
        self.identifier = identifier
        self.functionBody = functionBody

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        identifier = self.identifier if context.in_global_scope() else context.next_variable()
        new_context = Context(context)
        return f"def {identifier}(x):\n{ident_str(self.functionBody.to_python(new_context))}"

    def __eq__(self, obj):
        if not isinstance(obj, AssignmentDefinition):
            return False

        return self.identifier == obj.identifier and self.patternMatch == obj.patternMatch


class AssignmentOperator(Assignment):
    def __init__(self, identifier: str, functionBody: FunctionBody):
        self.identifier = identifier
        self.functionBody = functionBody

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
        identifier = AssignmentOperator.clean_identifier(
            self.identifier) if context.in_global_scope() else context.next_variable()

        return f"def {identifier}({context.next_variable()}):\n{ident_str(self.functionBody.to_python(Context(context)))}"

    def __eq__(self, obj):
        if not isinstance(obj, AssignmentOperator):
            return False

        return self.identifier == obj.identifier and self.functionBody == obj.functionBody
