#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of assingment 2
#   To use this, run: python test_a2d.py

import unittest
from graph import Graph


class Graph_TestCase(unittest.TestCase):
	"""These are the tests cases for functions and classes of a2"""

	def test_init(self):
		the_graph = Graph(10)
		self.assertEqual(the_graph.num_edges(), 0)
		self.assertEqual(the_graph.num_verts(), 10)

	def test_add_vertex(self):
		the_graph = Graph(10)
		the_graph.add_vertex()
		self.assertEqual(the_graph.num_verts(), 11)
		the_graph.add_vertex()
		self.assertEqual(the_graph.num_verts(), 12)

	def test_add_edge(self):
		the_graph = Graph(10)

		rc = the_graph.add_edge(0, 10)
		self.assertEqual(rc, False)

		rc = the_graph.add_edge(10, 7)
		self.assertEqual(rc, False)

		rc = the_graph.add_edge(-1, 10)
		self.assertEqual(rc, False)

		rc = the_graph.add_edge(12, 10)
		self.assertEqual(rc, False)

		the_graph.add_vertex()
		self.assertEqual(the_graph.num_verts(), 11)

		rc = the_graph.add_edge(0, 10, 5)
		self.assertEqual(rc, True)

		rc = the_graph.add_edge(10, 7)
		self.assertEqual(rc, True)

		rc = the_graph.add_edge(12, 10)
		self.assertEqual(rc, False)

		rc = the_graph.add_edge(0, 10)
		self.assertEqual(rc, False)

		rc = the_graph.add_edge(10, 7, 3)
		self.assertEqual(rc, False)

		rc = the_graph.add_edge(7, 10, 3)
		self.assertEqual(rc, True)

		for i in range(0, 10):
			rc = the_graph.add_edge(0, i)
			self.assertEqual(rc, True)

	def test_num_edges(self):

		the_graph = Graph(10)

		rc = the_graph.add_edge(0, 10)
		self.assertEqual(the_graph.num_edges(), 0)

		rc = the_graph.add_edge(10, 7)
		self.assertEqual(the_graph.num_edges(), 0)

		rc = the_graph.add_edge(-1, 10)
		self.assertEqual(the_graph.num_edges(), 0)

		rc = the_graph.add_edge(12, 10)
		self.assertEqual(the_graph.num_edges(), 0)

		the_graph.add_vertex()
		self.assertEqual(the_graph.num_verts(), 11)

		rc = the_graph.add_edge(0, 10, 5)
		self.assertEqual(the_graph.num_edges(), 1)

		rc = the_graph.add_edge(10, 7)
		self.assertEqual(the_graph.num_edges(), 2)

		rc = the_graph.add_edge(12, 10)
		self.assertEqual(the_graph.num_edges(), 2)

		rc = the_graph.add_edge(0, 10)
		self.assertEqual(the_graph.num_edges(), 2)

		rc = the_graph.add_edge(10, 7, 3)
		self.assertEqual(the_graph.num_edges(), 2)

		rc = the_graph.add_edge(7, 10, 3)
		self.assertEqual(the_graph.num_edges(), 3)

		for i in range(0, 11):
			rc = the_graph.add_edge(0, i)

		self.assertEqual(the_graph.num_edges(), 13)

	def test_num_edges_2(self):
		the_graph = Graph(10)

		rc = the_graph.add_edge(0, 10, 3)
		rc = the_graph.add_edge(10, 7, 5)
		rc = the_graph.add_edge(-1, 10, 1)
		rc = the_graph.add_edge(12, 10)
		the_graph.add_vertex()

		self.assertEqual(the_graph.num_edges(), 0)

		for i in range(0, 11):
			rc = the_graph.add_edge(0, i)

		self.assertEqual(the_graph.num_edges(), 11)

		rc = the_graph.add_edge(0, 5, 5)
		self.assertEqual(the_graph.num_edges(), 11)

		for i in range(1, 11):
			rc = the_graph.add_edge(i, 5, 5)

		self.assertEqual(the_graph.num_edges(), 21)

		rc = the_graph.add_edge(10, 11, 3)
		self.assertEqual(the_graph.num_edges(), 21)

		rc = the_graph.add_edge(11, 10, 3)
		self.assertEqual(the_graph.num_edges(), 21)

		the_graph.add_vertex()
		rc = the_graph.add_edge(10, 11, 3)
		self.assertEqual(the_graph.num_edges(), 22)

		rc = the_graph.add_edge(11, 10, 4)
		self.assertEqual(the_graph.num_edges(), 23)

		rc = the_graph.add_edge(10, 11, 5)
		self.assertEqual(the_graph.num_edges(), 23)

	def test_has_edge(self):
		the_graph = Graph(10)

		rc = the_graph.add_edge(0, 10, 3)
		rc = the_graph.add_edge(10, 7, 5)
		rc = the_graph.add_edge(-1, 10, 1)
		rc = the_graph.add_edge(12, 10)
		the_graph.add_vertex()

		# graph should be empty at this point, no vertices, no edges
		for i in range(0, 11):
			for j in range(0, 11):
				self.assertEqual(the_graph.has_edge(i, j), False)

		for i in range(0, 11):
			rc = the_graph.add_edge(0, i)

		for i in range(1, 11):
			for j in range(0, 11):
				self.assertEqual(the_graph.has_edge(i, j), False)

		for i in range(0, 11):
			self.assertEqual(the_graph.has_edge(0, j), True)

		rc = the_graph.add_edge(0, 5, 5)
		self.assertEqual(the_graph.has_edge(0, 5), True)

		for i in range(1, 11):
			rc = the_graph.add_edge(i, 5, 5)
			self.assertEqual(rc, True)

		for i in range(1, 11):
			for j in range(0, 11):
				if j != 5:
					self.assertEqual(the_graph.has_edge(i, j), False)
				else:
					self.assertEqual(the_graph.has_edge(i, j), True)

		rc = the_graph.add_edge(10, 11, 3)
		self.assertEqual(the_graph.has_edge(10, 11), False)

		rc = the_graph.add_edge(11, 10, 3)
		self.assertEqual(the_graph.has_edge(11, 10), False)

		the_graph.add_vertex()
		rc = the_graph.add_edge(10, 11, 3)
		self.assertEqual(the_graph.has_edge(10, 11), True)

		rc = the_graph.add_edge(11, 10, 4)
		self.assertEqual(the_graph.has_edge(11, 10), True)

		rc = the_graph.add_edge(10, 11, 5)
		self.assertEqual(the_graph.has_edge(10, 11), True)

	def test_edge_weight(self):
		the_graph = Graph(10)

		rc = the_graph.add_edge(0, 10, 3)
		rc = the_graph.add_edge(10, 7, 5)
		rc = the_graph.add_edge(-1, 10, 1)
		rc = the_graph.add_edge(12, 10)
		the_graph.add_vertex()

		# graph should be empty at this point, no vertices, no edges
		for i in range(0, 11):
			for j in range(0, 11):
				self.assertEqual(the_graph.edge_weight(i, j), None)

		for i in range(0, 11):
			rc = the_graph.add_edge(0, i)

		for i in range(1, 11):
			for j in range(0, 11):
				self.assertEqual(the_graph.edge_weight(i, j), None)

		for i in range(0, 11):
			self.assertEqual(the_graph.edge_weight(0, j), True)

		rc = the_graph.add_edge(0, 5, 5)
		self.assertEqual(the_graph.edge_weight(0, 5), 1)

		for i in range(1, 11):
			rc = the_graph.add_edge(i, 5, 5)

		for i in range(1, 11):
			for j in range(0, 11):
				if j != 5:
					self.assertEqual(the_graph.edge_weight(i, j), None)
				else:
					self.assertEqual(the_graph.edge_weight(i, j), 5)

		rc = the_graph.add_edge(10, 11, 3)
		self.assertEqual(the_graph.edge_weight(10, 11), None)

		rc = the_graph.add_edge(11, 10, 3)
		self.assertEqual(the_graph.edge_weight(11, 10), None)

		the_graph.add_vertex()

		rc = the_graph.add_edge(10, 11, 3)
		self.assertEqual(the_graph.edge_weight(10, 11), 3)

		rc = the_graph.add_edge(11, 10, 4)
		self.assertEqual(the_graph.edge_weight(11, 10), 4)

		rc = the_graph.add_edge(10, 11, 5)
		self.assertEqual(the_graph.edge_weight(10, 11), 3)

	def test_get_connected(self):
		the_graph = Graph(12)

		the_graph.add_edge(0, 5, 5)
		the_graph.add_edge(2, 6)
		the_graph.add_edge(7, 3)
		the_graph.add_edge(0, 4, 6)
		the_graph.add_edge(2, 10, 7)
		the_graph.add_edge(2, 3)
		the_graph.add_edge(6, 2, 4)
		the_graph.add_edge(7, 2, 3)
		the_graph.add_edge(3, 2, 6)
		the_graph.add_edge(8, 2, 5)
		the_graph.add_edge(10, 11, 2)
		the_graph.add_edge(6, 5)
		the_graph.add_edge(9, 3)
		the_graph.add_edge(7, 6, 5)

		result = [[(4, 6), (5, 5)], [], [(3, 1), (10, 7), (6, 1)], [(2, 6)], [], [], [(2, 4), (5, 1)],
		          [(3, 1), (2, 3), (6, 5)], [(2, 5)], [(3, 1)], [(11, 2)], []]

		for i in range(0, 12):
			edges = the_graph.get_connected(i)
			self.assertEqual(set(result[i]) == set(edges), True)


if __name__ == '__main__':
	unittest.main()