from .element import Element
from .constant import Constant
from .pattern import Pattern
from .context import Context
from typing import List, Tuple

class Expression(Element):
    pass

class IdentifierExpression(Expression):
    def __init__(self, identifier: str):
        self.identifier = identifier

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        return self.identifier
    
    def __eq__(self, obj):
        if not isinstance(obj, IdentifierExpression):
            return False
        
        return self.identifier == obj.identifier
    
class ConstantExpression(Expression):
    def __init__(self, constant: Constant):
        self.constant = constant

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        return self.constant.to_python(context)
    
    def __eq__(self, obj):
        if not isinstance(obj, ConstantExpression):
            return False
        
        return self.constant == obj.constant
    

class LambdaExpression(Expression):
    def __init__(self, identifier: str, expression: Expression):
        self.identifier = identifier
        self.expression = expression

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        #TODO: Update symbol
        return f"lambda {self.identifier}: {self.expression.to_python(context)}"
    
    def __eq__(self, obj):
        if not isinstance(obj, LambdaExpression):
            return False
        
        return self.identifier == obj.identifier and self.expression == obj.identifier
    

class IfElseExpression(Expression):
    def __init__(self, condition: Expression, true_expression: Expression, false_expression: Expression):
        self.condition = condition
        self.true_expresion = true_expression
        self.false_expression = false_expression

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        return f"{self.true_expresion.to_python(context)} if {self.condition.to_python(context)} else {self.false_expression.to_python(context)}"
    
    def __eq__(self, obj):
        if not isinstance(obj, IfElseExpression):
            return False
        
        return self.condition == obj.condition and self.true_expresion == obj.true_expresion and self.false_expression == obj.false_expression
    

class ForLoopExpression(Expression):
    def __init__(self, expression: Expression, pattern: Pattern, set: Expression, condition: Expression = None):
        self.expression = expression
        self.pattern = pattern
        self.set = set
        self.condition = condition

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        result = f"{self.expression.to_python(context)} for {self.pattern.to_python(context)} in {self.set.to_python(context)}"

        if self.condition is not None:
            result += f" if {self.condition.to_python(context)}"

        return result
    
    def __eq__(self, obj):
        if not isinstance(obj, ForLoopExpression):
            return False
        
        return self.expression == obj.expression and self.pattern == obj.pattern and self.set == obj.set and self.condition == obj.condition
    

class DictionaryCompreensionExpression(Expression):
    def __init__(self, identifier: str, expression: Expression, pattern: Pattern, set: Expression, condition: Expression = None):
        self.identifier = identifier
        self.expression = expression
        self.pattern = pattern
        self.set = set
        self.condition = condition

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        result = f"{{ {self.identifier} : {self.expression.to_python(context)} for {self.pattern.to_python(context)} in {self.set.to_python(context)}"

        if self.condition is not None:
            result += f" if {self.condition.to_python(context)}"
        result += "}"
        return result
    
    def __eq__(self, obj):
        if not isinstance(obj, DictionaryCompreensionExpression):
            return False
        
        return self.identifier == obj.identifier and self.expression == obj.expression \
            and self.pattern == obj.pattern and self.set == obj.set and self.condition == obj.condititon

class OperationExpression(Expression):
    def __init__(self, identifier: str, left_expression: Expression, right_expression: Expression):
        self.identifier = identifier
        self.left_expression = left_expression
        self.right_expression = right_expression

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        return f"{self.identifier}({self.left_expression.to_python(context)}, {self.right_expression.to_python(context)})"
    
    def __eq__(self, obj):
        if not isinstance(obj, OperationExpression):
            return False
        
        return self.left_expression == obj.left_expression and self.right_expression == obj.right_expression  and self.identifier == obj.identifier
    
   
   
class BracketExpression(Expression):
    def __init__(self, expression: Expression):
        self.expression = expression

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return f"({self.expression.to_python(context)})"
    
    def __eq__(self, obj):
        if not isinstance(obj, BracketExpression):
            return False
        
        return self.expression == obj.expression
    
class TupleExpressionContent(Element):
    pass
    
class NonEmptyTupleExpressionContent(TupleExpressionContent):
    def __init__(self, expressions: TupleExpressionContent, final_comma: bool = False):
        self.expressions = expressions
        self.final_comma = final_comma

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        result = ",".join(map(lambda exp: exp.to_python(context), self.expressions))

        if self.final_comma:
            result += ","

        return result
    
    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyTupleExpressionContent):
            return False
        
        return self.expressions == obj.expressions and self.final_comma == obj.final_comma
    

    


class TupleExpression(Expression):
    def __init__(self, expression: TupleExpressionContent):
        self.expression = expression

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return f"({self.expression.to_python(context)})"
    
    def __eq__(self, obj):
        if not isinstance(obj, TupleExpression):
            return False
        
        return self.expression == obj.expression
    
class ListExpressionContent(Expression):
    pass

    
class NonEmptyListExpressionContent(ListExpressionContent):
    def __init__(self, expressions: List[Expression], final_comma:bool = False):
        self.expressions = expressions
        self.final_comma = final_comma

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        result = ",".join(map(lambda exp: exp.to_python(context), self.expressions))

        if self.final_comma:
            result += ","

        return result
    
    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyListExpressionContent):
            return False
        
        return self.expressions == obj.expressions and self.final_comma == obj.final_comma

class ListExpression(Expression):
    def __init__(self, expressions: ListExpressionContent):
        self.expressions = expressions

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return f"[{self.expressions.to_python(context)}]"
    
    def __eq__(self, obj):
        if not isinstance(obj, ListExpression):
            return False
        
        return self.expressions == obj.expressions
    

class DictExpressionContent(Element):
    pass
    
class NonEmptyDictExpressionContent(DictExpressionContent):
    def __init__(self, key_value_pairs: List[Tuple[Expression, Expression]], final_comma:bool = False):
        self.key_value_pairs = key_value_pairs
        self.final_comma = final_comma

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        result = ",".join(map(lambda kv: f"{kv[0].to_python(context)} : {kv[1].to_python(context)}", self.key_value_pairs))

        if self.final_comma:
            result += ","

        return result
    
    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyDictExpressionContent):
            return False
        
        return self.key_value_pairs == obj.key_value_pairs and self.final_comma == obj.final_comma

class DictExpression(Expression):
    def __init__(self, expressions: DictExpressionContent):
        self.expressions = expressions
    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return f"{self.expressions.to_python(context)}"
    
    def __eq__(self, obj):
        if not isinstance(obj, DictExpression):
            return False
        
        return self.expressions == obj.expressions
