from typing import Generic, TypeVar, Callable, Tuple
from typing_extensions import override
from src.node import Node


InputType = TypeVar('InputType')
IntermediateType = TypeVar('IntermediateType')
OutputType1 = TypeVar('OutputType1')
OutputType2 = TypeVar('OutputType2')


class Fanout(Node[InputType, Tuple[OutputType1, OutputType2]], 
            Generic[InputType, IntermediateType, OutputType1, OutputType2]):
    """ 
    Represents a processing node that takes a node and applies two different functions
    to its output, effectively "fanning out" the result into two separate outputs.
    """

    def __init__(self, 
                 base: Node[InputType, IntermediateType],
                 func_one: Callable[[IntermediateType], OutputType1],
                 func_two: Callable[[IntermediateType], OutputType2]) -> None:
        self.base = base
        self.func_one = func_one
        self.func_two = func_two
        super().__init__()

    @property
    def base_node(self) -> Node[InputType, IntermediateType]:
        return self.base

    @property
    def fanout_func_one(self) -> Callable[[IntermediateType], OutputType1]:
        return self.func_one
    
    @property
    def fanout_func_two(self) -> Callable[[IntermediateType], OutputType2]:
        return self.func_two

    @override
    def _process(self, input_data: InputType) -> Tuple[OutputType1, OutputType2]:
        return self.func_one(self.base.process(input_data)), self.func_two(self.base.process(input_data))
