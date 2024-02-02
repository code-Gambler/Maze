class Graph:
    def __init__(self, number_of_verts):
        # Initialize the Graph object with a dictionary-based adjacency list representation
        self.adj_list = {v: [] for v in range(number_of_verts)}
    
    def add_vertex(self):
        # Adds an additional vertex to the graph
        self.adj_list[len(self.adj_list)] = []
    
    def add_edge(self, from_idx, to_idx, weight=1):
        # Adds an edge from 'from_idx' to 'to_idx' with an optional 'weight'
        if from_idx not in self.adj_list or to_idx not in self.adj_list:
            return False
        
        if to_idx in [v for v, _ in self.adj_list[from_idx]]:
            return False
        
        self.adj_list[from_idx].append((to_idx, weight))
        return True
    
    def num_edges(self):
        # Returns the total number of edges in the graph
        return sum(len(edges) for edges in self.adj_list.values())
    
    def num_verts(self):
        # Returns the number of vertices in the graph
        return len(self.adj_list)
    
    def has_edge(self, from_idx, to_idx):
        # Checks if there is an edge from 'from_idx' to 'to_idx'
        if from_idx not in self.adj_list or to_idx not in self.adj_list:
            return False
        
        return to_idx in [v for v, _ in self.adj_list[from_idx]]
    
    def edge_weight(self, from_idx, to_idx):
        # Returns the weight of the edge from 'from_idx' to 'to_idx'
        if from_idx not in self.adj_list or to_idx not in self.adj_list:
            return None
        
        for v, weight in self.adj_list[from_idx]:
            if v == to_idx:
                return weight
        
        return None
    
    def get_connected(self, v):
        # Finds all the vertices connected from 'v'
        # Returns a list of tuples (connected_vertex, edge_weight)
        if v not in self.adj_list:
            return []
        
        return self.adj_list[v]
