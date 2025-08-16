from src.node import Node
from src.bind import Bind
from src.extend import Extend
from src.fanout import Fanout
from src.combine import Combine
from src.leaf import Leaf

from typing import TypeVar, get_args, get_type_hints, Any

InputType = TypeVar("InputType")
OutputType = TypeVar("OutputType")

def process_graph_from_leaves(node: Node[InputType, OutputType]) -> OutputType:
    """
    Process the graph starting from the leaf nodes. Essentially feeds in the None values
    to the leaf nodes, assuming all the base nodes are leaves. This is needed as the
    input structure depends on how the graph was constructed, i.e. a graph with 3 leaves
    could require ((None, None), None) or (None, (None, None)).
    """

    def _get_structured_none(node: Node[InputType, OutputType]) -> Any:
        if isinstance(node, Leaf):
            return None
        if isinstance(node, Bind) or isinstance(node, Extend) or isinstance(node, Fanout):
            return _get_structured_none(node.base_node)
        if isinstance(node, Combine):
            return (_get_structured_none(node.base_node_one),
                    _get_structured_none(node.base_node_two))
        return None

    return node.process(_get_structured_none(node))
