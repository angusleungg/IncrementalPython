from src.node import Node
from typing import Generic, TypeVar, Callable
from typing_extensions import override

OutputType = TypeVar('OutputType')

class Leaf(Node[None, OutputType], 
             Generic[OutputType]):
    """ 
    Represents a processing node that is a leaf node that returns
    a constant value with no processing.
    """
    def __init__(self,
                 value: OutputType):
        self.value = value

    @property
    def return_value(self) -> OutputType:
        return self.value

    @override
    def process(self, input_data: None) -> OutputType:
        return self.value
