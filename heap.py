#User function Template for python3
def heapify(arr, n, i):
    '''
    :param arr: original array
    :param n: size of original array
    :param i: subtree rooted at ith index
    :return: 
    '''
    print('n = ', n)
    # code here
    l = left(i)
    print('l = ', l)
    r = right(i)
    print('r = ', r)
    if l <= n-1 and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r <= n-1 and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
        print('swapping {} with {}'.format(arr[largest], arr[i]))
        temp = arr[largest]
        arr[largest] = arr[i]
        arr[i] = temp
    
        heapify(arr, n, largest)

def buildHeap(arr,n):
    '''
    :param arr: given array
    :param n: size of array
    :return: None
    '''
    # code here
    for k in range((n - 1)//2 - 1, -1, -1):
        print('k = ', k)
        heapify(arr, n, k)

def right(pos):
    return (2 * pos) + 2

def left(pos):
    return 2 * pos + 1

def parent(pos):
    return (pos - 1) // 2



arr = [4, 5, 6, 7, 8]
#arr = [8, 7, 6, 5, 4]
n = len(arr)
buildHeap(arr,n)
print(arr)
