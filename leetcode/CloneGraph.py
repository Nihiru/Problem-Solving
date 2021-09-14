"""
Problem Description:
    1) Each node in the graph consists of a value(int) and a list(List[Node])
       of its neighbors
    2) Each node value is the same as the node's index.
    3) An adjacency list is used to represent a finite graph.
    4) Each list describes the set of neighbors of a node in the graph
    5) Return the copy of the given node as a reference to the cloned graph.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def add_neighbors(self, nodes):
        for node in nodes:
            self.neighbors.append(Node(node))


def clone_graph(root_graph: 'Node') -> 'Node':
    # perform a deep clone with the array via Bread First Search
    print(root_graph)


root_graph = Node(1)
root_graph.add_neighbors([2, 3])
clone_graph(root_graph)
