T = int(input())

# find all unique quadruples from the given array that sums up to the nuique number
# the elements need not be contiguous

def find_four(arr, val):
    n = len(arr)
    quads = []
    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    print('[{} {} {} {}], sum: {}, k: {}'.format(arr[i], arr[j], arr[k], arr[l], (arr[i] + arr[j] + arr[k] + arr[l]), k))
                    if (arr[i] + arr[j] + arr[k] + arr[l]) == val:
                        print('[{} {} {} {}]'.format(arr[i], arr[j], arr[k], arr[l]))
                        quads.append([arr[i], arr[j], arr[k], arr[l]])

    return quads
    

for t in range(T):
    n = int(input())
    k = int(input())
    arr = list(map(int, input().strip().split()))
    print('arr: {}, n: {}, k: {}'.format(arr, n, k))
    print(find_four(arr, k))


