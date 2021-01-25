import numpy as np
# function to count all possible paths
# from top left to bottom right

def numPaths(m, n):
# If either given row number is first
# or given column number is first
    if(m == 1 or n == 1):
        return 1

# If diagonal movements are allowed then
# the last addition is required
    return numPaths(m-1, n) + numPaths(m, n-1)

    

print(numPaths(3, 3))
