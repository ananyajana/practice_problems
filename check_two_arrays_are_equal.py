import operator
T = int(input())

# check if two arrays are equal
def equal(arr1, arr2):
    temp = dict()
    for i in range(len(arr1)):
        if arr1[i] not in temp.keys():
            temp[arr1[i]] = 1
        else:
            temp[arr1[i]] += 1
    for j in range(len(arr2)):
        if arr2[j] in temp.keys():
            temp[arr2[j]] -= 1
            if temp[arr2[j]] == 0:
                del temp[arr2[j]]
        else:
            return -1

    if not temp:
        return 0
    else:
        return -1

for t in range(T):
    n = int(input())
    arr1 = list(map(int, input().strip().split()))
    m = int(input())
    arr2 = list(map(int, input().strip().split()))
    print('arr1: {}, n: {}, arr2: {}, m: {}'.format(arr1, n, arr2, m))
    val = equal(arr1, arr2)
    if val == -1:
        print('not equal')
    else:
        print('equal')

