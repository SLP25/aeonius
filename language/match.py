from .element import Element
from .context import Context
from .expression import Expression
from typing import List, Tuple


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
        id = GraphVizId.getId()
        graph.node(id,"MultiCondMatch")
        for i in self.matches:
            idg = GraphVizId.getId()
            with g.subgraph(name=idg) as c:
                c.attr(color="blue")
                c.attr(label="")
                j=i[0].append_to_graph(c)
                k=i[1].append_to_graph(c)
            graph.edge(id,idg)
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
