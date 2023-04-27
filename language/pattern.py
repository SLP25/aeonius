from .element import Element
from .constant import Constant
from .context import Context
from typing import List, Tuple

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
    
class AnythingPattern(Pattern):
    def __init__(self):
        pass

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        return isinstance(obj, AnythingPattern)
    
class IdentifierPatttern(Pattern):
    def __init__(self, identifier: str):
        self.identifier = identifier

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, IdentifierPatttern):
            return False
        
        return self.identifier == obj.identifier
    
   
class BracketPattern(Pattern):
    def __init__(self, pattern: Pattern):
        self.pattern = pattern

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, BracketPattern):
            return False
        
        return self.pattern == obj.pattern
    
class TuplePatternContent(Element):
    pass
    
class NonEmptyTuplePatternContent(TuplePatternContent):
    def __init__(self, patterns: TuplePatternContent, final_comma: bool = False):
        self.patterns = patterns
        self.final_comma = final_comma

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyTuplePatternContent):
            return False
        
        return self.patterns == obj.patterns and self.final_comma == obj.final_comma
    

    


class TuplePattern(Pattern):
    def __init__(self, pattern: TuplePatternContent):
        self.pattern = pattern

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, TuplePattern):
            return False
        
        return self.pattern == obj.pattern
    
class ListPatternContent(Pattern):
    pass

    
class NonEmptyListPatternContent(ListPatternContent):
    def __init__(self, patterns: List[Pattern], final_comma:bool = False):
        self.patterns = patterns
        self.final_comma = final_comma

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyListPatternContent):
            return False
        
        return self.patterns == obj.patterns and self.final_comma == obj.final_comma

class ListPattern(Pattern):
    def __init__(self, patterns: ListPatternContent):
        self.patterns = patterns

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, ListPattern):
            return False
        
        return self.patterns == obj.patterns
    

class DictPatternContent(Element):
    pass
    
class NonEmptyDictPatternContent(DictPatternContent):
    def __init__(self, key_value_pairs: List[Tuple[Pattern, Pattern]], final_comma:bool = False):
        self.key_value_pairs = key_value_pairs
        self.final_comma = final_comma

    def validate(self, context):
        return True
    
    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, NonEmptyDictPatternContent):
            return False
        
        return self.key_value_pairs == obj.key_value_pairs and self.final_comma == obj.final_comma

class DictPattern(Pattern):
    def __init__(self, patterns: DictPatternContent):
        self.patterns = patterns
    def validate(self, context):
        return True

    def to_python(self, context: Context):
        return "ok"
    
    def __eq__(self, obj):
        if not isinstance(obj, DictPattern):
            return False
        
        return self.patterns == obj.patterns
