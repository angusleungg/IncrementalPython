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
                 _fixed_value: OutputType) -> None:
        self._fixed_value = _fixed_value
        super().__init__()

    @property
    def fixed_value(self) -> OutputType:
        return self._fixed_value

    @fixed_value.setter
    def fixed_value(self, value: OutputType) -> None:
        self._fixed_value = value

    @override
    def _process(self, input_data: None) -> OutputType:
        return self.fixed_value
