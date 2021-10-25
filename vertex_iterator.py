class VertexIterator:
    def __init__(self, vertex):
        self.element = vertex.first

    def __next__(self):
        if self.element is None:
            raise StopIteration()
        it = self.element
        self.element = self.element.next
        return it
