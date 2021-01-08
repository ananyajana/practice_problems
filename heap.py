#User function Template for python3
def heapify(arr, n, i):
    '''
    :param arr: original array
    :param n: size of original array
    :param i: subtree rooted at ith index
    :return: 
    '''
    # code here
    l = left(i)
    r = right(i)
    if l <= n and arr[l] > arr[i]:
        largest = l
    else:
        largest = k
    if r <= n and arr[r] > arr[largest]:
        largest = r
    
    if largest != k:
        temp = arr[largest]
        arr[largest] = arr[k]
        arr[k] = arr[largest]
    
    heapify(arr, n, largest)

def buildHeap(arr,n):
    '''
    :param arr: given array
    :param n: size of array
    :return: None
    '''
    # code here
    for k in reversed(range(n/2 + 1))

def right(pos):
    return (2 * pos) + 2

def left(pos):
    return 2 * pos + 1

def parent(pos):
    return (pos - 1) // 2
