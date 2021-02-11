T = int(input())

# find all unique quadruples from the given array that sums up to the nuique number
# the elements need not be contiguous

def find_four(arr, val):
    arr.sort()
    n = len(arr)
    quads = []
    for i in range(n-3):
        for j in range(i+1, n-2):
            # initialize the two variables as indexes of the first and last elemet
            # in the remaining elements
            l = j + 1
            r = n - 1
            
            # to find the remaining two elements,
            # move the index variables (l & r)
            # toward each other
            while l < r:
                if arr[i] + arr[j] + arr[l] + arr[r] == val:
                    quads.append([arr[i], arr[j], arr[l], arr[r]])
                    l += 1
                    r -= 1
                elif arr[i] + arr[j] + arr[l] + arr[r] < val:
                    l += 1
                else:
                    r -= 1

    return quads
    

for t in range(T):
    n = int(input())
    k = int(input())
    arr = list(map(int, input().strip().split()))
    print('arr: {}, n: {}, k: {}'.format(arr, n, k))
    print(find_four(arr, k))


