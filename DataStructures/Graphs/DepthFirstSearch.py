class DepthFirstSearch:

    def __init__(self):
        self.graph = dict()

    def add_node(self, u, v, w=0):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append({
            v: w
        })

    def traverse(self, node=None):
        visited = []
        if len(self.graph):
            for key, values in self.graph.items():
                if len(values):
                    for next_node in values:
                        if next_node not in visited:
                            pass
        else:
            return "Empty graph"

    def view_graph(self):
        if len(self.graph):
            for key, values in self.graph.items():
                print(f"Node: {key} connected nodes: {values}")
        else:
            print("Empty dictionary")


dfs_obj = DepthFirstSearch()
dfs_obj.view_graph()
dfs_obj.add_node(1, 2, 1)
dfs_obj.add_node(1, 3, 2)
dfs_obj.add_node(2, 4, 2)
dfs_obj.add_node(3, 5, 3)
dfs_obj.add_node(4, 5, 2)
dfs_obj.add_node(5, 6, 5)

dfs_obj.view_graph()
