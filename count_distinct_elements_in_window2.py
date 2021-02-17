T = int(input())

# find all unique quadruples from the given array that sums up to the nuique number
# the elements need not be contiguous

def count_distinct(arr, n, k):
    res = []
    #n = len(arr)
    counts = dict()
    # process the first k elements first by putting them in a hashmap(key:count)
    for j in range(k):
        if arr[j] not in counts.keys():
            counts[arr[j]] = 1
        else:
            counts[arr[j]] += 1
    res.append(len(counts))
                
    for i in range(k, n):
        # insert the incoming element
        if arr[i] not in counts.keys():
              counts[arr[i]] = 1
        else:
            counts[arr[i]] += 1
        
        # delete the i-1 element i.e. the outgoing element
        if counts[arr[i-1]] == 1:
            del counts[arr[i-1]]
        else:
            counts[arr[i-1]] -= 1
            
        res.append(len(counts))
    return res
    

for t in range(T):
    n = int(input())
    k = int(input())
    arr = list(map(int, input().strip().split()))
    print('arr: {}, n: {}, k: {}'.format(arr, n, k))
    print(count_distinct(arr, n, k))


