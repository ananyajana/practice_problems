T = int(input())

# the key insight is that the sum of two numbers to be divisible by k
# the sum of the remainders(%k) of the two numbers i.e. (a+b) % k = 0
# iff (a%k + b%k)%k =0
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


