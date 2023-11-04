def construct_shortest_path(parent:dict,start_cell:tuple,target_cell:tuple):
    shortest_path=[]
    my_parent=target_cell
    while my_parent!=start_cell:
        shortest_path.append(my_parent)
        my_parent=parent[my_parent]
    shortest_path.append(start_cell)
    shortest_path.reverse()
    return shortest_path
