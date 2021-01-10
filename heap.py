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
    print('l = ', l)
    r = right(i)
    print('r = ', r)
    if l < n and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < n and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
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
    for k in range((n - 1)//2 + 1, -1, -1):
        print('k = ', k)
        heapify(arr, n, k)

def right(pos):
    return (2 * pos) + 2

def left(pos):
    return 2 * pos + 1

def parent(pos):
    return (pos - 1) // 2



arr = [4, 5, 6, 7, 8]
n = len(arr)
buildHeap(arr,n)
