# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):

    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))] for ori in range(len(forward))]
    policy = [[[' ' for row in range(len(grid[0]))] for col in range(len(grid))] for ori in range(len(forward))]
    change = True

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for ori in range(len(forward)):
                    if x==goal[0] and y==goal[1]:
                        if value[ori][x][y] > 0:
                            value[ori][x][y] = 0
                            policy[ori][x][y] = '*'
                            change = True
                    
                    elif grid[x][y] == 0:
                        for a in range(len(action)):
                            o2 = (ori + action[a]) % 4
                            x2 = x + forward[o2][0]
                            y2 = y + forward[o2][1]
                            if 0<=x2 and x2 < len(grid) and 0<=y2 and y2<len(grid[0]) and grid[x2][y2]==0:
                                v2 = value[o2][x2][y2] + cost[a]
                                if value[ori][x][y]>v2:
                                    value[ori][x][y] = v2
                                    policy[ori][x][y] = action_name[a]
                                    change = True


    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    
    x = init[0]
    y = init[1]
    orient = init[2]
    step = policy[orient][x][y]
    policy2D[goal[0]][goal[1]] = '*'

    while policy[orient][x][y] != '*':
        if policy[orient][x][y] == '#':
            policy2D[x][y] = '#'
        elif policy[orient][x][y] == 'R':
            policy2D[x][y] = 'R'
            orient = (orient + action[0]) % 4
        elif policy[orient][x][y] == 'L': 
            policy2D[x][y] = 'L'
            orient = (orient + action[2]) % 4
        x += forward[orient][0]
        y += forward[orient][1]

    return policy2D

policy2D = optimum_policy2D(grid,init,goal,cost)

for i in range(len(policy2D)):
    print policy2D[i]
