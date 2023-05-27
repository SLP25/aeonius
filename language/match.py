from .element import Element
from .context import Context
from .grammar import Code
from .expression import Expression
from .utils import ident_str, return_name, pipe_validate
from typing import List, Tuple
from .graphviz_data import GraphVizId
from graphviz import nohtml


class Match(Element):
    pass


class MultiCondMatch(Match):
    def __init__(self, matches: List[Tuple[Expression, Match]]):
        self.matches = matches

    def validate(self, context):
        return pipe_validate(list(map(lambda s: s[0].validate(context), self.matches)) + list(map(lambda s: s[1].validate(context), self.matches)))

    def __single_if__(self, expression: Expression, match: Match, context: Context):
        cond = f"if {expression.to_python(context)}:"
        code = ident_str(match.to_python(context))
        return f"{cond}\n {code}"

    def to_python(self, context: Context) -> str:
        return "\n".join(map(lambda em: self.__single_if__(em[0], em[1], context), self.matches))

    def __eq__(self, obj):
        if not isinstance(obj, MultiCondMatch):
            return False

        return self.matches == obj.matches

    def append_to_graph(self, graph):
        id = GraphVizId.createNode(graph, "MultiCondMatch")
        for i in self.matches:
            graph.edge(id, GraphVizId.pairToGraph(graph, i[0].append_to_graph(
                graph), i[1].append_to_graph(graph), "Expression", "Match"))
        return id


class MatchFunctionBody(Match):
    def __init__(self, body):
        self.body = body

    #TODO: Validate availability of "return_{name}"
    def validate(self, context):
        return self.body.validate(context)

    def to_python(self, context: Context):
        function_name = return_name(context.function_name)
        arg_name = context.next_variable()
        new_context = Context(function_name, arg_name, context)
        return f"def {function_name}({arg_name}):{ident_str(self.body.to_python(new_context))}"

    def __eq__(self, obj):
        if not isinstance(obj, MatchFunctionBody):
            return False

        return self.body == obj.body

    def append_to_graph(self, graph):
        # como n sei o q isto representa vou so usar o body
        return self.body.append_to_graph(graph)


class MatchExpression(Match):
    def __init__(self, body: Expression, auxiliary: Code):
        self.body = body
        self.auxiliary = auxiliary

    def validate(self, context):
        return pipe_validate([self.auxiliary.validate(context), self.body.validate(context)])

    def to_python(self, context: Context):
        new_context = Context(context.function_name,
                              context.function_name, context)
        aux = self.auxiliary.to_python(new_context)

        return f"{aux}\n{return_name(context.function_name)} = {self.body.to_python(new_context)}\nreturn {return_name(context.function_name)}"

    def __eq__(self, obj):
        if not isinstance(obj, MatchExpression):
            return False

        return self.body == obj.body and self.auxiliary == obj.auxiliary

    def append_to_graph(self, graph):
        g = GraphVizId.createNode(graph, nohtml(
            "<0>MatchExpression|<1>Auxliary|<2>Return"), shape="record")
        graph.edge(g+":1", self.auxiliary.append_to_graph(graph))
        graph.edge(g+":2", self.body.append_to_graph(graph))
        return g+":0"


class MatchCondition(Match):
    def __init__(self, body: MultiCondMatch, code: Code):
        self.body = body
        self.code = code

    def validate(self, context):
        return pipe_validate([self.body.validate(context), self.code.validate(context)])

    def to_python(self, context: Context):
        return self.code.to_python(context) + "\n" + self.body.to_python(context)

    def __eq__(self, obj):
        if not isinstance(obj, MatchCondition):
            return False

        return self.body == obj.body and self.code == obj.code

    def append_to_graph(self, graph):
        return self.body.append_to_graph(graph)
