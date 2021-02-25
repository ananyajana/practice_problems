import operator
T = int(input())

# the idea is when we get a number we insert as key the number+1 and increment the value which is the count
# if the
# or can we do this, for every number start counting the longest consecutive subsequence from that number
# and update the smaller values as well

def array_subset(arr1, arr2):
    temp = dict()
    for i in range(len(arr1)):
        if arr1[i] not in temp.keys():
            temp[arr1[i]] = 1
    for i in range(len(arr2)):
        if arr2[i] not in temp.keys():
            return 0

    return 1


for t in range(T):
    n, m = list(map(int, input().strip().split())) # size of the first and second array respectively
    arr1 = list(map(int, input().strip().split()))
    print('arr: {}, n: {}'.format(arr1, n))
    arr2 = list(map(int, input().strip().split()))
    print('arr: {}, n: {}'.format(arr2, m))
    if array_subset(arr1, arr2) == 1:
        print('yes')
    else:
        print('No')


