import unittest
from setList import SetList


class SetList_TestCase(unittest.TestCase):
	"""These are the tests cases for functions and classes of a1_partb"""

	def test_Init_And_Len(self):
		the_list = SetList()

		self.assertEqual(len(the_list), 0)
		self.assertEqual(the_list.get_front(), None)
		self.assertEqual(the_list.get_back(), None)

	def test_Make_Set(self):
		list1 = SetList()
		list2 = SetList()

		node = list1.make_set("cat")
		self.assertEqual(list1.get_front(), node)
		self.assertEqual(list1.get_back(), node)
		self.assertEqual(node.get_next(), None)
		self.assertEqual(node.get_previous(), None)
		self.assertEqual(node.get_data(), "cat")
		self.assertEqual(node.get_set(), list1)
		self.assertEqual(len(list1), 1)

		node2 = list2.make_set("dog")
		self.assertEqual(list2.get_front(), node2)
		self.assertEqual(list2.get_back(), node2)
		self.assertEqual(node2.get_next(), None)
		self.assertEqual(node2.get_previous(), None)
		self.assertEqual(node2.get_data(), "dog")
		self.assertEqual(node2.get_set(), list2)
		self.assertEqual(len(list2), 1)

		node3 = list2.make_set("fish")
		self.assertEqual(node3, None)
		self.assertEqual(list2.get_front(), node2)
		self.assertEqual(list2.get_back(), node2)
		self.assertEqual(node2.get_next(), None)
		self.assertEqual(node2.get_previous(), None)
		self.assertEqual(node2.get_data(), "dog")
		self.assertEqual(node2.get_set(), list2)
		self.assertEqual(len(list2), 1)

	def test_Representative_Node(self):
		list1 = SetList()
		list2 = SetList()

		self.assertEqual(list1.representative_node(), None)

		self.assertEqual(list2.representative_node(), None)

		node = list1.make_set("cat")
		self.assertEqual(list1.representative_node(), node)
		self.assertEqual(list1.representative_node(), list1.get_front())
		self.assertEqual(list1.representative_node(), list1.get_back())

		node = list2.make_set("dog")
		self.assertEqual(list2.representative_node(), node)
		self.assertEqual(list2.representative_node(), list2.get_front())
		self.assertEqual(list2.representative_node(), list2.get_back())

	def test_Representative(self):
		list1 = SetList()
		list2 = SetList()
		self.assertEqual(list1.representative(), None)
		self.assertEqual(list2.representative(), None)
		node = list1.make_set("cat")
		self.assertEqual(list1.representative(), "cat")
		node = list2.make_set("dog")
		self.assertEqual(list2.representative(), "dog")

	def test_Union_Set(self):
		list1 = SetList()
		list2 = SetList()
		list3 = SetList()

		node1 = list1.make_set("cat")
		node2 = list2.make_set("dog")
		node3 = list3.make_set("fish")

		list1.union_set(list2)

		self.assertEqual(list2.get_front(), None)
		self.assertEqual(list2.get_back(), None)
		self.assertEqual(len(list2), 0)

		self.assertNotEqual(list1.get_front(), list1.get_back())
		self.assertEqual(len(list1), 2)

		self.assertEqual(node1.get_set(), list1)
		self.assertEqual(node2.get_set(), list1)

		rep = list1.representative_node()
		self.assertEqual(list1.representative(), rep.get_data())

		list3.union_set(list1)

		self.assertEqual(node1.get_set(), list3)
		self.assertEqual(node2.get_set(), list3)
		self.assertEqual(node3.get_set(), list3)

		self.assertEqual(list1.get_front(), None)
		self.assertEqual(list1.get_back(), None)
		self.assertEqual(len(list1), 0)

		self.assertNotEqual(list3.get_front(), list3.get_back())
		self.assertEqual(len(list3), 3)

		rep = list3.representative_node()
		self.assertEqual(list3.representative(), rep.get_data())

		list1.union_set(list3)

		self.assertEqual(node1.get_set(), list1)
		self.assertEqual(node2.get_set(), list1)
		self.assertEqual(node3.get_set(), list1)

		self.assertEqual(list3.get_front(), None)
		self.assertEqual(list3.get_back(), None)
		self.assertEqual(len(list3), 0)

		self.assertNotEqual(list1.get_front(), list1.get_back())
		self.assertEqual(len(list1), 3)

		rep = list1.representative_node()
		self.assertEqual(list1.representative(), rep.get_data())

	def test_Find_Data(self):
		list1 = SetList()
		list2 = SetList()
		list3 = SetList()

		node1 = list1.make_set("cat")
		node2 = list2.make_set("dog")
		node3 = list3.make_set("fish")

		list1.union_set(list2)

		list3.union_set(list1)

		result = list3.find_data("cat")
		self.assertEqual(result, node1)
		self.assertEqual(result.get_set(), list3)

		result = list3.find_data("dog")
		self.assertEqual(result, node2)
		self.assertEqual(result.get_set(), list3)

		result = list3.find_data("fish")
		self.assertEqual(result, node3)
		self.assertEqual(result.get_set(), list3)


if __name__ == '__main__':
	unittest.main()