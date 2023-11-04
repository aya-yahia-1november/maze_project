import numpy as np
def get_accessible_neighbors(maze:np.ndarray,cell:tuple):
    neighbors=[]
    x,y=cell
    for i,j in[(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:
        if i>=0 and j>=0 and i<len(maze) and j<len(maze[0]) and maze[(i,j)]==0:
            neighbors.append(((i,j),1))
    return neighbors