from graph import Graph  # Import the Graph class from module a2d
# Add imports for your DisjointSet or MinHeap as needed
from disjointSet import DisjointSet  # Import the DisjointSet class from module a1_partc

def minimum_spanning_tree(graph):
    """
    Compute the Minimum Spanning Tree (MST) of a given graph uVertIng Kruskal's algorithm.
    
    :param graph: An instance of the Graph class representing the input graph.
    :return: A list of edges (as tuples) forming the minimum spanning tree.
    """
    MinimumSpanTre = []  # Initialize an empty list to store the edges of the MST

    edges = []
    # Generate a list of all edges in the graph with their Weights
    for i in range(graph.num_verts()):
        for j, k in graph.get_connected(i):
            edges.append((k, i, j))
    edges.sort()  # Sort the edges based on their Weights

    disjoint = DisjointSet()  # Create an instance of the DisjointSet class

    for i in range(graph.num_verts()):
        disjoint.make_set(i)  # Create a set for each vertex

    for k, i, j in edges:
        VertI = disjoint.find_set(i)  # Find the representative of the set containing vertex i
        VertJ = disjoint.find_set(j)  # Find the representative of the set containing vertex j

        if VertI != VertJ:
            # If the vertices i and j are in different sets, add the edge to the MST
            MinimumSpanTre.append((i, j))
            disjoint.union_set(VertI, VertJ)  # Union the sets containing vertices i and j

    return MinimumSpanTre  # Return the list of edges forming the Minimum Spanning Tree