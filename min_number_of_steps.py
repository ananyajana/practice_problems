import numpy as np
'''  returns the maximum sum increasing subsequence of X[0...n-1]
This is slightly different from longest increasing subsequence.
Here the criteria is sum instead of length'''

def min_number_of_jumps(X, n):
    ''' create a table to store the lengths of
    longest increasing subsequence of a sequence.
    Note that LIS contains the length of the
    increasing numbers seuquence in X'''

    # initialize the memoization table all entries with the
    # corresponding array entry because when the subsequence
    # length is just one, that means the element itself and
    # that is the default maximum increasing subsequence sum
    # for that entry
    # the length of the array is the maximum possible number of jumps
    # mj[i] gives the minimum possible number of jumps to reach the ith
    # element, at most it can be i and hence that's the value we initialize it with
    mj = [i for i in range(n)]
    
    # to store the sum of mum increasing subsequence
    result = 0

    # following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(0, n-1):
        for j in range(i+1, n):
            if X[j] - X[i] <= X[i] and mj[i] + 1 < mj[j]:
                mj[j] = mj[i] + 1
    #

    print(mj)
    return mj[-1]

# Driver code
#X = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
X = [1, 4, 3, 2, 6, 7]
n = len(X)

print('min number of jumps', min_number_of_jumps(X, n))
