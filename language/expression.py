from language.context import Context
from .element import Element
from .constant import Constant
from .pattern import Pattern
from .context import Context
from typing import List, Tuple
from .graphviz_data import GraphVizId
from graphviz import nohtml


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
    def append_to_graph(self,graph):
        id = GraphVizId.getId()
        graph.node(id,self.identifier)
        return id
        
        


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
    def append_to_graph(self,graph):
        return self.constant.append_to_graph(graph)


class OperatorApplication(Expression):
    def __init__(self, operator: str):
        self.operator = operator

    def validate(self, context):
        return True

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

    def to_python(self, context: Context):
        return OperatorApplication.clean_identifier(self.operator)

    def __eq__(self, obj):
        if not isinstance(obj, OperatorApplication):
            return False

        return self.operator == obj.operator
    
    def append_to_graph(self,graph):
        id = GraphVizId.getId()
        graph.node(id,OperatorApplication.clean_identifier(self.operator))
        return id 


class FunctionApplicationExpression(Expression):
    def __init__(self, function: Expression, arguments: List[Expression]):
        self.function = function
        self.arguments = arguments

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        res = self.function.to_python(context)
        for arg in self.arguments:
            res += f" {arg.to_python(context)}"
        return res

    def __eq__(self, obj):
        if not isinstance(obj, FunctionApplicationExpression):
            return False

        return self.function == obj.function and self.arguments == obj.arguments
    
    def append_to_graph(self,graph):
        id = GraphVizId.getId()
        graph.node(id,"FunctionApplicationExpression")
        function=self.function.append_to_graph(graph)
        graph.edge(id,function)
        idg = GraphVizId.getId()
        with graph.subgraph(name=idg) as c:
            c.attr(color="green")
            c.attr(label="Expressions")
            for arg in self.arguments:
                arg.append_to_graph(c)
        graph.edge(id,idg)
        return id 


class LambdaExpression(Expression):
    def __init__(self, identifier: str, expression: Expression):
        self.identifier = identifier
        self.expression = expression

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        # TODO: Update symbol
        return f"lambda {self.identifier}: {self.expression.to_python(context)}"

    def __eq__(self, obj):
        if not isinstance(obj, LambdaExpression):
            return False

        return self.identifier == obj.identifier and self.expression == obj.identifier
    
    def append_to_graph(self, graph):
        id=GraphVizId.getId()
        graph.node(id,f"LambdaExpression -> {self.identifier}")
        expression =self.expression.append_to_graph(graph)
        graph.edge(id,expression)
        return id
        


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

    def append_to_graph(self, graph):
        id=GraphVizId.getId()
        graph.node(id, nohtml('<f0> IF|<f1> Then|<f2> Else'))
        expression = self.expression.append_to_graph(graph)
        then = self.condition.append_to_graph(graph)
        elsee = self.false_expression.append_to_graph(graph)
        graph.edge(id+":f0",expression)
        graph.edge(id+":f1",then)
        graph.edge(id+":f2",elsee)
        return id+":f0"

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
    
    def append_to_graph(self, graph):
        id=GraphVizId.getId()
        if self.condition is not None:
            graph.node(id, nohtml('<f0> FOR|<f1> VALUE|<f2> IN|<f3>IF'))
            condition = self.condition.append_to_graph(graph)
            graph.edge(id+":f3",condition)
        else:
            graph.node(id, nohtml('<f0> FOR|<f1> VALUE|<f2> IN'))
        expression = self.expression.append_to_graph(graph)
        pattern = self.pattern.append_to_graph(graph)
        sett = self.set.append_to_graph(graph)
        graph.edge(id+":f0",expression)
        graph.edge(id+":f1",pattern)
        graph.edge(id+":f2",sett)
        return id+":f0"

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
    
    def append_to_graph(self, graph):
        id=GraphVizId.getId()
        if self.condition is not None:
            graph.node(id, nohtml('<f0> KEY|<f1> VALUE|<f2> FOR VALUE|<f3>IN|<f4>IF'))
            condition = self.condition.append_to_graph(graph)
            graph.edge(id+":f4",condition)
        else:
            graph.node(id, nohtml('<f0> KEY|<f1> VALUE|<f2> FOR VALUE|<f3>IN'))
        identifier=GraphVizId.getId()
        graph.node(identifier,self.identifier)
        expression = self.expression.append_to_graph(graph)
        pattern = self.pattern.append_to_graph(graph)
        sett = self.set.append_to_graph(graph)
        graph.edge(id+":f0",identifier)
        graph.edge(id+":f1",expression)
        graph.edge(id+":f2",pattern)
        graph.edge(id+":f3",sett)
        return id+":f0"


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

        return self.left_expression == obj.left_expression and self.right_expression == obj.right_expression and self.identifier == obj.identifier
    
    def append_to_graph(self, graph):
        id=GraphVizId.getId()
        graph.node(id, nohtml(f'<f0> Operation|{self.identifier}|(|<f1>Left|,|<f2> Right|)'))
        left_expression = self.expression.append_to_graph(graph)
        right_expression = self.condition.append_to_graph(graph)
        graph.edge(id+":f1",left_expression)
        graph.edge(id+":f2",right_expression)
        return id+":f0"

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
    def append_to_graph(self, graph):
        return self.expression.append_to_graph(graph)


