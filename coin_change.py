''' we need to count the total number of ways it is possible to create a change
for N from the set(of length m) of coins where a coin can be used infinite times'''
# we need to find all subsequences that sum upto N. Also we need to see how many
# ways a coin S can be made from the set given to us


# recursive way, solutions that include the coin s_m and solutions that do not include
# s_m 

def count(S, m, n):
    # if n==0 then there is only one way i.e. no coin
    if n == 0:
        return 1

    # if n is less than 0 ten no solution exits
    if n < 0:
        return 0

    # if there is no coins and n is > 0 then no solution exist  
    if m <= 0 and n >= 1:
        return 0

    # count the sum of the solutions which include s[m-1] and 
    # xclusing s[m-1]
    return count(S, m - 1, n) + count(S, m, n - S[m-1])

# Driver program to test above function
arr = [1, 2, 3]
n = 4

#arr = [2, 5, 3, 6]
#n = 10

m = len(arr)
print(count(arr, m, n))
