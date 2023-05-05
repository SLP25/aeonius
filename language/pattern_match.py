from .element import Element
from .match import Match
from .context import Context
from .pattern import Pattern
from .utils import ident_str
from typing import List, Tuple


class MultiPatternMatch(Element):
    def __init__(self, matches: List[Tuple[Pattern, Match]]):
        self.matches = matches

    def validate(self, context):
        return True

    def to_python(self, context: Context):
        matches = "\n".join(map(lambda s: f"case {s[0].to_python(context)}:\n{ident_str(s[1].to_python(context))}", self.matches))
        return f"match x:\n{ident_str(matches)}"

    def __eq__(self, obj):
        if not isinstance(obj, MultiPatternMatch):
            return False

        return self.matches == obj.matches
