''' fin the minimum number of operations to convert one string into another.
Allowed operations are 1.insert, 2.remove and 3.replace. '''

# one observation os that in the worst case if all the chars are different we
# man(m, n) operations where m and n are the elngths of the strings respectively
# basically we want to find the longest common subsequence between the two strings
# and coner the rest, we need the longest common subsequence and their locations
# as well?
def edit_dist(a, b):
    n = len(a)
    m = len(b)

    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            # filling the dp table in a bottom up manner
            # if the length of t=one of the strings is 0
            # then the dp should hold the length of the
            # other string
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i

            # if the current chars match, then the value is 
            # same as the value for the previous two chars
            # from the two strings
            elif a[i-1] == b[j-1]:  # this is because the i-1 and j-1 char
                # are corrsponding to the dp[i][j] entry, the iteration
                # of i, j are done from 0 to m+1, n+1 but string lengths are m, n
                dp[i][j] = dp[i-1][j-1]

            #else we need to find the minimum of all possible
            # scenarions - insert, delete and replace as the current 
            # chars do not match
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])     # dp[i][j-1] # insert in the a string
                                        # dp[i-1][j] # delete in the a string
                                        # dp[i-1][j-1]) # replace the last char in a string to be the last char in b string


    
    return dp[n][m]


#a = 'geek'
#b = 'gesek'
a = 'sunday'
b = 'saturday'
print(edit_dist(a, b))
