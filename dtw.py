''' implementtion of the dtw algorithm
https://towardsdatascience.com/dynamic-time-warping-3933f25fcdd
in this algorithm the first elements are always matched.
But is it necessary that the first elements have to be matched?
Even the last elements are also matched, but this also may not hold
true if one of the signals is little different from the other
'''

import numpy as np

def dtw(s, t):
    n = len(s)
    m = len(t)

    # initialize the DTW table with very large value or infinity
    #dtw_matrix = np.zeros((n+1, m+1)) * np.Inf # this does not work,
    # all the numbers become nan instead of infinity

    dtw_matrix = np.zeros((n+1, m+1))
    for i in range(n+1):
        for j in range(m+1):
            dtw_matrix[i, j] = np.inf
    # initialize the dtw matrix with very  large values
    dtw_matrix[0, 0] = 0

    print('dtw_matrix: ', dtw_matrix)

    for i in range(1, n+1):
        for j in range(1, m+1):
            # the absolute distance between the two points is the cost
            cost = abs(s[i-1] - t[j-1])
            # take the last minimum entry from the last three surroundin
            # cells in the dtw matrix
            #last_min = np.min([dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1]])
            last_min = min(dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1])
            print('last_min :', last_min)
            dtw_matrix[i, j] = cost + last_min
    
    return dtw_matrix

a = [1, 2, 3]
b = [2, 2, 2, 3, 4]
print(dtw(a, b))
#print(dtw2(a, b))

# the distance between a ad b is the last element in the matrix i.e. dtw_matrix[n, m]

