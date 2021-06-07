''' given an array of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same'''

''' in that case the sum of each subset should be exactly half of the sum
of all elements in the array, another constraint is that the array needs to
have an even sum?
one key observation is that we do not need to find both the subsets, we just
need to find one subset which sums upto sum(arr) / 2
Where is the optimal substructure'''
# another observation is that if there is any element bigger
# than the req_sum then such subset is not possible

import numpy as np
# we don't need a separate equal subset sum routine for this
# we can just reuse the subset sum problem
def equal_subset_sum(arr, n):
    sum_val =  np.sum(np.array(arr)) 
    if sum_val% 2 != 0:
        return False
    
    req_sum = sum_val // 2 # if we are here sum_val is even

    # we will need to make a memoization table which will try to 
    # see if there is a sum possible from 1 to sum/2 and fill it
    # in the same way as to find subsequence sum

    # how to decide whether we need a 1d or 2d table?
    # we need to enumerate all possible subset sums till we reach the req_sum
    # or alternately we are trying to find the req_sum sum in the array
    # maybe we can try to take each current element and find the req_sum - element in
    # the remaining array, so that is the recursion. But how to find the
    # table entries? should be element Vs partial sum, but in that case we will
    # need to enumerate all possible sums which might not be necessary
    #table = [[arr[i] for i in range(len(arr))] for j in range(req_sum)]
    #table = [arr[i] for i in range(len(arr)) and j in range(req_sum) if arr[i] == j else 0] 
    # problem with this table is that it does not specify how many times does the
    # particular sum occur.
    table = [0 for j in range(req_sum + 1)]
    for i in range(n):
        for j in range(req_sum):
            if arr[i] == j:
                table[j] = 1


    # we need to update the sum table afer accessing each array element
    for i in range(n):
        for j in range(req_sum + 1):
            # the element is itself equal to the subset sum
            # hence the subset partition is possible as other
            # elements must also sum up equal to the req_sum
            if arr[i] == req_sum:
                return True
            elif arr[i] > req_sum:
                return False
            # if the j-arr[i] sum exists in the table, then only fill
            # the current sum as exists, else not
            if table[j - arr[i]] == 0:
                table[j] = 0
            else:
                table[j] = 1
        
    # we need to update the table with this element
    print('table is:', table)
            
    return (table[req_sum] == 1)

# returns true if there is a subset from the array[0, ...j-1] with sum equal to i

def subset_sum(arr, n, sum_val):
    # the value of the subset[i][j] will be true if there is a subset of set[0,...j-1] with sum equal to i
    subset = [[False for i in range(sum_val + 1)] for i in range(n + 1)]

    # if sum is 0, then value is always true, as we do not need to 
    # include any element in the subset and hat is the only solution
    for i in range(n + 1):
        subset[i][0] = True    

    # if sum is not 0 and set is empty then return False
    for i in range(1, sum_val + 1):
        subset[0][i] = False

    # fill the subset table in bottom up manner
    # subset[i][j] corresponds to the arr[i-1] element and sum j
    # be mindful of the array indexing
    for i in range(1, n+1):
        for j in range(1, sum_val + 1):
            if j < arr[i - 1] :
                # in this case if the subset sum was already found
                # it still remains a valid subset after including the
                # the current element and as the current element
                # cannot be part of the subset then the previous valid
                # subset still holds valid for the set[0, ...i]
                subset[i][j] = subset[i-1][j]       
            else:
                # the element is valid and hence can be a part of the subset
                # so check both possibilities ie (1)the subset is already found
                # and (2)the j - arr[i] is present in the arr[o, ....i]
                # then we cna include the current element and complete the subset
                subset[i][j] = (subset[i-1][j] or subset[i-1][j - arr[i-1]])

    return subset[n][sum_val]

arr = [1, 5, 9, 2, 5]
#arr = [1, 5, 11, 5]
#arr = [1, 5, 1]
#arr = [1, 4, 1]
#arr = [1, 3, 2]
N = len(arr)
#print('equal subset partition possible? ', equal_subset_sum(arr, N))
sum_val =  np.sum(np.array(arr)) 
if sum_val% 2 != 0:
    print('equal subset partition possible? ', False)
else:
    req_sum = sum_val // 2 # if we are here sum_val is even
    print('equal subset partition possible? ', subset_sum(arr, N, req_sum))
