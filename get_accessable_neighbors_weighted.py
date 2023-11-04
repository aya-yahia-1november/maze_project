import numpy as np
def get_accessable_neighbors_weighted(maze:np.ndarray,
                                      cell:tuple,
                                      horizontal_vertical_weight:float,
                                      diagonal_vertical_weight:float):
    neighbors=[]
    x,y=cell
    for i,j in [(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]:
        if i>=0 and j>=0 and i<len(maze) and j<len(maze[0]) and maze[(i,j)]==0:
            neighbors.append(((i,j),diagonal_vertical_weight))
    for i,j in [(x-1,y),(x,y-1),(x,y+1),(x+1,y)] :
        if i >= 0 and j >= 0 and i < len(maze) and j < len(maze[0]) and maze[(i, j)] == 0:
            neighbors.append(((i, j), horizontal_vertical_weight))
    return neighbors