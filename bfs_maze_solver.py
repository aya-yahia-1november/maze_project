from construct_shortest_path import construct_shortest_path
import numpy as np
def bfs_maze_solver(start_cell:tuple,taget_cell:tuple,maze:np.ndarray,get_neighbors:callable,verbose:bool=False):
    cell_visits=0
    visited=set()
    to_expand=[]
    visited.add(start_cell)
    to_expand.append(start_cell)
     #shortest distance form the start cell to each other cell
    shortest_distance={}
    shortest_distance[start_cell]=0
    parent={}
    parent[start_cell]=start_cell
    while len(to_expand)>0:
        next_cell=to_expand.pop(0)
        if verbose:
            print('\n Expanding cell ',next_cell)
        for neighbor,cost in get_neighbors(maze,next_cell):
            if verbose:
                print('\t Visited neighbors cell ',neighbor)
            cell_visits+=1
            if neighbor not in visited:
                visited.add(neighbor)
                to_expand.append(neighbor)
                parent[neighbor]=next_cell
                shortest_distance[neighbor]=shortest_distance[next_cell]+cost
                if neighbor == taget_cell:
                    shortest_path = construct_shortest_path(parent, start_cell, taget_cell)
                    return shortest_path, shortest_distance[taget_cell], cell_visits

            else:
                  if shortest_distance[neighbor]>shortest_distance[next_cell]+cost:
                      parent[neighbor]=next_cell
                      shortest_distance[neighbor]=shortest_distance[next_cell]+cost
    return None,None,None