from abc import abstractmethod, ABC
from typing import Generic, TypeVar

InputType = TypeVar('InputType')
OutputType = TypeVar('OutputType')

class Node(Generic[InputType, OutputType], ABC):
    """
    Abstract base class for processing nodes. 
    """

    @abstractmethod 
    def process(self, input_data: InputType) -> OutputType:
        raise NotImplementedError("Subclasses should implement this method.")
