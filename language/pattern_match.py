from .element import Element
from .match import Match
from .context import Context
from .pattern import Pattern
from .graphviz_data import GraphVizId
from .utils import ident_str, return_name, pipe_validate
from typing import List, Tuple


class MultiPatternMatch(Element):
    def __init__(self, matches: List[Tuple[Pattern, Match]]):
        self.matches = matches

    def validate(self, context):
        return pipe_validate(list(map(lambda s: s[0].validate(context), self.matches)) + list(map(lambda s: s[1].validate(context), self.matches)))

    def to_python(self, context: Context):
        new_context = Context(context.function_name, context.arg_name, context)
        new_context.symbols["ignore"] = True
        matches = "\n".join(map(
            lambda s: f"case {s[0].to_python(new_context)}:\n{ident_str(s[1].to_python(context))}", self.matches))
        return f"match {context.arg_name}:\n{ident_str(matches)}\nreturn {return_name(context.function_name)}"

    def __eq__(self, obj):
        if not isinstance(obj, MultiPatternMatch):
            return False

        return self.matches == obj.matches

    def append_to_graph(self, graph):
        id = GraphVizId.createNode(graph, "MultiPatternMatch")
        for i in self.matches:
            idg = GraphVizId.pairToGraph(graph, i[0].append_to_graph(
                graph), i[1].append_to_graph(graph), "PATTERN", "MATCH")
            graph.edge(id, idg)
        return id
