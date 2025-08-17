from src.bind import Bind
from src.combine import Combine
from src.extend import Extend
from src.fanout import Fanout
from src.leaf import Leaf
from src.node import Node
from src.function import Function
import time

from src.utils import process_graph_from_leaves

def sum(x, y):
    time.sleep(2)
    return x + y

def main():
    #make a graph that goes from 4 inputs to 2, to 1

    leaf1 = Leaf(1)
    leaf2 = Leaf(-2)
    leaf3 = Leaf(3)
    leaf4 = Leaf(4)

    comb = Combine(leaf1, leaf2, sum)
    comb2= Combine(leaf3, leaf4, sum)

    final_node = Combine(comb, comb2, sum)

    # time first
    start = time.perf_counter()
    x = process_graph_from_leaves(final_node)
    end = time.perf_counter()
    print(f"First run took {end - start:.4f} seconds")

    start = time.perf_counter()
    y = process_graph_from_leaves(final_node)
    end = time.perf_counter()
    print(f"Second run took {end - start:.4f} seconds")
    assert x == y
    
if __name__ == "__main__":
    main()
