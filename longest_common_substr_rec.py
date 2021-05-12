''' Returns the longest common substring of X[0..m-1],Y[0..n-1]'''

def lcs(i, j, count):
    if i== 0 or j == 0:
        return count
    
    if (X[i - 1] == Y[j - 1]):
        count = lcs(i-1, j-1, count+1)

    # confused about why these two cases needs to be covered?
    # is it to check whether the introcucing the x[i] or y[j]
    # character does not decrease the length of the common
    # substring associated with x[i-1], y[j-1] so far
    count = max(count, max(lcs(i, j-1, 0),lcs(i-1, j, 0)))

    return count    

X = "abcdxyz"
Y = "xyzabcd"

n = len(X)
m = len(Y)

print(lcs(n, m, 0))
