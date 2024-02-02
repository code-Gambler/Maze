# Maze Runs

screenshots of maze runs:

- Run-1:

![image](https://github.com/seneca-dsa456/a3-g3-a3-lkamal1-mprapti-spillay6/assets/98861688/7267f381-f1ed-4969-b8ca-7afbafe3509c)

- Run-2:

![image](https://github.com/seneca-dsa456/a3-g3-a3-lkamal1-mprapti-spillay6/assets/98861688/8a69ff2a-e710-460c-927e-d3d2c7449737)

Graph Algorithms Implementation
-------------------------------

This project focuses on the implementation of various graph algorithms, specifically the MinHeap data structure, Minimum Spanning Tree (MST) using Kruskal's algorithm, and Maze Generation.

### MinHeap Implementation

#### Class: MinHeap

A MinHeap is implemented as a Python class with the following member functions:

1.  **Initializer: __init__(self, arr = [])**

-   When instantiated, the MinHeap is passed a Python list, which may be empty. It initializes the heap using this array.

1.  **Function: insert(self, element)**

-   Adds an element to the MinHeap.

1.  **Function: get_min(self)**

-   Returns the smallest value in the MinHeap without altering the data structure.

1.  **Function: extract_min(self)**

-   Removes the smallest value from the MinHeap and returns that value.

1.  **Function: is_empty(self)**

-   Returns True if the MinHeap is empty, False otherwise.

1.  **Function: __len__(self)**

-   Returns the number of values stored in the heap.

### Minimum Spanning Tree (MST) Implementation

#### Function: minimum_spanning_tree(graph)

Implemented a function that finds the minimum spanning tree of a graph using Kruskal's algorithm, which involves disjoint sets.

### Maze Generation

#### Function: generate_maze(number_of_rows, number_of_columns)

Implemented a maze generation function that takes the size of the maze in terms of the number of rows and columns. It returns a Python list of tuples representing the walls for this maze.

### Maze Generation Process

1.  **Wall Representation:**

-   Each wall is represented as a tuple of two numbers (cell_1, cell_2).

1.  **Graph Creation:**

-   Create a graph where each cell in the maze is a vertex.
-   For each wall in the list of walls, create edges between cells with random weights.

1.  **Minimum Spanning Tree:**

-   Find the minimum spanning tree of the graph using Kruskal's algorithm.
-   Create a list of walls to remove based on the MST.

1.  **Maze Formation:**

-   Remove each wall in the MST from the original wall list, creating the final list of walls that form the maze.

### Unit Tests and GitHub Workflows

Unit tests have been developed to ensure the correctness of the implemented algorithms. GitHub workflows have been set up for continuous integration.

Usage
-----

To use the MinHeap, MST, and Maze Generation functionalities, refer to the respective sections above. Ensure that the required classes and functions are imported into your project.

## My Reflections

1. What did I do for the Project.

I implemented a maze generation algorithm utilizing graph theory. Here's a breakdown of the steps I took:

**Initialization**: I began by calculating the total number of cells based on the number of rows and columns for the maze. These cells were used as vertices for our graph representation of the maze.

**Wall Representation**: Using a grid-based approach, I represented each wall as a tuple of two cells. For instance, in a 3x4 maze, the wall separating cell 0 and cell 1 would be represented as the tuple (0,1). I systematically generated these tuples for both vertical and horizontal walls and combined them into a single list.

**Graph Creation**: Using the aforementioned list of walls, I initiated the creation of our maze graph. Every cell (or vertex) in the maze has potential connections (or edges) to its neighboring cells. These connections were assigned random weights between 1 and 50, to introduce randomness into the maze generation process. This randomness is pivotal as it ensures that each time a maze is generated, the outcome is potentially different. For every wall, I added two edges (due to the undirected nature of the graph): one from cell A to cell B, and another from cell B to cell A, both with the same random weight.

**Minimum Spanning Tree (MST)**: The objective of creating a maze is to ensure there's a path from any cell to any other cell, without cycles. To achieve this, I used the minimum spanning tree function which leveraged Kruskal's algorithm to find a Minimum Spanning Tree (MST) for our graph. By definition, an MST connects all vertices in a graph, ensuring no cycles and utilizing the minimum possible total edge weight.

**Maze Finalization**: With the MST edges identified, I used them to determine the walls of our final maze. Specifically, the walls in our final maze were the ones not present in the MST. Hence, I removed MST edges from our original wall list to determine the walls for the maze.

2. What was one thing that I learned when doing this Project?

One profound lesson from this assignment was the application of graph theory in practical scenarios, such as maze generation. I learned how core graph algorithms, like Kruskal's algorithm for MST determination, can be adapted and utilized in different contexts. Additionally, the assignment underscored the significance of randomness in procedural generation. By merely assigning random weights to edges, we were able to generate diverse maze configurations.

3. What was the most challenging aspect and what did I do to overcome this challenge?

The most challenging aspect of this Project was ensuring that the generated maze was both random and solvable. It was crucial to strike a balance between introducing randomness (through edge weights) and adhering to the principles of graph theory to guarantee a solvable maze. Initially, I grappled with understanding how the MST ensured a solvable maze without cycles. To overcome this, I delved deeper into the properties and principles of MSTs, reinforcing my comprehension through visual aids and supplemental reading. This deeper understanding allowed me to confidently use the MST to craft the final maze.








