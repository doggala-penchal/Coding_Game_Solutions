"""

Goal
The 12 year old child has lost his mother and now he wants to meet his mother.
Somehow child navigated to his mother but he wanna know exact shortest distance
 and in order to help him you have to tell him exact shortest distance .
each block =10km
Input
map 10*10 first ten lines input string row only consist of '.' means road where child can move,
'#'-means wall where he can't move,'M'-position of mother,'C'-position of child.
NOTE-child can't move diagonally.
Output
one line with the shortest ditance which child have to travel in order to reach his mother
NOTE-Get ready for Episode 2.
Constraints
length of each row will be 10 and consist of only:-
'.'-Road where child can move(empty space)
'#'-wall child can't move
'M'-position of his mother
'C'-position of child
There will always be a solution
Example
Input
..........
M....C....
..........
..........
..........
..........
..........
..........
..........
..........
Output
50km

"""

"""
Answer Methodology : 
    We have to find all the values in four directions of the child
    If we don't find his mother we have to continue until we find his mother

"""

def possible_surroundings(Road_map, child_node):
    """Returns all possible surrounding positions nodes in Road_map
    Args:
        Road_map (list<list>>) : Road_map of the total situation.
        child_position (list<int, int>) : Current position of the child
    Returns:
        all_possible_surroundings (list<tuple<int, int>, ... >) : Returns all possible surroundings nodes in list
    Methodology: 
        we need to find all 4 possible surroundings so we need to find the positions in the grid.
        left : (x, y-1)
        Right : (x, y+1) 
        top : (x-1, y)
        down : (x+1, y)
    """
    l = [0,1,2,3,4,5,6,7,8,9]
    all_nodes = []
    all_possible_surroundings = []
    child_position = [child_node['current_position'][0], child_node['current_position'][1]]

    try:
        left_x = child_position[0]
        left_y = child_position[1]-1
        if left_x in l and left_y in l:
            if Road_map[left_x][left_y] == 'M' or Road_map[left_x][left_y] == '.' :
                all_possible_surroundings.append([left_x, left_y])
    except:
        pass
    try:
        right_x = child_position[0]
        right_y = child_position[1]+1
        if right_x in l and right_y in l :
            if Road_map[right_x][right_y] == '.' or Road_map[right_x][right_y] == 'M':
                all_possible_surroundings.append([right_x,right_y])
    except:
        pass
    try:
        up_x = child_position[0]-1
        up_y = child_position[1]
        if up_x in l and up_y in l:
            if Road_map[up_x][up_y] == '.' or Road_map[up_x][up_y] == 'M':
                all_possible_surroundings.append([up_x, up_y])
        
    except:
        pass
    try:
        down_x = child_position[0]+1
        down_y = child_position[1]
        if down_x in l and down_y in l:
            if Road_map[down_x][down_y] == '.' or Road_map[down_x][down_y] == 'M':
                all_possible_surroundings.append([down_x, down_y])
    except:
        pass
    for position in all_possible_surroundings:
        if position not in visited:
            all_nodes.append({'current_position' : position,'distance' : child_node['distance']+10})
    return all_nodes
    







Road_map = []
for i in range(10):
    single_road = []
    for j in input():
        single_road.append(j)
    Road_map.append(single_road)
#print(Road_map)
child_node = {
    'current_position' :  [0, 0],
    'distance' : 0,
}
for i in range(10):
    for j in range(10):
        if Road_map[i][j] == 'C':
            child_node['current_position'][0] = i
            child_node['current_position'][1] = j
            break
#print(child_node['current_position'])

fringe = [child_node]
#print(possible_surroundings(Road_map, child_node))
visited = []
while fringe:
    current_node = fringe[0]
    visited.append(current_node['current_position'])
    fringe = fringe[1:]
    possible_nodes = possible_surroundings(Road_map, current_node)
    #print(possible_nodes)
    for node in possible_nodes:
        position = node['current_position']
        x_p = position[0]
        y_p = position[1]
        if Road_map[x_p][y_p] == 'M':
            print(node['distance'],end='')
            print('km')
            fringe = []
            break
        fringe.append(node)

#print(possible_surroundings(Road_map, child_node))

        
        