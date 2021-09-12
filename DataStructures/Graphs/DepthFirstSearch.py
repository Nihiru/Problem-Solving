"""
Complexity:
    1) Time Complexity: O(V+E) where V is the number of vertices and E is the number of edges in the graph.
    2) Space Complexity: O(V) where V is the number of vertices in the graph.
  
For more information
1) https://stackoverflow.com/questions/36479640/time-space-complexity-of-depth-first-search?answertab=oldest#tab-top
"""


class DepthFirstSearch:

    def __init__(self):
        self.graph = dict()

    def add_node(self, source_vertex, dest_vertex=None, edge=0):
        if source_vertex not in self.graph:
            self.graph[source_vertex] = {}
        if dest_vertex:
            if dest_vertex not in self.graph:
                self.graph[dest_vertex] = {}
            self.graph[source_vertex][dest_vertex] = edge  # edges to vertices

    def traverse(self, node, visited):
        visited.add(node)
        # for nodes that have siblings
        if len(self.graph[node]):
            print(f"Nodes visited: {node}")
            for node in self.graph[node]:
                if node not in visited:
                    self.traverse(node, visited)
        # for leaf nodes and nodes that don't have siblings
        else:
            print(f"Nodes visited: {node}")

    def view_graph(self):
        if len(self.graph):
            for key, values in self.graph.items():
                print(f"Node: {key} connected nodes: {values}")
        else:
            print("Empty dictionary")


if __name__ == "__main__":
    node_set = set()
    dfs_obj = DepthFirstSearch()
    # dfs_obj.view_graph() # Empty dictionary
    dfs_obj.add_node(1, 2, 1)
    dfs_obj.add_node(1, 3, 2)
    dfs_obj.add_node(2, 4, 2)
    dfs_obj.add_node(3, 5, 3)
    dfs_obj.add_node(3, 7, 5)
    dfs_obj.add_node(4, 5, 2)
    dfs_obj.add_node(5, 6, 5)
    dfs_obj.add_node(9)
    dfs_obj.traverse(1, node_set)
    # dfs_obj.view_graph()

    # to find out if any disjoint node is present in the graph
    disjoint_node = set(list(dfs_obj.graph)) - node_set
    if disjoint_node:
        print(f"Disjoint node: {list(disjoint_node)[0]}")
