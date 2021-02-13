from collections import OrderedDict
import numpy as np

T = int(input())

# the task is to swap two elemnts in the arrays such that their sums become equal
def swap_pairs_to_make_sum_equal(v1, n, v2, m):
    sum1 = np.array(v1).sum() 
    sum2 = np.array(v2).sum()
    if (sum1 + sum2) % 2 == 1:
        return -1
    
    # for every element in the larger sum array, we hash the element
    # needed from the smaller sum array to swap and make the sum equal
    temp = dict()
    if sum1 >= sum2:
        diff = sum1 - sum2
        big = v1
        small = v2
    else:
        diff = sum2 - sum1
        big = v2
        small = v1

    for i in range(len(big)):
        elem_needed = big[i] - int(diff/2) 
        if elem_needed not in temp.keys():
            temp[elem_needed] = 1
    for j in range(len(small)):
        if small[j] in temp.keys():
            return 1
    
    return -1
                


for t in range(T):
    n = int(input())
    v1 = list(map(int, input().strip().split()))
    m = int(input())
    v2 = list(map(int, input().strip().split()))
    print(' the array is :', swap_pairs_to_make_sum_equal(v1, n, v2, m))


