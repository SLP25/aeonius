from .element import Element
from .match import Match
from .context import Context
from .pattern import Pattern
from typing import Tuple


class MultiPatternMatch(Element):
    def __init__(self, matches: Tuple[Pattern, Match]):
        self.matches = matches

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"

    def __eq__(self, obj):
        if not isinstance(obj, MultiPatternMatch):
            return False

        return self.matches == obj.matches
    
    def append_to_graph(self,graph):
        id = GraphVizId.getId()
        graph.node(id,"MultiPatternMatch")
        for i in self.matches:
            idg = GraphVizId.getId()
            with g.subgraph(name=idg) as c:
                c.attr(color="blue")
                c.attr(label="")
                j=i[0].append_to_graph(c)
                k=i[1].append_to_graph(c)
            graph.edge(id,idg)
        return id
