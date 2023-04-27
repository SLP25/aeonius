from .element import Element
from .context import Context
from typing import List, Tuple

class Constant(Element):
    pass

class PrimitiveConstant(Constant):
    def __init__(self, primitive):
        self.primitive = primitive

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, PrimitiveConstant):
            return False
        
        return type(self.primitive) == type(obj.primitive) and self.primitive == obj.primitive
    
class BracketConstant(Constant):
    def __init__(self, constant: Constant):
        self.constant = constant

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, BracketConstant):
            return False
        
        return self.constant == obj.constant
    
class TupleConstantContent(Element):
    pass

class EmptyTupleConstantContent(TupleConstantContent):
    def __init__(self):
        pass

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        return isinstance(obj, EmptyTupleConstantContent)
    
class NonEmptyTupleConstantContent(TupleConstantContent):
    def __init__(self, constants: TupleConstantContent, final_comma: bool = False):
        self.constants = constants
        self.final_comma = final_comma

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyTupleConstantContent):
            return False
        
        return self.constants == obj.constants and self.final_comma == obj.final_comma
    

    


class TupleConstant(Constant):
    def __init__(self, constant: TupleConstantContent):
        self.constant = constant

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, TupleConstant):
            return False
        
        return self.constant == obj.constant
    
class ListConstantContent(Constant):
    pass

class EmptyListConstantContent(ListConstantContent):
    def __init__(self):
        pass

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        return isinstance(obj, EmptyListConstantContent)
    
class NonEmptyListConstantContent(ListConstantContent):
    def __init__(self, constants: List[Constant], final_comma:bool = False):
        self.constants = constants
        self.final_comma = final_comma

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyListConstantContent):
            return False
        
        return self.constants == obj.constants and self.final_comma == obj.final_comma

class ListConstant(Constant):
    def __init__(self, constants: ListConstantContent):
        self.constants = constants

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, ListConstant):
            return False
        
        return self.constants == obj.constants
    

class DictConstantContent(Element):
    pass

class EmptyDictConstantContent(DictConstantContent):
    def __init__(self):
        pass

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        return isinstance(obj, EmptyDictConstantContent)
    
class NonEmptyDictConstantContent(DictConstantContent):
    def __init__(self, key_value_pairs: List[Tuple[Constant, Constant]], final_comma:bool = False):
        self.key_value_pairs = key_value_pairs
        self.final_comma = final_comma

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyDictConstantContent):
            return False
        
        return self.key_value_pairs == obj.key_value_pairs and self.final_comma == obj.final_comma

class DictConstant(Constant):
    def __init__(self, constants: DictConstantContent):
        self.constants = constants
    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, DictConstant):
            return False
        
        return self.constants == obj.constants
