from queue import PriorityQueue

from edge import Edge
from vertex import Vertex


class Graph:
    def __init__(self, v):
        self.number_of_vertexes = v
        self.vertexes = [Vertex(i) for i in range(v)]
        self.edges = []

    def add_edge(self, vertex_from, vertex_to, **kwargs):
        self.edges.append(Edge(self.vertexes[vertex_from], self.vertexes[vertex_to], **kwargs))

    def prim_mst(self, vertex_start):
        q = PriorityQueue()
        visited = [False for _ in range(self.number_of_vertexes)]
        q.put((0, vertex_start))
        result = 0
        while not q.empty():
            element = q.get()
            if visited[element[1]]:
                continue
            visited[element[1]] = True
            result += element[0]
            for edge in self.vertexes[element[1]]:
                if not visited[edge.successor.value]:
                    q.put((edge.weight, edge.successor.value))
        if visited:
            return result
        else:
            return -1
