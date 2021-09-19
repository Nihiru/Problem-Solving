from collections import defaultdict


class BreadthFirstSearchGraph:

    def __init__(self, val=0, neighbors=[]) -> None:
        self.val = val
        self.neighbors = neighbors
        # self.graph = {val: neighbors} # for efficiency

    def attach_vertices(self, source_vertex: 'BreadthFirstSearchGraph', dest_vertex: 'BreadthFirstSearchGraph', weight: 'int'):
        # check if the source vertex is present in the graph
        attaching_node = self.get_existing_node(source_vertex)
        if attaching_node:
            pass
        else:
            attaching_node.append(
                BreadthFirstSearchGraph(
                    dest_vertex.val, dest_vertex.neighbors
                )
            )

        # check if the destination vertex is present in the graph

    def get_existing_node(self, find_node):
        """
        Check if a node exists in the given graph or not
        Search the entire graph using breadth-first-traverse approach
        """
        graph_copy = self
        found = False
        while(True):
            if graph_copy.val == find_node.val:
                found = True
                break
            else:
                for neighbor in graph_copy.neighbors:
                    graph_copy = neighbor
                    continue
        if found:
            return graph_copy
        return None
