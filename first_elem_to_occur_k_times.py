T = int(input())

import copy

def first_elem_that_occurs_k_times(arr1, k):
    temp = dict()
    for i in range(len(arr1)):
        print('arr[i]: ', arr1[i])
        if arr1[i] not in temp.keys():
            temp[arr1[i]] = 1
            if k == 1:
                return arr1[i]
        else:
            temp[arr1[i]] += 1
            if temp[arr1[i]] == k:
                return arr1[i]
        print('count: ', temp[arr1[i]])

    return -1


for t in range(T):
    k = int(input())
    arr1 = list(map(int, input().strip().split()))
    print('arr1: {}, k: {}'.format(arr1, k))
    val = first_elem_that_occurs_k_times(arr1, k)
    if val == -1:
        print('None')
    else:
        print('{} occurs {} times'.format(val, k))

