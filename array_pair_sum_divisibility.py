T = int(input())

# find all unique quadruples from the given array that sums up to the nuique number
# the elements need not be contiguous

def array_pair(arr, k):
    n = len(arr)
    temp = dict()
    for i in range(n):
        if (arr[i]%k) not in temp.keys():
            temp[k - (arr[i]%k)] = 1
        else:
            temp[arr[i]%k] -= 1
            if temp[arr[i]%k] == 0:
                del temp[arr[i]%k]

    print(temp)
    if len(temp) == 0:
        return 1
    else:
        return 0
    

for t in range(T):
    n = int(input())
    k = int(input())
    arr = list(map(int, input().strip().split()))
    print('arr: {}, n: {}, k: {}'.format(arr, n, k))
    print(array_pair(arr, k))


