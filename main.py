from src.bind import Bind
from src.combine import Combine
from src.extend import Extend
from src.fanout import Fanout
from src.leaf import Leaf
from src.node import Node

from src.utils import process_graph_from_leaves

def main():
    #make a graph that goes from 4 inputs to 2, to 1

    leaf1 = Leaf(1)
    leaf2 = Leaf(2)
    leaf3 = Leaf(3)

    combine_node = Combine(leaf1, leaf2, lambda x, y: x + y)
    extend_1 = Extend(leaf3, lambda x: x * 2)
    extend_2 = Extend(leaf3, lambda x: x + 10)
    comb_2 = Combine(extend_1, extend_2, lambda x, y: x - y)

    final_node = Combine(combine_node, comb_2, lambda x, y: x + y)

    print(process_graph_from_leaves(final_node))
    
if __name__ == "__main__":
    main()
