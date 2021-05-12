'''  returns the longest common substring of X[0...m-1] and Y[0...n-1]'''

def LCSubStr(X, Y, m, n):
    ''' create a table to store the lengths of
    longest common suffixes of substrings.
    Note that LCSuff[i][j] contains the length
    of the longest common suffix of X[0...i-1]
    and Y[0...j-1].'''

    #LCSuff is the memoization table with 0 value
    # in all the celsss
    LCSuff = [[0 for k in range(n+1)] for l in range(m+11)]
    
    # to store the length of longest common substring
    result = 0

    # following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                LCSuff[i][j] = 0
            elif X[i-1] == Y[j-1]:
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                # result should hold the longest substring's length
                # and hence needs to be checked every time any enry
                # is updated in the memoization table
                result = max(result, LCSuff[i][j])
           #     else:
                # why do we need this explicit 0 setting?
                # we have already set everything to 0 in the
                # beginning
                #LCSuff[i][j] = 0
    
    return result

# Driver code
X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'

m = len(X)
n = len(Y)

print('Length of longest common substring is', LCSubStr(X, Y, m, n))
