from vertex_iterator import VertexIterator


class Vertex:
    def __init__(self, value):
        self.value = value
        self.first = self.last = None

    def __iter__(self):
        return VertexIterator(self)
