import random
from graph import Graph
from mst import minimum_spanning_tree

def generate_maze(number_of_rows, number_of_columns):
    """
    Generate a maze with the specified dimensions using a graph-based approach.

    The function creates a maze by:
    1. Constructing a graph where each cell in the maze corresponds to a node in the graph.
    2. Creating a list of all possible walls between adjacent cells.
    3. Assigning random weights to these walls (edges in the graph).
    4. Using Kruskal's algorithm to compute a minimum spanning tree (MST) of this graph.
    5. The walls of the maze are determined by removing the edges of the MST from the list of all walls.

    Parameters:
    - number_of_rows (int): The number of rows in the maze.
    - number_of_columns (int): The number of columns in the maze.

    Returns:
    - list of tuple: A list of walls, where each wall is represented as a tuple of two integers,
                     denoting the cells that this wall separates.
    """

    # Calculate the total number of cells in the maze
    tuple_cells = number_of_rows * number_of_columns

    # Create a list of walls using list comprehensions
    # First, create the vertical walls (separating cells horizontally)
    vertical_walls = [
        (row * number_of_columns + col, row * number_of_columns + col + 1)
        for row in range(number_of_rows) for col in range(number_of_columns - 1)
    ]
    # Then, create the horizontal walls (separating cells vertically)
    horizontal_walls = [
        (row * number_of_columns + col, (row + 1) * number_of_columns + col)
        for row in range(number_of_rows - 1) for col in range(number_of_columns)
    ]
    walls = vertical_walls + horizontal_walls

    # Initialize the maze graph
    maze_graph = Graph(tuple_cells)

    # Populate the maze graph with edges representing walls
    for start_index, end_index in walls:
        random_weight = random.randint(1, 50)  # Assign a random weight to the wall
        maze_graph.add_edge(start_index, end_index, random_weight)

    # Compute a minimum spanning tree for the graph
    edges_of_mst = minimum_spanning_tree(maze_graph)

    # Determine the final walls by removing the MST edges from the list of all walls
    final_walls = [wall for wall in walls if wall not in edges_of_mst]

    return final_walls

