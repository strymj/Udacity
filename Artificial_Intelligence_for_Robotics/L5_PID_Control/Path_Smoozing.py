# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and 
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in nextpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite 
# correct).
# -----------

from copy import deepcopy
import math

# thank you to EnTerr for posting this on our discussion forum
def printpaths(path,nextpath):
    for old,new in zip(path,nextpath):
        print '['+ ', '.join('%.3f'%x for x in old) + \
               '] -> ['+ ', '.join('%.3f'%x for x in new) +']'

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    # Make a deep copy of path into nextpath
    nextpath = deepcopy(path)
    newpath = deepcopy(path)
    change = True

    while change:
        change = False
        for i in range(1,len(path)-1):
            for j in range(len(path[0])):
                nextpath[i][j] = newpath[i][j]
                nextpath[i][j] += weight_data * (path[i][j] - newpath[i][j])
                nextpath[i][j] += weight_smooth * (newpath[i-1][j] + newpath[i+1][j] - 2 * newpath[i][j])
                if math.fabs(nextpath[i][j] - newpath[i][j]) > tolerance:
                    newpath[i][j] = nextpath[i][j]
                    change = True
    
    return newpath # Leave this line for the grader!

printpaths(path,smooth(path))
