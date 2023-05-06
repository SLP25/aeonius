from .element import Element
from .context import Context
from .grammar import Code
from .expression import Expression
from .utils import ident_str
from typing import List, Tuple
from .graphviz_data import GraphVizId


class Match(Element):
    pass


class MultiCondMatch(Match):
    def __init__(self, matches: List[Tuple[Expression, Match]]):
        self.matches = matches

    def validate(self, context):
        return True

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

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        function_name = context.next_variable()
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
        return True

    def to_python(self, context: Context):
        new_context = Context(context.function_name,
                              context.function_name, context)
        aux = self.auxiliary.to_python(new_context)

        return f"{aux}\nreturn_{context.function_name} = {self.body.to_python(new_context)}\nreturn return_{context.function_name}"

    def __eq__(self, obj):
        if not isinstance(obj, MatchExpression):
            return False

        return self.body == obj.body and self.auxiliary == obj.auxiliary

    def append_to_graph(self, graph):
        # FIXME: lumafepe como n sei o q isto representa vou so usar o body
        return self.body.append_to_graph(graph)


class MatchCondition(Match):
    def __init__(self, body: MultiCondMatch):
        self.body = body

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return self.body.to_python(context)

    def __eq__(self, obj):
        if not isinstance(obj, MatchCondition):
            return False

        return self.body == obj.body

    def append_to_graph(self, graph):
        # como n sei o q isto representa vou so usar o body
        return self.body.append_to_graph(graph)
