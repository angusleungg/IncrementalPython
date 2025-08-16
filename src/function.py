from typing import Generic, TypeVar, Callable
from typing_extensions import override
from src.node import Node


InputType = TypeVar('InputType')
OutputType = TypeVar('OutputType')


class Function(Node[InputType, OutputType], 
           Generic[InputType, OutputType]):
    """ 
    Represents a processing node that is just a function wrapper. This is useful
    for creating nodes in bind, as it can be used instead of a Leaf to construct 
    a subgraph that has no inputs bound. 
    """

    def __init__(self, 
                 func: Callable[[InputType], OutputType]):
        self.func = func

    @property
    def function(self) -> Callable[[InputType], OutputType]:
        return self.func

    @override
    def process(self, input_data: InputType) -> OutputType:
        return self.func(input_data)
