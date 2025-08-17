from typing import Generic, TypeVar, Callable
from typing_extensions import override
from src.node import Node


InputType = TypeVar('InputType')
IntermediateType = TypeVar('IntermediateType')
OutputType = TypeVar('OutputType')


class Bind(Node[InputType, OutputType], 
           Generic[InputType, IntermediateType, OutputType]):
    """ 
    Represents a processing node that is the equivalent of a bind operation,
    allowing for the dynamic generation of "process" based on the output of a base node.
    """

    def __init__(self, 
                 base: Node[InputType, IntermediateType], 
                 func: Callable[[IntermediateType], Node[IntermediateType, OutputType]]) -> None:
        self.base = base
        self.func = func
        super().__init__()
    
    @property
    def base_node(self) -> Node[InputType, IntermediateType]:
        return self.base

    @property
    def bind_function(self) -> Callable[[IntermediateType], Node[IntermediateType, OutputType]]:
        return self.func

    @override
    def _process(self, input_data: InputType) -> OutputType:
        return self.func(value := self.base.process(input_data)).process(value)