class TupleExpressionContent(Element):
    pass


class UnpackExpression(Expression):
    def __init__(self, expression: Expression):
        self.expression = expression

    def validate(self, context):
        return True

    def to_python(self, context: Context) -> str:
        return "ok"

    def __eq__(self, obj):
        if not isinstance(obj, UnpackExpression):
            return False

        return self.expression == obj.expression
    def append_to_graph(self, graph):
        return self.expression.append_to_graph(graph)


class NonEmptyTupleExpressionContent(TupleExpressionContent):
    def __init__(self, expressions: TupleExpressionContent, final_comma: bool = False):
        self.expressions = expressions
        self.final_comma = final_comma

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        result = ",".join(
            map(lambda exp: exp.to_python(context), self.expressions))

        if self.final_comma:
            result += ","

        return result

    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyTupleExpressionContent):
            return False

        return self.expressions == obj.expressions and self.final_comma == obj.final_comma
    
    def append_to_graph(self,graph):
        id = GraphVizId.getId()
        graph.node(id,"NonEmptyTupleExpressionContent")
        for i in self.expressions:
            j=i.append_to_graph(graph)
            graph.edge(id,j)
        if self.final_comma:
            idg = GraphVizId.getId()
            graph.node(idg,',')
            graph.edge(id,idg)
        return id


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
    
    def append_to_graph(self, graph):
        return self.expression.append_to_graph(graph)


class ListExpressionContent(Expression):
    pass


class NonEmptyListExpressionContent(ListExpressionContent):
    def __init__(self, expressions: List[Expression], final_comma: bool = False):
        self.expressions = expressions
        self.final_comma = final_comma

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        print(self.expressions)
        result = ",".join(
            map(lambda exp: exp.to_python(context), self.expressions))

        if self.final_comma:
            result += ","

        return result

    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyListExpressionContent):
            return False

        return self.expressions == obj.expressions and self.final_comma == obj.final_comma
    
    def append_to_graph(self,graph):
        id = GraphVizId.getId()
        graph.node(id,"NonEmptyListExpressionContent")
        for i in self.expressions:
            j=i.append_to_graph(graph)
            graph.edge(id,j)
        if self.final_comma:
            idg = GraphVizId.getId()
            graph.node(idg,',')
            graph.edge(id,idg)
        return id


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
    def append_to_graph(self, graph):
        return self.expressions.append_to_graph(graph)


class DictExpressionContent(Element):
    pass


class NonEmptyDictExpressionContent(DictExpressionContent):
    def __init__(self, key_value_pairs: List[Tuple[Expression, Expression]], final_comma: bool = False, tail: Expression = None):
        self.key_value_pairs = key_value_pairs
        self.final_comma = final_comma
        self.tail = tail

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        result = ",".join(map(
            lambda kv: f"{kv[0].to_python(context)} : {kv[1].to_python(context)}", self.key_value_pairs))

        if self.final_comma:
            result += ","

        if self.tail is not None:
            result += f"**{self.tail.to_python(context)}"

        return result

    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyDictExpressionContent):
            return False

        return self.key_value_pairs == obj.key_value_pairs and self.final_comma == obj.final_comma and self.tail == obj.tail
    
    def append_to_graph(self,graph):
        id = GraphVizId.getId()
        graph.node(id,"NonEmptyDictExpressionContent")
        for i in self.key_value_pairs:
            idg = GraphVizId.getId()
            with g.subgraph(name=idg) as c:
                c.attr(color="blue")
                c.attr(label="")
                j=i[0].append_to_graph(c)
                k=i[1].append_to_graph(c)
            graph.edge(id,idg)
        if self.final_comma:
            idg = GraphVizId.getId()
            graph.node(idg,',')
            graph.edge(id,idg)
        if self.tail:
            tail=self.tail.append_to_graph(graph)
            graph.edge(id,tail)
        return id

class DictExpression(Expression):
    def __init__(self, expressions: DictExpressionContent):
        self.expressions = expressions

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return f"{{ {self.expressions.to_python(context)}}}"

    def __eq__(self, obj):
        if not isinstance(obj, DictExpression):
            return False

        return self.expressions == obj.expressions
    def append_to_graph(self, graph):
        return self.expressions.append_to_graph(graph)
