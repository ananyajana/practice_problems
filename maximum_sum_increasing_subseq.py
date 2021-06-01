import numpy as np
'''  returns the maximum sum increasing subsequence of X[0...n-1]
This is slightly different from longest increasing subsequence.
Here the criteria is sum instead of length'''

def max_sum_increasing_subsequence(X, n):
    ''' create a table to store the lengths of
    longest increasing subsequence of a sequence.
    Note that LIS contains the length of the
    increasing numbers seuquence in X'''

    # initialize the memoization table all entries with the
    # corresponding array entry because when the subsequence
    # length is just one, that means the element itself and
    # that is the default maximum increasing subsequence sum
    # for that entry
    msis = [0 for x in range(n)]
    for i in range(n):
        msis[i] = X[i]
    
    # to store the sum of mum increasing subsequence
    result = 0

    # following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(1, n):
        for j in range(i):
            if X[i] > X[j] and msis[i] < msis[j] + X[i]:
                msis[i] = msis[j] + X[i]
    #

    print(msis)
    return np.amax(np.array(msis))

# Driver code
X = [1, 101, 2, 3, 100, 4, 5]
n = len(X)

print('sum of maximum sum increasin subsequence is', max_sum_increasing_subsequence(X, n))
