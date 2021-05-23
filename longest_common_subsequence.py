import numpy as np
'''  returns the longest common subsequence of X[0...n-1] and Y[0...m-1]'''

def longest_common_subsequence(X, Y, n, m):
    ''' create a table to store the lengths of
    longest common subsequence of two sequences.
    Note that LCS contains the length of the
    subsequence common to both X and Y'''

    #LCSuff is the memoization table with 0 value
    # in all the cells
    # the entry at the i,j the cell contains the length
    # of the longest common subsequence ending at X[i] and Y[j]
    # is the condition ending at a necessary condition?
    LCS = np.array([[0 for i in range(n+1)] for j in range(m+1)])
    
    # to store the length of longest common subsequence
    result = 0

    # following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(n+1):
        for j in range(m+1):
            print(LCS)
            if i == 0 or j == 0:
                LCS[i][j] = 0
            elif X[i-1] == Y[j-1]:
                LCS[i][j] = LCS[i-1][j-1] + 1
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
                    
                        

    print(LCS)
    return np.amax(np.array(LCS))

# Driver code
X = "ABCDGH"
Y = "AEDFHR"
n = len(X)
m = len(Y)

print('Length of longest common substring is', longest_common_subsequence(X, Y, n, m))
