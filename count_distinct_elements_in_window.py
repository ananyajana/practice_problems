T = int(input())

# find all unique quadruples from the given array that sums up to the nuique number
# the elements need not be contiguous

def count_distinct(arr, n, k):
    res = []
    for i in range(n-3):
        counts = dict()
        for j in range(k):
            if arr[i+j] not in counts.keys():
                counts[arr[i+j]] = 1
            else:
                counts[arr[i+j]] += 1
        print('counts:', counts)
        res.append(len(counts))
    return res
    

for t in range(T):
    n = int(input())
    k = int(input())
    arr = list(map(int, input().strip().split()))
    print('arr: {}, n: {}, k: {}'.format(arr, n, k))
    print(count_distinct(arr, n, k))


