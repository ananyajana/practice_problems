import operator
T = int(input())

# the idea is when we keep the characters in a hash map, whenever we find a key that
# is already present, we print it.
def repeated_char(arr):
    temp = dict()
    for i in range(len(arr)):
        if arr[i] not in temp.keys():
            temp[arr[i]] = 1
        else:
            return arr[i]

    return -1


for t in range(T):
    T = int(input())
    arr = list(map(int, input().strip().split()))
    print('arr: {}'.format(arr))
    print(repeated_char(arr))


