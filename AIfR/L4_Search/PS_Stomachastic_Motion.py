# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# returns two grids. The first grid, value, should 
# contain the computed value of each cell as shown 
# in the video. The second grid, policy, should 
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid,goal,cost_step,collision_cost,success_prob):
    failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[collision_cost for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    change = True

    value[goal[0]][goal[1]] = 0
    policy[goal[0]][goal[1]] = '*'

    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    for d in range(len(delta)):
                        x2 = x - delta[d][0]
                        y2 = y - delta[d][1]
                        if 0<=x2 and x2<len(grid) and 0<=y2 and y2<len(grid[0]) and grid[x2][y2]==0:
                            v2 = 1
                            for i in range(-1,2):
                                dire = (d+i) % len(delta)
                                x3 = x2 + delta[dire][0]
                                y3 = y2 + delta[dire][1]
                                vx = collision_cost
                                prob = failure_prob
                                if 0<=x3 and x3<len(grid) and 0<=y3 and y3<len(grid[0]) and grid[x3][y3]==0:
                                    vx = value[x3][y3]
                                if i == 0:
                                    prob = success_prob
                                v2 += vx * prob
                            if v2<value[x2][y2]:
                                value[x2][y2] = v2
                                policy[x2][y2] = delta_name[d]
                                change = True
    
    return value, policy

# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0,0,0,1,0,0,0],
        [0,1,0,0,0,1,0],
        [0,1,1,0,1,1,0],
        [0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0]]

#grid = [[0,0,0,0],
#        [0,0,0,0],
#        [0,0,0,0],
#        [0,1,1,0]]

goal = [0, len(grid[0])-1] # Goal is in top right corner
cost_step = 1
collision_cost = 100
success_prob = 0.8
#success_prob = 0.5
value,policy = stochastic_value(grid,goal,cost_step,collision_cost,success_prob)
#for row in value:
#    print row
#for row in policy:
#    print row

# Expected outputs:
#
# [57.9029, 40.2784, 26.0665,  0.0000]
# [47.0547, 36.5722, 29.9937, 27.2698]
# [53.1715, 42.0228, 37.7755, 45.0916]
# [77.5858, 100.00, 100.00, 73.5458]
#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']
