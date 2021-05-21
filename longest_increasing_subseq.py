import numpy as np
'''  returns the longest increasing subsequence of X[0...n-1'''

def longest_increasing_subsequence(X, n):
    ''' create a table to store the lengths of
    longest increasing subsequence of a sequence.
    Note that LIS contains the length of the
    increasing numbers seuquence in X'''

    #LCSuff is the memoization table with 0 value
    # in all the cells
    LIS = [1] * n
    
    # to store the length of longest common substring
    result = 0

    # following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(n-1):
        for j in range(i+1, n):
            if X[j] > X[i]:
                # the longest subsequence now includes j
                temp = LIS[i] + 1
                if temp > LIS[j]:
                    LIS[j] = temp
            else:
                LIS[j] = 1 # there is no longest subsequence which ends as jthe number

    print(LIS)
    return np.amax(np.array(LIS))

# Driver code
X = [5, 8, 3, 7, 9, 1] 
n = len(X)

print('Length of longest common substring is', longest_increasing_subsequence(X, n))
