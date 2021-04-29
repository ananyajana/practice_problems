''' arrays are in sorted order(ascending order). We can start from the right side of the array either from th erray of size M or N, we can start traversing from that end towards the left side, we can see where is the first crossover from the right and which array gives the max value from that crossover to the right end'''

# will the results be different depending upon whether 
# geek started from array a or array b?
# can there be multiple solutions? I think yes
# e.g. let's say the last part of array a is 6, 8, 9 and the last 
# part of array b is 6, 15, then both would be optimal path and 
# hence both are valid solutions

''' the road switching happens just before the same count bucket i.e. if 
the sequences are a = {1, 4, 5, 6, 8}, b[] = {2, 3, 4, 6, 9}, then
the road crossing can occur at 5 in first list of 4 in second list,
not 6 as I thought  earlier'''

# at the point of possible crossover do we need to consider all these
# sums: a_sum, b_sum+xleme; b_sum, a_sum+xelem; a_sum, b_sum?
''' Let's say the beginning of the array as T0, the element where the
crossoer happens as T1 and the end T2. At T1, we have four possible paths
 - continue with a[], continue with b[], go from a[] to b[] and continue
and go from b[] to a[] and continue
 max{(5+6+8), (4+6+9), (5+4+6+9), (4+5+6+8)}'''

''' but there is a problem with this approach, for example if the optimal
sum between T0 and T1 is in path b[], then if optimal path frpom T1 to T2
is go from a[] to b[] and continue, there is a conflict as it is not possible
to be on path b[] and then suddenly choose go from a[] to b[]'''

''' for every crossover we have such 4 options foe each of the already exisitng
previous options. Hence traversing may not give the solution'''

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

    flag = False
    for i in range(small):
        # updathe the sums(from that point to the end of the arrya)
        a_sum += a[m - i - 1]
        b_sum += b[n - i - 1]
        if flag is True:    # last element was a crossover element, so need to compare and take the greater sum
            # check which sum from the end is greater so far
            # assign that sum to the current biggest sum seen so far
            if a_sum > b_sum:
                cur_sum += a_sum
            else:
                cur_sum += b_sum
            flag = False # since the necessry actions for a the crossover is done,
            # we can reset the flag
        # check if a cross over is possible and set the flag
        # in next iteration, the flag needs to be checked for updating current sum
        if a[m - i - 1] == b[n - i - 1]:
            flag = True # to signify that cross over is possible
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
# https://github.com/krishnakannan/DS-Algorithms/blob/master/GeeksForGeeks/Greedy/GeekCollectBalls.java
def find_max2(a, b, m, n):
    path1 = 0
    path2 = 0

    i = 0
    j = 0

    while i < m and j < n:
        if a[i] < b[j]:
            path1 += a[i]
            i += 1
        elif a[i] < b[j]:
            path2 += b[j]
            j += 1
        else:
            path1 += a[i]
            path2 += b[j]
            if path1 > path2:
                path2 = path1
            else:
                path1 = path2
            i += 1
            j += 1

    # if te last elements are equal
    if a[i-1] == b[j-1]:
        if path1 > path2:
            path2 = path1
        else:
            path1 = path2


    while i < m:
        path1 += a[i]
        i += 1

    while j < n:
        path2 += b[j]
        j += 1

    return path1 if path1 > path2 else path2

a = [1, 4, 5, 6, 8]
b = [2, 3, 4, 6, 9]
m = 5
n = 5
#find_max(a, b, m, n)
print('max path: ', find_max2(a, b, m, n))
