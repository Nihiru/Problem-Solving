""" 
Topological Sorting:
    1) For Directed Acylic Graph is a linear ordering of vertices such that for every directed edge u, v vertex u comes
        before v in the ordering
    2) Topological sorting for a graph is not possible if the graph is not a DAG
    3) A topological sort is a graph traversal in which each node v is visited only after all its dependencies are visited.
"""

from collections import defaultdict


class Graph:
    def __init__(self, vertices) -> None:
        self.graph = defaultdict(list)
        self.total_vertices = vertices

    # function to add an edge to a graph
    def addEdge(self, source_vertex, dest_vertex):
        self.graph[source_vertex].append(dest_vertex)

    def topologicalSortUtil(self, vertex, visited, stack):
        visited[vertex] = True
        for i in self.graph[vertex]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        stack.append(vertex)

    def topologicalSort(self,):
        """ 
        At first all the vertices are marked as not visited
        We declare a visited array for avoiding re-visiting an vertice when going down the graph
        """
        visited = [False] * self.total_vertices
        stack = []  # it would hold the topological ordering of the nodes
        for i in range(self.total_vertices):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        print(stack)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g.topologicalSort()
""" 
Abstraction:
    1) Output from topological sorting can be seen as starting from Maximum outgoing edges to Minimum outgoing edges
    2) Stack data structure is used to represent the ordering
        1) Front of the stack represents the Maximum outgoing edges
        2) Rear of the stack represents the Minimum / No outgoing edges

Applications:
    1) Scheduling a sequence of jobs or tasks based on their dependencies.
"""
