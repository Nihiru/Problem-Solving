from typing import ItemsView, List


def canFinish(numCourse: int, prerequisites: List[List[int]]) -> str:
    visited = []
    vertices = {}

    """
    Data Representation Phase
    """
    # counting the total number of vertices
    for i in prerequisites:
        # phase for creating an edge
        source_vertex = i[0]
        if source_vertex not in vertices:
            vertices[source_vertex] = []
        # else clause is executed when there an edge exists
        dest_vertex = i[1]
        if dest_vertex not in vertices[source_vertex]:
            vertices[source_vertex].append(dest_vertex)

    print(vertices)

    """
    Operational Phase
    """
    acyclic = False
    if len(vertices):
        # getting the first node and its neighbors
        # graph = vertices.items()
        # pair_iterator = iter(graph)
        # node = next(pair_iterator)
        for vertex in vertices:
            if acyclic or (vertex in visited):
                acyclic = True
                break
            visited.append(vertex)
            neighbors = vertices[vertex]  # setting the starting nodes
            """
            Following loop doesn't hold good for changing neighbors values
            """
            for neighbor in neighbors:
                if neighbor in visited:
                    acyclic = True
                    break
                else:
                    visited.append(neighbor)
                    neighbors = vertices.get(neighbor)

        if acyclic:
            return "Impossible"
        else:
            return "Possible"


# print(canFinish(2, [[1, 0], [0, 1]]))  # Impossible


def course_schedule(numcourse: int, prerequisites: List[List[int]]):
    for node in numcourse:
        pass
