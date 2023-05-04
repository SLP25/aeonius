from .element import Element
from .context import Context
from .expression import Expression
from typing import List, Tuple
from .graphviz_data import GraphVizId


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
    
    def append_to_graph(self,graph):
        id = GraphVizId.createNode(graph,"MultiCondMatch")
        for i in self.matches:
            graph.edge(id,GraphVizId.pairToGraph(graph, i[0].append_to_graph(graph), i[1].append_to_graph(graph),"Expression","Match"))
        return id


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
    
    def append_to_graph(self, graph):
        #como n sei o q isto representa vou so usar o body
        return self.body.append_to_graph(graph)


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
    def append_to_graph(self, graph):
        #como n sei o q isto representa vou so usar o body
        return self.body.append_to_graph(graph)


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
    def append_to_graph(self, graph):
        #como n sei o q isto representa vou so usar o body
        return self.body.append_to_graph(graph)
