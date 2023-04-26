from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def validate(self, context) -> bool:
        pass
    @abstractmethod
    def __str__(self) -> str:
        pass
    @abstractmethod
    def __eq__(self, obj) -> bool:
        pass