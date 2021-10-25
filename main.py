from graph import *


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(0, 1, w=2)
    g.add_edge(0, 2, w=6)
    g.add_edge(0, 3, w=4)
    g.add_edge(0, 4, w=4)
    g.add_edge(0, 5, w=4)
    g.add_edge(4, 5, w=1)
    g.add_edge(1, 0, w=2)
    g.add_edge(2, 0, w=6)
    g.add_edge(3, 0, w=4)
    g.add_edge(4, 0, w=4)
    g.add_edge(5, 0, w=4)
    g.add_edge(5, 4, w=1)
    print(g.prim_mst(5))
