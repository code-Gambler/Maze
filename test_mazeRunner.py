import unittest
from mazeRunner import find_path
from maze_v2 import Maze, print_pathfile


class MazeRunner_TestCase(unittest.TestCase):
	"""These are the tests cases for functions and classes of a1_partb"""

	def test_find_path1(self):
		the_maze = Maze("maze1.txt")
		correct = [0, 1, 7, 8, 2, 3, 4, 5, 11, 17]
		result = find_path(the_maze, 0, 17)
		print_pathfile("../test1path.txt", result, the_maze.get_num_rows(), the_maze.get_num_cols())
		self.assertEqual(len(correct), len(result))
		self.assertEqual(correct, result)

	def test_find_path2(self):
		the_maze = Maze("maze1.txt")
		correct = [8]
		result = find_path(the_maze, 8, 8)
		print_pathfile("../test2path.txt", result, the_maze.get_num_rows(), the_maze.get_num_cols())
		self.assertEqual(len(correct), len(result))
		self.assertEqual(correct, result)

	def test_find_path3(self):
		the_maze = Maze("maze1.txt")
		correct = [0, 1, 7, 8, 2, 3, 4, 5]
		result = find_path(the_maze, 0, 5)
		print_pathfile("../test3path.txt", result, the_maze.get_num_rows(), the_maze.get_num_cols())
		self.assertEqual(len(correct), len(result))
		self.assertEqual(correct, result)

	def test_find_path4(self):
		the_maze = Maze("maze2.txt")
		correct = [158, 157, 177, 197, 196, 195, 175, 174, 173, 172,
		           171, 151, 131, 111, 112, 92, 72, 52, 53, 33,
		           13, 12, 11, 10, 9, 29, 28, 27, 47, 67,
		           66, 86, 85, 84, 83, 63, 62, 42, 41]
		result = find_path(the_maze, 158, 41)
		print_pathfile("../test4path.txt", result, the_maze.get_num_rows(), the_maze.get_num_cols())
		self.assertEqual(len(correct), len(result))
		self.assertEqual(correct, result)

	def test_find_path5(self):
		the_maze = Maze("maze2.txt")
		correct = [199, 179, 178, 177, 197, 196, 195, 175, 174, 173, 172, 171, 151, 131,
		           111, 112, 92, 72, 52, 53, 33, 13, 12, 11, 10, 9, 29, 28, 27, 47, 67, 66, 86, 85, 84, 83,
		           63, 62, 42, 41, 61, 60, 40, 20, 0]
		result = find_path(the_maze, 199, 0)
		print_pathfile("../test5path.txt", result, the_maze.get_num_rows(), the_maze.get_num_cols())
		self.assertEqual(len(correct), len(result))
		self.assertEqual(correct, result)

	def test_find_path6(self):
		the_maze = Maze("maze3.txt")
		correct = [1740, 1680, 1681, 1682, 1622, 1562, 1563, 1503, 1504, 1444,
		           1443, 1383, 1382, 1381, 1321, 1322, 1323, 1324, 1264, 1204,
		           1205, 1145, 1085, 1084, 1083, 1023, 1022, 1082, 1081, 1021,
		           961, 901, 841, 842, 782, 722, 723, 724, 664, 604,
		           605, 606, 666, 667, 607, 547, 487, 488, 489, 429,
		           430, 370, 371, 372, 312, 313, 253, 254, 255, 195,
		           196, 197, 198, 199, 259, 319, 318, 317, 377, 378,
		           379, 439, 499, 498, 497, 496, 556, 616, 676, 736,
		           796, 795, 855, 915, 975, 1035, 1095, 1094, 1154, 1155,
		           1156, 1216, 1276, 1336, 1337, 1397, 1398, 1458, 1459, 1460,
		           1520, 1580, 1581, 1521, 1522, 1582, 1583, 1584, 1585, 1586,
		           1526, 1527, 1528, 1468, 1467, 1407, 1408, 1409, 1410, 1411,
		           1351, 1352, 1412, 1413, 1414, 1354, 1294, 1293, 1292, 1291,
		           1231, 1232, 1172, 1173, 1174, 1114, 1115, 1055, 1056, 996,
		           997, 998, 999, 939, 879, 878, 877, 817, 816, 815,
		           814, 754, 694, 634, 633, 632, 572, 512, 513, 514,
		           515, 516, 576, 636, 696, 756, 757, 697, 698, 638,
		           639, 579, 519, 520, 521, 522, 523, 583, 584, 585,
		           645, 646, 647, 648, 649, 650, 651, 591, 590, 530,
		           529, 469, 409, 349, 350, 290, 230, 231, 232, 172,
		           112, 113, 173, 233, 234, 235, 236, 176, 116, 56,
		           57, 58, 59]
		result = find_path(the_maze, 1740, 59)
		print_pathfile("../test6path.txt", result, the_maze.get_num_rows(), the_maze.get_num_cols())
		self.assertEqual(len(correct), len(result))
		self.assertEqual(correct, result)

	def test_find_path7(self):
		the_maze = Maze("maze3.txt")
		correct = []
		result = find_path(the_maze, 0, 959)
		self.assertEqual(len(correct), len(result))
		self.assertEqual(correct, result)

	def test_find_path8(self):
		the_maze = Maze("maze3.txt")
		correct = [423, 424, 484, 483, 543, 603, 604, 605, 606, 666,
		           667, 607, 547, 487, 488, 489, 429, 430, 370, 371,
		           372, 312, 313, 253, 254, 255, 195, 196, 197, 198,
		           199, 259, 319, 318, 317, 377, 378, 379, 439, 499,
		           498, 497, 496, 556, 616, 676, 736, 796, 795, 855,
		           915, 975, 1035, 1095, 1094, 1154, 1155, 1156, 1216, 1276,
		           1336, 1337, 1397, 1398, 1458, 1459, 1460, 1520, 1580, 1581,
		           1521, 1522, 1582, 1583, 1584, 1585, 1586, 1526, 1527, 1528,
		           1468, 1467, 1407, 1408, 1409, 1410, 1411, 1351, 1352, 1412,
		           1413, 1414, 1354, 1294, 1293, 1292, 1291, 1231, 1232, 1172,
		           1173, 1174, 1114, 1115, 1055, 1056, 996, 997, 998, 999,
		           939, 879, 878, 877, 817, 816, 815, 814, 754, 694,
		           634, 633, 632, 572, 512, 513, 514, 515, 516, 576,
		           636, 696, 756, 757, 697, 698, 638, 639, 579, 519,
		           520, 521, 522, 523, 583, 584, 585, 645, 646, 647,
		           648, 708, 768, 828, 829, 889, 949, 950, 1010, 1011,
		           951, 952, 953, 893, 894, 895, 955, 1015, 1075, 1076,
		           1077, 1078, 1018, 1019]
		result = find_path(the_maze, 423, 1019)
		print_pathfile("../test8path.txt", result, the_maze.get_num_rows(), the_maze.get_num_cols())
		self.assertEqual(len(correct), len(result))
		self.assertEqual(correct, result)

	def test_find_path9(self):
		the_maze = Maze("maze3.txt")
		correct = []
		result = find_path(the_maze, 959, 1019)
		self.assertEqual(len(correct), len(result))
		self.assertEqual(correct, result)

	def test_find_path10(self):
		the_maze = Maze("maze3.txt")
		correct = [959, 899, 898, 838, 778, 779, 839]
		result = find_path(the_maze, 959, 839)
		print_pathfile("../test10path.txt", result, the_maze.get_num_rows(), the_maze.get_num_cols())
		self.assertEqual(len(correct), len(result))
		self.assertEqual(correct, result)


if __name__ == '__main__':
	unittest.main()