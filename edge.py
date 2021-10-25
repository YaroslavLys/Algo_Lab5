class Edge:
    def __init__(self, predecessor, successor, **kwargs):
        if predecessor.first is None:
            predecessor.first = self
        else:
            predecessor.last.next = self
        predecessor.last = self
        self.successor = successor
        self.next = None
        self.weight = kwargs['w']
