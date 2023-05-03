from language.context import Context
from .element import Element
from .constant import Constant, PrimitiveConstant
from .context import Context
from typing import List, Tuple
from .graphviz_data import GraphVizId


class Pattern(Element):
    pass


class ConstantPattern(Pattern):
    def __init__(self, constant: Constant):
        self.constant = constant

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"

    def __eq__(self, obj):
        if not isinstance(obj, ConstantPattern):
            return False

        return self.constant == obj.constant
    
    def append_to_graph(self, graph):
        return self.constant.append_to_graph(graph)


class AnythingPattern(Pattern):
    def __init__(self):
        pass

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"

    def __eq__(self, obj):
        return isinstance(obj, AnythingPattern)
    
    def append_to_graph(self, graph):
        id = GraphVizId.getId()
        graph.node(id,"AnythingPattern")
        return id
        


class IdentifierPatttern(Pattern):
    def __init__(self, identifier: str):
        self.identifier = identifier

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return self.identifier

    def __eq__(self, obj):
        if not isinstance(obj, IdentifierPatttern):
            return False

        return self.identifier == obj.identifier
    
    def append_to_graph(self, graph):
        id = GraphVizId.getId()
        graph.node(id,self.identifier)
        return id


class BracketPattern(Pattern):
    def __init__(self, pattern: Pattern):
        self.pattern = pattern

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return f"({self.pattern.to_python(context)})"

    def __eq__(self, obj):
        if not isinstance(obj, BracketPattern):
            return False

        return self.pattern == obj.pattern
    def append_to_graph(self, graph):
        return self.pattern.append_to_graph(graph)


class TuplePatternContent(Element):
    pass


class NonEmptyTuplePatternContent(TuplePatternContent):
    def __init__(self, patterns: TuplePatternContent, final_comma: bool = False):
        self.patterns = patterns
        self.final_comma = final_comma

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return ",".join(map(lambda p: p.to_python(context), self.patterns)) + ("," if self.final_comma else "")

    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyTuplePatternContent):
            return False

        return self.patterns == obj.patterns and self.final_comma == obj.final_comma
    
    def append_to_graph(self,graph):
        id = GraphVizId.getId()
        graph.node(id,"NonEmptyTuplePatternContent")
        for i in self.patterns:
            j=i.append_to_graph(graph)
            graph.edge(id,j)
        if self.final_comma:
            idg = GraphVizId.getId()
            graph.node(idg,',')
            graph.edge(id,idg)
        return id


class TuplePattern(Pattern):
    def __init__(self, pattern: TuplePatternContent):
        self.pattern = pattern

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return f"({self.pattern.to_python(context)})"

    def __eq__(self, obj):
        if not isinstance(obj, TuplePattern):
            return False

        return self.pattern == obj.pattern
    
    def append_to_graph(self, graph):
        return self.pattern.append_to_graph(graph)


class ListPatternContent(Pattern):
    pass


class NonEmptyListPatternContent(ListPatternContent):
    def __init__(self, patterns: List[Pattern], final_comma: bool = False):
        self.patterns = patterns
        self.final_comma = final_comma

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return ",".join(map(lambda p: p.to_python(context), self.patterns)) + ("," if self.final_comma else "")

    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyListPatternContent):
            return False

        return self.patterns == obj.patterns and self.final_comma == obj.final_comma
    
    def append_to_graph(self,graph):
        id = GraphVizId.getId()
        graph.node(id,"NonEmptyListPatternContent")
        for i in self.patterns:
            j=i.append_to_graph(graph)
            graph.edge(id,j)
        if self.final_comma:
            idg = GraphVizId.getId()
            graph.node(idg,',')
            graph.edge(id,idg)
        return id


class PrimitivePattern(Pattern):
    def __init__(self, primitive: PrimitiveConstant):
        self.primitive = primitive

    def validate(self, context):
        return True

    def to_python(self, context):
        return self.primitive.to_python(context)

    def __eq__(self, obj):
        if not isinstance(obj, PrimitivePattern):
            return False

        return True
    
    def append_to_graph(self, graph):
        return self.primitive.append_to_graph(graph)


class UnpackPattern(Pattern):
    def __init__(self, pattern: Pattern):
        self.pattern = pattern

    def validate(self, context):
        return True

    def to_python(self, context: Context) -> str:
        return f"*{self.pattern.to_python(context)}"

    def __eq__(self, obj):
        if not isinstance(obj, UnpackPattern):
            return False

        return self.pattern == obj.pattern
    def append_to_graph(self, graph):
        id=GraphVizId.getId()
        graph.node(id,"**")
        k=self.pattern.append_to_graph(graph)
        graph.edge(id,k)
        return id


class ListPattern(Pattern):
    def __init__(self, patterns: ListPatternContent):
        self.patterns = patterns

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return f"[{self.patterns.to_python(context)}]"

    def __eq__(self, obj):
        if not isinstance(obj, ListPattern):
            return False

        return self.patterns == obj.patterns
    
    def append_to_graph(self, graph):
        return self.patterns.append_to_graph(graph)


class DictPatternContent(Element):
    pass


class NonEmptyDictPatternContent(DictPatternContent):
    def __init__(self, key_value_pairs: List[Tuple[Pattern, Pattern]], final_comma: bool = False, tail: Pattern = None):
        self.key_value_pairs = key_value_pairs
        self.final_comma = final_comma
        self.tail = tail

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        content = map(
            lambda kv: f"{kv[0].to_python(context)}:{kv[1].to_python(context)}", self.key_value_pairs)
        base = ",".join(content)
        base += ("," if self.final_comma else "")
        base += f",**{self.tail.to_python(context)}" if self.tail else ""
        return base

    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyDictPatternContent):
            return False

        return self.key_value_pairs == obj.key_value_pairs and self.final_comma == obj.final_comma and self.tail == obj.tail

    def append_to_graph(self,graph):
        id = GraphVizId.getId()
        graph.node(id,"NonEmptyDictPatternContent")
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
    

class DictPattern(Pattern):
    def __init__(self, patterns: DictPatternContent):
        self.patterns = patterns

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return f"{{ {self.patterns.to_python(self.patterns)} }}"

    def __eq__(self, obj):
        if not isinstance(obj, DictPattern):
            return False

        return self.patterns == obj.patterns
    
    def append_to_graph(self, graph):
        return self.patterns.append_to_graph(graph)
