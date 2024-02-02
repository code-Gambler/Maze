import unittest
from graph import Graph
from mst import minimum_spanning_tree



class MST_TestCase(unittest.TestCase):
    # These are the tests cases for functions of MinHeap class

    def test_minimum_spanning_tree(self):
        the_graph = Graph(7)
        the_graph.add_edge(0,1,2)
        the_graph.add_edge(0,2,3)
        the_graph.add_edge(1,4,4)
        the_graph.add_edge(1,6,5)
        the_graph.add_edge(2,3,1)
        the_graph.add_edge(3,4,2)
        the_graph.add_edge(4,5,4)
        the_graph.add_edge(5,6,1)

        the_graph.add_edge(1,0,2)
        the_graph.add_edge(2,0,3)
        the_graph.add_edge(4,1,4)
        the_graph.add_edge(6,1,5)
        the_graph.add_edge(3,2,1)
        the_graph.add_edge(4,3,2)
        the_graph.add_edge(5,4,4)
        the_graph.add_edge(6,5,1)


        correct = [(2, 3), (5, 6), (0, 1), (3, 4), (0, 2), (4, 5)]

        mst = minimum_spanning_tree(the_graph)

        for i in range(len(mst)):
            if mst[i][0] > mst[i][1]:
                mst[i] = (mst[i][1],mst[i][0])

        correct.sort()
        mst.sort()

        self.assertEqual(correct, mst)


    def test_minimum_spanning_tree2(self):
        the_graph = Graph(11)
        the_graph.add_edge(0,1,6)
        the_graph.add_edge(0,5,8)
        the_graph.add_edge(0,7,7)
        the_graph.add_edge(1,2,3)
        the_graph.add_edge(1,4,2)
        the_graph.add_edge(2,3,4)
        the_graph.add_edge(2,4,1)
        the_graph.add_edge(3,6,9)
        the_graph.add_edge(4,6,5)
        the_graph.add_edge(5,7,4)
        the_graph.add_edge(5,9,8)
        the_graph.add_edge(6,8,3)
        the_graph.add_edge(7,10,5)
        the_graph.add_edge(8,9,1)
        the_graph.add_edge(9,10,3)


        the_graph.add_edge(1,0,6)
        the_graph.add_edge(5,0,8)
        the_graph.add_edge(7,0,7)
        the_graph.add_edge(2,1,3)
        the_graph.add_edge(4,1,2)
        the_graph.add_edge(3,2,4)
        the_graph.add_edge(4,2,1)
        the_graph.add_edge(6,3,9)
        the_graph.add_edge(6,4,5)
        the_graph.add_edge(7,5,4)
        the_graph.add_edge(9,5,8)
        the_graph.add_edge(8,6,3)
        the_graph.add_edge(10,7,5)
        the_graph.add_edge(9,8,1)
        the_graph.add_edge(10,9,3)



        correct = [(2,4),(8,9),(1,4),(9,10),(6,8),(5,7),(2,3),(4,6),(7,10),(0,1)]

        mst = minimum_spanning_tree(the_graph)


        for i in range(len(mst)):
            if mst[i][0] > mst[i][1]:
                mst[i] = (mst[i][1],mst[i][0])

        correct.sort()
        mst.sort()

        self.assertEqual(correct, mst)


        



if __name__ == '__main__':
    unittest.main()
