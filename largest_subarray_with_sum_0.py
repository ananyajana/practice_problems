T = int(input())

def maxLen(n, arr):
    # create a new dictionary where where key is the sum and 
    hash_map = dict()
    # create an array of the same length as arr.
    # this is to hold the prefix sums
    sum1 = 0
    max_len = 0

    for i in range(n):
        sum1 = sum1 + arr[i]
        if arr[i] == 0 and max_len == 0:
            max_len = 1
        # if the current sum is 0 then the maximum length is i+1
        # because this is the longest path we have seen so far
        if sum1 == 0:
            max_len = i + 1
        # if the current sum is already in  the hash table that means
        # the subarray between the hash_map[sum] and i is 0
        if sum1 in hash_map.keys():
            max_len = max(max_len, i - hash_map[sum1])
        else:
            hash_map[sum1] = i

    return max_len


    

for t in range(T):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print('arr {}, n {} '.format(arr, n))
    print('max_len is :', maxLen(n, arr))


