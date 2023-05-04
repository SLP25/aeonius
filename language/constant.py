from .element import Element
from .context import Context
from typing import List, Tuple
from .graphviz_data import GraphVizId

class Constant(Element):
    pass


class PrimitiveConstant(Constant):
    def __init__(self, primitive):
        self.primitive = primitive

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return str(self.primitive)

    def __eq__(self, obj):
        if not isinstance(obj, PrimitiveConstant):
            return False

        return type(self.primitive) == type(obj.primitive) and self.primitive == obj.primitive
    
    def append_to_graph(self,graph):
        return GraphVizId.createNode(graph,"Primitive: "+str(self.primitive))


class BracketConstant(Constant):
    def __init__(self, constant: Constant):
        self.constant = constant

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return f"({self.constant.to_python(context)})"

    def __eq__(self, obj):
        if not isinstance(obj, BracketConstant):
            return False

        return self.constant == obj.constant
    
    def append_to_graph(self,graph):
        return GraphVizId.encapsulate(graph,self.constant.append_to_graph(graph),initial='(',end=')')


class TupleConstantContent(Element):
    pass


class EmptyTupleConstantContent(TupleConstantContent):
    def __init__(self):
        pass

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return ""

    def __eq__(self, obj):
        return isinstance(obj, EmptyTupleConstantContent)
    
    def append_to_graph(self,graph):
        return GraphVizId.createNode(graph,"EmptyTupleConstantContent")


class NonEmptyTupleConstantContent(TupleConstantContent):
    def __init__(self, constants: TupleConstantContent, final_comma: bool = False):
        self.constants = constants
        self.final_comma = final_comma

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return ",".join(map(lambda elem: elem.to_python(context), self.constants))

    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyTupleConstantContent):
            return False

        return self.constants == obj.constants and self.final_comma == obj.final_comma
    
    def append_to_graph(self,graph):
        return GraphVizId.content(graph, list(map(lambda x:x.append_to_graph(graph),self.constants)))


class TupleConstant(Constant):
    def __init__(self, constant: TupleConstantContent):
        self.constant = constant

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return f"({self.constant.to_python(context)})"

    def __eq__(self, obj):
        if not isinstance(obj, TupleConstant):
            return False

        return self.constant == obj.constant
    
    def append_to_graph(self,graph):
        return GraphVizId.encapsulate(graph,self.constant.append_to_graph(graph),initial='(',end=')')

class ListConstantContent(Constant):
    pass


class EmptyListConstantContent(ListConstantContent):
    def __init__(self):
        pass

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return ""

    def __eq__(self, obj):
        return isinstance(obj, EmptyListConstantContent)
    
    def append_to_graph(self,graph):
        return GraphVizId.createNode(graph,"EmptyListConstantContent")


class NonEmptyListConstantContent(ListConstantContent):
    def __init__(self, constants: List[Constant], final_comma: bool = False):
        self.constants = constants
        self.final_comma = final_comma

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return ",".join(map(lambda elem: elem.to_python(context), self.constants))

    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyListConstantContent):
            return False

        return self.constants == obj.constants and self.final_comma == obj.final_comma

    def append_to_graph(self,graph):
        return GraphVizId.content(graph, list(map(lambda x:x.append_to_graph(graph),self.constants)),self.final_comma)



class ListConstant(Constant):
    def __init__(self, constants: ListConstantContent):
        self.constants = constants

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return f"[{self.constants.to_python(context)}]"

    def __eq__(self, obj):
        if not isinstance(obj, ListConstant):
            return False

        return self.constants == obj.constants
    
    def append_to_graph(self,graph):
        return self.constants.append_to_graph(graph)


class DictConstantContent(Element):
    pass


class EmptyDictConstantContent(DictConstantContent):
    def __init__(self):
        pass

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return ""

    def __eq__(self, obj):
        return isinstance(obj, EmptyDictConstantContent)
    
    def append_to_graph(self,graph):
        return GraphVizId.createNode(graph,"EmptyDictConstantContent")


class NonEmptyDictConstantContent(DictConstantContent):
    def __init__(self, key_value_pairs: List[Tuple[Constant, Constant]], final_comma: bool = False):
        self.key_value_pairs = key_value_pairs
        self.final_comma = final_comma

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return ",".join(map(lambda kv: f"{kv[0].to_python(context)}: {kv[1].to_python(context)}", self.key_value_pairs))

    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyDictConstantContent):
            return False

        return self.key_value_pairs == obj.key_value_pairs and self.final_comma == obj.final_comma
    
    def append_to_graph(self,graph):
        return GraphVizId.content(graph, map(lambda xy: GraphVizId.pairToGraph(graph, xy[0].append_to_graph(graph), xy[1].append_to_graph(graph),"KEY","VALUE"),self.key_value_pairs),self.final_comma)


class DictConstant(Constant):
    def __init__(self, constants: DictConstantContent):
        self.constants = constants

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return f"{{{self.constant.to_python(context)}}}"

    def __eq__(self, obj):
        if not isinstance(obj, DictConstant):
            return False

        return self.constants == obj.constants
    
    def append_to_graph(self,graph):
        return GraphVizId.encapsulate(graph, self.constants.append_to_graph(graph),initial='{',end='}')
