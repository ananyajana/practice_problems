import operator
T = int(input())

# the idea is when we get a number we insert as key the number+1 and increment the value which is the count
# if the
# or can we do this, for every number start counting the longest consecutive subsequence from that number
# and update the smaller values as well

def array_subset(arr1, arr2, n, m, k):
    temp = dict()
    all_pairs = []
    for i in range(n):
        if arr1[i] not in temp.keys():
            temp[k - arr1[i]] = 1
    for i in range(m):
        if arr2[i] in temp.keys():
            all_pairs.append([arr2[i], k-arr2[i]])

    return all_pairs


for t in range(T):
    n, m = list(map(int, input().strip().split())) # size of the first and second array respectively
    arr1 = list(map(int, input().strip().split()))
    print('arr: {}, n: {}'.format(arr1, n))
    arr2 = list(map(int, input().strip().split()))
    k = int(input())
    print('arr: {}, n: {}'.format(arr2, m))
    print(array_subset(arr1, arr2, n, m, k))


