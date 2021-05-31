''' We want to construct a table k(nxW) where n is the number of items and
W is the maximum capacity. At every step we want to find what is the maximum
possible value for a specific capacity. K[i][j] denotes the maximum possible
value for capacity j. We fill in the 0th column and row of the table with all
0s, that is a dummy column and row to handle the -1 case,
as we can see the numberings are from 1 to W and 1 to n'''


def knapsack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:  # there is a possibility of adding wt[i-1]
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
                # there are two possible cases, take the current weight
                # and add the last possible maximum weight till the last
                # element, or take the last element's vale from the same
                # same column
            else:
                K[i][w] = K[i-1][w] # here we need to fill in the last
                # elelemnt's value in the same column because current
                # weight can't fit in the capacity

    return K[n][w]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapsack(W, wt, val, n))
