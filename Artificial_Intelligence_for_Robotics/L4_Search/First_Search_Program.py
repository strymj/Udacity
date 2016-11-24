# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    o_list = [[0,init[0],init[1]]]
    check = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    check[init[0]][init[1]] = 1

    while len(o_list) != 0:
        o_list.sort()
        o_list.reverse()
        nex = o_list.pop()

        for i in range(len(delta)):
            x2 = nex[1] + delta[i][0]
            y2 = nex[2] + delta[i][1]
            if 0<=x2 and x2 <len(grid) and 0<=y2 and y2<len(grid[0]) and grid[x2][y2]==0 and check[x2][y2]==0:
                o_list.append([nex[0]+cost,x2,y2])
                check[x2][y2] = 1
                if x2==goal[0] and y2==goal[1]:
                    return o_list.pop()

    return "fail"

print search(grid,init,goal,cost)
