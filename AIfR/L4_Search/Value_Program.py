# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    
    value = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    import copy
    check = copy.deepcopy(grid)
    #value = deepcopy.value

    x = goal[0]
    y = goal[1]
    v = 0
    o_list = [[v,x,y]]
    value[x][y] = 0;

    finish = False

    while not finish:

        if len(o_list)==0:
            finish = True

        else:
            o_list.sort()
            o_list.reverse()
            next = o_list.pop()
            v = next[0]
            x = next[1]
            y = next[2]
            for i in range(len(delta)):
                x2 = x - delta[i][0]
                y2 = y - delta[i][1]
                if 0<=x2 and x2<len(grid) and 0<=y2 and y2<len(grid[0]) and grid[x2][y2]!=1 and value[x2][y2]==-1:
                    v2 = v + cost
                    o_list.append([v2,x2,y2])
                    value[x2][y2] = v2

    for g in range(len(value)):
        for h in range(len(value[0])):
            if value[g][h]==-1:
                value[g][h]=99
    
    return value 

value = compute_value(grid,goal,cost)
for i in range(len(value)):
    print value[i]
