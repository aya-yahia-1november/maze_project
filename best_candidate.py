import  sys
import numpy as np
from get_accessable_neighbors_weighted import get_accessable_neighbors_weighted
from construct_shortest_path import construct_shortest_path
def constant_heuristic(candidate_cell:tuple,target_cell:tuple):
    return 1
def manhatten_heuristic(candidate_cell:tuple,target_cell:tuple):
    x1,y1=candidate_cell
    x2,y2=target_cell
    return abs(x1-x2)+abs(y1-y2)

def get_best_candidate(expansion_candidates:set,
                       shortest_distance:dict,
                       heuristic:callable):
    winner=None
    target_cell=None
    best_estimate=sys.maxsize
    for candidate in expansion_candidates:
        candidate_estimate=shortest_distance[candidate]+heuristic(candidate,target_cell)
        if candidate_estimate<best_estimate:
            winner=candidate
            best_estimate=candidate_estimate
    return winner
def astar_maze_solver(start_cell:tuple,
                      target_cell:tuple,
                      maze:np.ndarray,
                      get_neighbors:callable,
                      heuristic:callable,
                      verbose:bool=False):
    cell_visits = 0
    shortest_distance={}
    shortest_distance[start_cell]=0
    parent={}
    parent[start_cell]=start_cell
    expansion_candidate=set([start_cell])
    fully_expanded=set()


    while len(expansion_candidate) > 0:
        best_cell=get_best_candidate(expansion_candidate,shortest_distance,heuristic)
        if best_cell==None :break
        if verbose:

            print('\n Expanding cell',best_cell)
        if best_cell==target_cell:
            shortest_path=construct_shortest_path(parent,start_cell,target_cell)
            return shortest_path,shortest_distance[target_cell],cell_visits
        for neighbor,cost in get_neighbors(maze,best_cell):
            if verbose:
                print('\t Visited neighbors cell ',neighbor)
            cell_visits+=1
            if (neighbor not  in expansion_candidate) and (neighbor not  in fully_expanded):
                expansion_candidate.add(neighbor)
                parent[neighbor]=best_cell
                shortest_distance[neighbor]=shortest_distance[best_cell]+cost

            elif shortest_distance[neighbor]>shortest_distance[best_cell]+cost:
                shortest_distance[neighbor] = shortest_distance[best_cell] + cost
                parent[neighbor] = best_cell
                if neighbor in fully_expanded:
                    fully_expanded.remove(neighbor)
                    expansion_candidate.add(neighbor)

        expansion_candidate.remove(best_cell)
        fully_expanded.add(best_cell)
    return None,None,None