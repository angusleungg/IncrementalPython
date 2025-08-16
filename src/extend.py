from src.node import Node
from typing import Generic, TypeVar, Callable
from typing_extensions import override

InputType = TypeVar('InputType')
IntermediateType = TypeVar('IntermediateType')
OutputType = TypeVar('OutputType')

class Extend(Node[InputType, OutputType], 
             Generic[InputType, IntermediateType, OutputType]):
    """ 
    Represents a processing node that is the equivalent of a map.
    """
    def __init__(self, 
                 base: Node[InputType, IntermediateType], 
                 func: Callable[[IntermediateType], OutputType]):
        self.base = base
        self.func = func
    
    @property
    def base_node(self) -> Node[InputType, IntermediateType]:
        return self.base

    @property
    def extend_function(self) -> Callable[[IntermediateType], OutputType]:
        return self.func

    @override
    def process(self, input_data: InputType) -> OutputType:
        return self.func(self.base.process(input_data))
