''' arrays are in sorted order(ascending order). We can start from the right side of the array either from th erray of size M or N, we can start traversing from that end towards the left side, we can see where is the first crossover from the right and which array gives the max value from that crossover to the right end'''

# will the results be different depending upon whether 
# geek started from array a or array b?
# can there be multiple solutions? I think yes
# e.g. let's say the last part of array a is 6, 8, 9 and the last 
# part of array b is 6, 15, then both would be optimal path and 
# hence both are valid solutions
def find_max(a, b, m, n):
    # cur sum holds the current biggest sum seen so far
    # cur sum holds the current maximum number of balls that can be picked
    # from the end so far
    cur_sum = 0
    # this variable holds the smaller of m and n
    small = m
    # these two sums contain the number of balls that can be picked 
    #up in these two arrays from the last crossover(traversal is
    # being done from right to left in the arrays)
    a_sum = 0
    b_sum = 0
    # if the sizes of the arrays are different, we will precomputer
    # ths ums of the larger array(only the part which is additional)
    if m > n:
        small = n
        # calculate the sum of the additional entries
        for i in range(n, m):
            a_sum += a[i]
    elif n > m:
        for i in range(m, n):
            b_sum += b[i]

    for i in range(small):
        # updathe the sums(from that point to the end of the arrya)
        a_sum += a[m - i - 1]
        b_sum += b[n - i - 1]
        # check if a cross over is possible
        if a[m - i - 1] == b[n - i - 1]:
            # check which sum from the end is greater so far
            # assign that sum to the current biggest sum seen so far
            if a_sum > b_sum:
                cur_sum += a_sum
            else:
                cur_sum += b_sum
            # thse sums are made to be 0 again because they can hold
            # the number of balls between two crossovers, not the entire arrays
            a_sum = 0
            b_sum = 0

    # when there was no other cross over found after the last cross over, 
    # the current sum needs to be still updates after exhausting the arrays
    # check which sum from the end is greater so far
    # assign that sum to the current biggest sum seen so far
    if a_sum > b_sum:
        cur_sum += a_sum
    else:
            cur_sum += b_sum
        
    print('cur_sum is:', cur_sum) 

a = [1, 4, 5, 6, 8]
b = [2, 3, 4, 6, 9]
m = 5
n = 5
find_max(a, b, m, n)
