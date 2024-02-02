from maze import Maze

def find_path(the_maze, from_cell, to_cell):
    visited = set()  # Set to keep track of visited cells
    path = []  # List to store the path from the starting cell to the target cell
    
    # Recursive helper function
    def find_path_recursive(current_cell):
        visited.add(current_cell)  # Mark the current cell as visited
        path.append(current_cell)  # Add the current cell to the path
        
        if current_cell == to_cell:
            return True  # Found the target cell, return True to stop recursion
        
        # Iterate through the neighboring cells
        left_cell = the_maze.get_left(current_cell)
        if left_cell != -1 and left_cell not in visited:
            if find_path_recursive(left_cell):
                return True  # Path found, return True to stop recursion
        
        right_cell = the_maze.get_right(current_cell)
        if right_cell != -1 and right_cell not in visited:
            if find_path_recursive(right_cell):
                return True  # Path found, return True to stop recursion
        
        up_cell = the_maze.get_up(current_cell)
        if up_cell != -1 and up_cell not in visited:
            if find_path_recursive(up_cell):
                return True  # Path found, return True to stop recursion
        
        down_cell = the_maze.get_down(current_cell)
        if down_cell != -1 and down_cell not in visited:
            if find_path_recursive(down_cell):
                return True  # Path found, return True to stop recursion
        
        # If no path found from the current cell, backtrack
        path.pop()
        
        return []  # No path found from the current cell
    
    # Call the recursive function to find the path
    if find_path_recursive(from_cell):
        return path
    
    return []  # No path found from the starting cell to the target cell
