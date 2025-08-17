from typing import Callable, ParamSpec, TypeVar, Tuple, FrozenSet, Any, TypeVarTuple
from src.lib.lrucache import LRUCache

P = ParamSpec('P')
OutputType = TypeVar('OutputType')

def cache(func: Callable[P, OutputType]) -> Callable[P, OutputType]:
    """
    A decorator that caches the result of a function call.
    
    This is a simple implementation that uses a dictionary to store results.

    We also include print statements to indicate when the cache is being used
    for debugging purposes.
    """
    cache_dict = LRUCache[Any, OutputType]()

    def wrapper(*args: P.args, **kwargs: P.kwargs) -> OutputType:
        kwargs_items = frozenset(kwargs.items())
        key = (args, kwargs_items)
        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)
        else:
            print(f"Cache hit for {func.__qualname__} with args: {args}, kwargs: {kwargs}")

        # Ensure that mypy recognizes that the value is not None
        assert (value := cache_dict[key]) is not None
        return value

    return wrapper
