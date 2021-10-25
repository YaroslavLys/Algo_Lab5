import unittest
from graph import Graph


class TestGraph(unittest.TestCase):

    def test1_prim_mst(self):
        g = Graph(5)
        g.add_edge(0, 1, w=2)
        g.add_edge(1, 2, w=12)
        g.add_edge(2, 3, w=10)
        g.add_edge(3, 0, w=40)
        g.add_edge(1, 3, w=1)
        g.add_edge(1, 0, w=2)
        g.add_edge(2, 1, w=12)
        g.add_edge(3, 2, w=10)
        g.add_edge(0, 3, w=40)
        g.add_edge(3, 1, w=1)
        self.assertEqual(g.prim_mst(0), 13)

    def test2_prim_mst(self):
        g = Graph(4)
        g.add_edge(0, 1, w=99)
        g.add_edge(1, 2, w=1)
        g.add_edge(2, 3, w=1)
        g.add_edge(3, 1, w=1)
        g.add_edge(0, 2, w=100)
        g.add_edge(0, 3, w=100)
        g.add_edge(1, 0, w=99)
        g.add_edge(2, 1, w=1)
        g.add_edge(3, 2, w=1)
        g.add_edge(1, 3, w=1)
        g.add_edge(2, 0, w=100)
        g.add_edge(3, 0, w=100)
        self.assertEqual(g.prim_mst(2), 101)
