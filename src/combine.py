from typing import Generic, TypeVar, Callable, Tuple
from typing_extensions import override
from src.node import Node


InputType1 = TypeVar('InputType1')
InputType2 = TypeVar('InputType2')
IntermediateType1 = TypeVar('IntermediateType1')
IntermediateType2 = TypeVar('IntermediateType2')
OutputType = TypeVar('OutputType')


class Combine(Node[Tuple[InputType1, InputType2], OutputType], 
              Generic[InputType1, InputType2, IntermediateType1, IntermediateType2, OutputType]):
    """ 
    Represents a processing node that takes two antecedent nodes and combines their outputs.
    """

    def __init__(self, 
                 base_one: Node[InputType1, IntermediateType1],
                 base_two: Node[InputType2, IntermediateType2],
                 func: Callable[[IntermediateType1, IntermediateType2], OutputType]) -> None:
        self.base_one = base_one
        self.base_two = base_two
        self.func = func
        super().__init__()
    
    @property
    def base_node_one(self) -> Node[InputType1, IntermediateType1]:
        return self.base_one

    @property
    def base_node_two(self) -> Node[InputType2, IntermediateType2]:
        return self.base_two

    @property
    def combine_function(self) -> Callable[[IntermediateType1, IntermediateType2], OutputType]:
        return self.func

    @override
    def _process(self, input_data: Tuple[InputType1, InputType2]) -> OutputType:
        return self.func(self.base_one.process(input_data[0]), self.base_two.process(input_data[1]))
