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

    def clone_graph(self, approach, node: 'Node') -> 'Node':
        # perform a deep clone with the array via Bread First Search

        clone = {}
        # this just works for one node with its neighbor

        # if node.val not in clone:
        #     clone[node.val] = []

        # if len(node.neighbors):
        #     for neighbor in node.neighbors:
        #         clone[node.val].append(neighbor.val)

        # using inner function to perform a recursive(DFS)
        def dfs(node):
            if node.val in clone:
                return clone[node.val]
            # initializing an object from an existing graph object of type `Node`
            newly_created_node = Node(node.val)
            clone[node.val] = newly_created_node
            for nei in node.neighbors:
                newly_created_node.neighbors.append(dfs(nei))
            return newly_created_node

        stack = []

        def bfs(node):
            # since graph may contain cycles, a boolean visited array is used
            pass

        if approach == 1:
            return dfs(node) if node else None
        else:
            return bfs(node) if node else None


root_graph = Node(1)
root_graph.add_neighbors([2, 3])
root_graph.neighbors[0].add_neighbors([1, 4])
root_graph.neighbors[1].add_neighbors([1, 4])
root_graph.clone_graph(1, root_graph)
