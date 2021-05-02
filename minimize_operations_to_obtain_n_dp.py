''' from geeksforgeeks.
If the minimum number of operations needed to obtain any number smaller
than N is known, them minimum operations to obtain N can be calculated.
A lookup table needs to be created where
dp[i] = min. no. of operations needed to obtain i from 1.
so, for any number x, the minimum no. of operations required to obtain x
can be calculated as:
dp[x] = min(dp[x-1], dp[x/2]) + 1
The only possible operations are multiplication by 1
addition of 1'''

MAX = 999999999
# function to find the minimum number of operations
def min_operations(n):
    # storing the minimum operations
    # to obtain all numbers upto N
    dp = [MAX]*(n + 1)

    # initial state
    dp[0] = 0

    # iterate for the remaining numbers
    for i in range(1, n+1):
        # if the number can be obtained
        # by multiplication by 2
        if i % 2 == 0:
            x = dp[i // 2]
            if x + 1 < dp[i]:
                dp[i] = x + 1

        # obtaining the number by adding 1
        x = dp[i - 1]
        # if the current value of dp[x] is greater than
        # the number of operations needed to create i-1 + 1
        # then update dpi]
        if x + 1 < dp[i]:
            dp[i] = x + 1


    return dp[n]

n = 15
print(min_operations(n))
