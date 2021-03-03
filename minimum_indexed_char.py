import operator
T = int(input())

# counting the zero-sum subarrays is easy when
# there are no contiguous zero-sum subarrays
# because the presence of two contiguous zero-sum
# subarrays automatically make up a third zero-sum
# subarray which spans the entire two zero-sum subarrays
# this means we would need to know all the last indices

# this function originally did not take care of the contiguous subarrays case
def min_indexed_char(str1, pat):
    temp = dict()
    for i in range(len(pat)):
        temp[pat[i]] = 1    # we do not check whether the key is already present because
        # it does not matter in this problem, at the end we want all the chars to be hashed
        # irrespective of the number of times they are hashed. The only difference could be
        # if checking if the key is apready present takes less time than actual hashing operation
    for i in range(len(str1)):
        if str1[i] in temp.keys():
            return i

    return -1



for t in range(T):
    arr = input()
    pat = input()
    print('arr: {}, pat: {}'.format(arr, pat))
    val = min_indexed_char(arr, pat)
    if val == -1:
        print('No index found')
    else:
        print('vl: {}', val)

