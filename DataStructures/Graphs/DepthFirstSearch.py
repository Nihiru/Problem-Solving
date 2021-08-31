class DepthFirstSearch:

    def __init__(self):
        self.graph = dict()

    def add_node(self, u, v, w=0):
        if u not in self.graph:
            self.graph[u] = []
        else:
            self.graph[u].append({
                v: w
            })

    def calculate_nodes_in_graph(self):
        pass

    def view_graph(self):
        for keys, values in self.graph.items():
            pass


dfs_obj = DepthFirstSearch()
dfs_obj.add_node()