from abc import ABC, abstractmethod
from .context import Context
from graphviz import Graph


class Element(ABC):
    @abstractmethod
    def validate(self, context) -> bool:
        pass

    @abstractmethod
    def to_python(self, context: Context) -> str:
        pass

    @abstractmethod
    def __eq__(self, obj) -> bool:
        pass

    @abstractmethod
    def append_to_graph(self, graph: Graph) -> int:
        pass
