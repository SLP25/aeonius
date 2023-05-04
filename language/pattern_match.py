from .element import Element
from .match import Match
from .context import Context
from .pattern import Pattern
from typing import Tuple
from .graphviz_data import GraphVizId


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
        id = GraphVizId.createNode(graph,"MultiPatternMatch")
        for i in self.matches:
            idg = GraphVizId.getId()
            GraphVizId.pairToGraph(graph, i[0].append_to_graph(graph), i[1].append_to_graph(graph),"PATTERN","MATCH")
            graph.edge(id,idg)
        return id
