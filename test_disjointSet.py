import unittest

from disjointSet import DisjointSet


class DisjointSet_Testcase(unittest.TestCase):
	"""These are the tests cases for functions and classes of a1_partb"""

	def test_Init_Len_NumSets(self):
		the_set = DisjointSet()
		self.assertEqual(len(the_set), 0)
		self.assertEqual(the_set.get_num_sets(), 0)

	def test_Make_Set(self):
		the_set = DisjointSet()
		rc1 = the_set.make_set("cat")
		self.assertEqual(len(the_set), 1)
		self.assertEqual(the_set.get_num_sets(), 1)
		self.assertEqual(rc1, True)

		rc2 = the_set.make_set("dog")
		self.assertEqual(len(the_set), 2)
		self.assertEqual(the_set.get_num_sets(), 2)
		self.assertEqual(rc2, True)

		rc3 = the_set.make_set("fish")
		self.assertEqual(len(the_set), 3)
		self.assertEqual(the_set.get_num_sets(), 3)
		self.assertEqual(rc3, True)

		rc1 = the_set.make_set("cat")
		self.assertEqual(len(the_set), 3)
		self.assertEqual(the_set.get_num_sets(), 3)
		self.assertEqual(rc1, False)

		rc2 = the_set.make_set("dog")
		self.assertEqual(len(the_set), 3)
		self.assertEqual(the_set.get_num_sets(), 3)
		self.assertEqual(rc2, False)

		rc3 = the_set.make_set("fish")
		self.assertEqual(len(the_set), 3)
		self.assertEqual(the_set.get_num_sets(), 3)
		self.assertEqual(rc3, False)

	def test_Find_Set(self):
		the_set = DisjointSet()
		the_set.make_set("cat")
		the_set.make_set("dog")
		the_set.make_set("fish")
		self.assertEqual(the_set.find_set("cat"), "cat")
		self.assertEqual(the_set.find_set("dog"), "dog")
		self.assertEqual(the_set.find_set("fish"), "fish")

	def test_Get_Set_Size(self):
		the_set = DisjointSet()
		the_set.make_set("cat")
		the_set.make_set("dog")
		the_set.make_set("fish")
		self.assertEqual(the_set.get_set_size("cat"), 1)
		self.assertEqual(the_set.get_set_size("dog"), 1)
		self.assertEqual(the_set.get_set_size("fish"), 1)
		self.assertEqual(the_set.get_set_size("hamster"), 0)

	def test_Union_Set(self):
		the_set = DisjointSet()
		the_set.make_set("cat")
		the_set.make_set("dog")
		the_set.make_set("fish")
		rc = the_set.union_set("cat", "dog")
		self.assertEqual(rc, True)
		self.assertEqual(the_set.find_set("cat"), the_set.find_set("dog"))
		self.assertNotEqual(the_set.find_set("fish"), the_set.find_set("dog"))
		self.assertNotEqual(the_set.find_set("fish"), the_set.find_set("cat"))
		self.assertEqual(len(the_set), 3)
		self.assertEqual(the_set.get_num_sets(), 2)
		self.assertEqual(the_set.get_set_size("cat"), 2)
		self.assertEqual(the_set.get_set_size("dog"), 2)
		self.assertEqual(the_set.get_set_size("fish"), 1)

		the_set.make_set("hamster")
		the_set.make_set("turtle")
		the_set.make_set("frog")
		the_set.make_set("gerbil")
		self.assertEqual(len(the_set), 7)
		self.assertEqual(the_set.get_num_sets(), 6)
		rc = the_set.union_set("turtle", "frog")
		self.assertEqual(rc, True)
		self.assertEqual(len(the_set), 7)
		self.assertEqual(the_set.get_num_sets(), 5)

		self.assertEqual(the_set.find_set("turtle"), the_set.find_set("frog"))
		self.assertNotEqual(the_set.find_set("hamster"), the_set.find_set("frog"))
		self.assertNotEqual(the_set.find_set("dog"), the_set.find_set("turtle"))
		self.assertNotEqual(the_set.find_set("gerbil"), the_set.find_set("turtle"))
		self.assertNotEqual(the_set.find_set("cat"), the_set.find_set("frog"))
		self.assertNotEqual(the_set.find_set("fish"), the_set.find_set("frog"))

		self.assertEqual(the_set.get_set_size("hamster"), 1)
		self.assertEqual(the_set.get_set_size("turtle"), 2)
		self.assertEqual(the_set.get_set_size("frog"), 2)
		self.assertEqual(the_set.get_set_size("gerbil"), 1)

		rc = the_set.union_set("fish", "frog")
		self.assertEqual(rc, True)
		self.assertEqual(len(the_set), 7)
		self.assertEqual(the_set.get_num_sets(), 4)
		self.assertEqual(the_set.find_set("frog"), the_set.find_set("fish"))
		self.assertEqual(the_set.find_set("turtle"), the_set.find_set("fish"))
		self.assertEqual(the_set.get_set_size("frog"), 3)
		self.assertEqual(the_set.get_set_size("fish"), 3)
		self.assertEqual(the_set.get_set_size("turtle"), 3)

		rc = the_set.union_set("fish", "turtle")
		self.assertEqual(rc, False)
		self.assertEqual(len(the_set), 7)
		self.assertEqual(the_set.get_num_sets(), 4)
		self.assertEqual(the_set.find_set("frog"), the_set.find_set("fish"))
		self.assertEqual(the_set.find_set("turtle"), the_set.find_set("fish"))
		self.assertEqual(the_set.get_set_size("frog"), 3)
		self.assertEqual(the_set.get_set_size("fish"), 3)
		self.assertEqual(the_set.get_set_size("turtle"), 3)

		rc = the_set.union_set("fish", "cat")
		self.assertEqual(rc, True)
		self.assertEqual(len(the_set), 7)
		self.assertEqual(the_set.get_num_sets(), 3)
		self.assertEqual(the_set.find_set("frog"), the_set.find_set("cat"))
		self.assertEqual(the_set.find_set("turtle"), the_set.find_set("dog"))
		self.assertEqual(the_set.find_set("fish"), the_set.find_set("dog"))
		self.assertEqual(the_set.get_set_size("frog"), 5)
		self.assertEqual(the_set.get_set_size("fish"), 5)
		self.assertEqual(the_set.get_set_size("turtle"), 5)
		self.assertEqual(the_set.get_set_size("cat"), 5)
		self.assertEqual(the_set.get_set_size("dog"), 5)
		self.assertEqual(the_set.get_set_size("hamster"), 1)
		self.assertEqual(the_set.get_set_size("gerbil"), 1)


if __name__ == '__main__':
	unittest.main()