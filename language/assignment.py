from language.context import Context
from .element import Element
from .pattern import Pattern
from .expression import Expression
from .utils import ident_str, clean_identifier, return_name
from .context import Context
from .grammar import Code
from .pattern_match import MultiPatternMatch
from .graphviz_data import GraphVizId
from graphviz import nohtml, Graph
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

    def append_to_graph(self, graph: Graph):
        id = GraphVizId.getId()
        with graph.subgraph(name="cluster"+id) as c:
            g = GraphVizId.createNode(
                c, nohtml("<0>AssignmentPattern|<1>Pattern|<2>Expression"), shape="record")
            c.attr(color="blue")
            c.attr(label="AssignmentPattern")
            c.edge(g+":1", self.pattern.append_to_graph(c))
            c.edge(g+":2", self.expression.append_to_graph(c))
        return g+":0"


class FunctionBody(Element):
    def __init__(self, code: Code, multiPattern: MultiPatternMatch):
        self.code = code
        self.multiPattern = multiPattern

    def validate(self, context):
        return True

    def to_python(self, context: Context) -> str:
        return f"{self.code.to_python(context)}\n{self.multiPattern.to_python(context)}"

    def __eq__(self, obj):
        if not isinstance(obj, FunctionBody):
            return False

        return self.code == obj.code and self.multiPattern == obj.multiPattern

    def append_to_graph(self, graph):
        id = GraphVizId.createNode(graph, nohtml(
            "<0>FunctionBody|<CODE>Code|<PATTERNS>Patterns"), shape="record")
        graph.edge(id+":CODE", self.code.append_to_graph(graph))
        graph.edge(id+":PATTERNS", self.multiPattern.append_to_graph(graph))
        return id+":0"


class AssignmentDefinition(Assignment):
    def __init__(self, identifier: str, functionBody: FunctionBody):
        self.identifier = identifier
        self.functionBody = functionBody

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        identifier = self.identifier if context.in_global_scope(
        ) else return_name(context.function_name)
        arg_name = context.next_variable()
        context.symbols[self.identifier] = identifier
        new_context = Context(identifier, arg_name, context)

        body = f"{self.functionBody.to_python(new_context)}"
        return f"def {identifier}({arg_name}):\n{ident_str(body)}\n"

    def __eq__(self, obj):
        if not isinstance(obj, AssignmentDefinition):
            return False

        return self.identifier == obj.identifier and self.patternMatch == obj.patternMatch

    def append_to_graph(self, graph: Graph):
        id = GraphVizId.getId()
        with graph.subgraph(name="cluster"+id) as c:
            g = GraphVizId.createNode(c, nohtml(
                f"<0>AssignmentDefinition|{self.identifier}|<2>functionBody"), shape="record")
            c.attr(color="blue")
            c.attr(label="AssignmentPattern")
            c.edge(g+":2", self.functionBody.append_to_graph(c))
        return g+":0"


class AssignmentOperator(Assignment):
    def __init__(self, identifier: str, functionBody: FunctionBody):
        self.identifier = identifier
        self.functionBody = functionBody

    def validate(self, context):
        return True

    def to_python(self, context: Context):

        identifier = clean_identifier(
            self.identifier) if context.in_global_scope() else context.next_variable()

        arg_name = context.next_variable()
        context.symbols[self.identifier] = identifier
        new_context = Context(identifier, arg_name, context)
        return f"def {identifier}({arg_name}):\n{ident_str(self.functionBody.to_python(new_context))}"

    def __eq__(self, obj):
        if not isinstance(obj, AssignmentOperator):
            return False

        return self.identifier == obj.identifier and self.functionBody == obj.functionBody

    def append_to_graph(self, graph: Graph):
        id = GraphVizId.getId()
        with graph.subgraph(name="cluster"+id) as c:
            g = GraphVizId.createNode(c, nohtml(
                f"<0>AssignmentOperator|\\{self.identifier}|<2>functionBody"), shape="record")
            c.attr(color="blue")
            c.attr(label="AssignmentOperator")
            c.edge(g+":2", self.functionBody.append_to_graph(c))
        return g+":0"
