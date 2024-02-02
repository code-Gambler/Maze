import unittest

from maze import Maze, print_mazefile, print_pathfile
from mazeRunner import find_path
from generateMaze import generate_maze


class GenerateMaze_TestCase(unittest.TestCase):
    # These are the tests cases for functions of MinHeap class

    def test_generate_maze(self):
        maze = generate_maze(3,4)
        self.assertEqual(len(maze),6)


    def test_generate_maze2(self):

        maze = generate_maze(10,10)
        self.assertEqual(len(maze),81)

        print_mazefile("a3_maze1.txt", maze, 10, 10, 11, 88)

        the_maze=Maze("a3_maze1.txt")
        result = find_path(the_maze, 11, 88)
        print_pathfile("a3_run1.txt", result, the_maze.get_num_rows(), the_maze.get_num_cols())

    def test_generate_maze3(self):
        maze = generate_maze(80,100)
        self.assertEqual(len(maze),7821)
        print_mazefile("a3_maze2.txt", maze, 80, 100, 99, 7900)

        the_maze=Maze("a3_maze2.txt")
        result = find_path(the_maze, 99, 7900)
        print_pathfile("a3_run2.txt", result, the_maze.get_num_rows(), the_maze.get_num_cols())


        



if __name__ == '__main__':
    unittest.main()
