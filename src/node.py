from abc import abstractmethod, ABC
from typing import Generic, TypeVar, Optional
from src.lib.lrucache import LRUCache

InputType = TypeVar('InputType')
OutputType = TypeVar('OutputType')

class Node(Generic[InputType, OutputType], ABC):
    """
    Abstract base class for processing nodes. 
    """
    def __init__(self, _cache_enabled: bool = True) -> None:
        self._cache: LRUCache[InputType, OutputType] = LRUCache()

        # Cut-off value for propagating changes, only applicable
        # to float/int types for OutputType.
        self._cut_off: Optional[float] = None

        self._cache_enabled: bool = _cache_enabled
    
    def process(self, input_data: InputType) -> OutputType: 
        """
        Top level method to process input data. Contains common
        caching logic across all node types.
        """
        if not self.cache_enabled:
            return self._process(input_data)

        if input_data not in self.cache:
            self.cache[input_data] = self._process(input_data)

        assert (value := self.cache[input_data]) is not None
        return value

    @abstractmethod 
    def _process(self, input_data: InputType) -> OutputType:
        raise NotImplementedError("Subclasses should implement this method.")
    
    @property
    def cut_off(self) -> Optional[float]:
        return self._cut_off
    
    @property
    def cache_enabled(self) -> bool:
        return self._cache_enabled
    
    @property
    def cache(self) -> LRUCache[InputType, OutputType]:
        return self._cache

