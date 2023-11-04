import numpy as np
import  random
from plot_maze import plot_maze
from accessible_neighbors import get_accessible_neighbors
from bfs_maze_solver import bfs_maze_solver
from functools import partial
from get_accessable_neighbors_weighted import get_accessable_neighbors_weighted
import best_candidate
"""randam_maze=np.zeros((10,10))
blocks=[(random.randint(0,9),random.randint(0,9)) for i in range(30)]
for block in blocks:
    randam_maze[block]=1"""
max_maze=np.zeros((15,15))
blocks=[(2,8),(2,9),(2,10),(2,11),(2,12),
        (8,8),(8,9),(8,10),(8,11),(8,12),
        (3,8),(4,8),(5,8),(6,8),(7,8),
        (3,12),(4,12),(6,12),(7,12)]
for block in blocks:
    max_maze[block]=1

plot_maze(max_maze)
start_cell=(14,0)
target_cell=(5,10)
horz_vec=1
diag_vec=3

solution,distance,cell_visits=bfs_maze_solver(start_cell,
                                              target_cell,
                                              max_maze,
                                             get_accessible_neighbors,
                                              verbose=False)
print('\n shortest path:',solution)
print('cell on the shortest path:',len(solution))
print('shortest path Distance:',distance)
print('Number of cell visits',cell_visits)


solution_astar,distance_astar,cell_visits_astar=best_candidate.astar_maze_solver(start_cell,
                                              target_cell,
                                              max_maze,
                                             get_accessible_neighbors,
                                             best_candidate.constant_heuristic,
                                              verbose=False)

print('\n shortest path:',solution_astar)
print('cell on the shortest path:',len(solution_astar))
print('shortest path Distance:',distance_astar)
print('Number of cell visits',cell_visits_astar)
"""partial(get_accessable_neighbors_weighted,horizontal_vertical_weight=horz_vec,diagonal_vertical_weight=diag_vec)"""
