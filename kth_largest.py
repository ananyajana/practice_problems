#User function Template for python3
# function to build min heap


# need to maintain of minheap or k elements.
# whenever a next element comes, the kth largest element is checked.
# if it is smaller than the minimum element then ignored. Otherwise
# the minheap is poppoed and the new element inserted
T = int(input())
st_list =[]
for t in range(T):
    st_list.append(input())

for t in range(T):
    s1 = st_list[t]
        

# make a list of count of all the characters of the string count[c - 'a']
NUM = 26
# make a priority queue to hold the character and its frequency with frequency
# as the key

# Now the list needs to be processed so that the strings could be processed to
# make a priority queue with the count of the elements
for t in range(T):
    s1 = st_list[t]

    count = [0] * NUM
    pq = []
    for i in range(len(s1)):
        count[ord(s1[i]) - ord('a')] += 1

    print(count)
    for i in range(NUM):
        if count[i]:
            # remember in python heap1 is a min heap, but we want a max
            # heap based priority queue
            heapq.heappush(pq, (count[i] * (-1), chr(ord('a') + i)))

    print(pq)

    # this will store the resultant value
    str = ''

    # work as the previous visited element
    # initial previous elements be. ('#' and its frequency is -1)
    prev = (-1, '#')

    # traverse the queue
    while (len(pq)) != 0:
        # pop the element with the highest frequency
        k = heapq.heappop(pq)
        str = str + k[1]

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
    if l <= n-1 and arr[l] < arr[i]:
        smallest = l
    else:
        smallest = i
    if r <= n-1 and arr[r] < arr[smallest]:
        smallest = r
    
    if smallest != i:
        print('swapping {} with {}'.format(arr[smallest], arr[i]))
        temp = arr[smallest]
        arr[smallest] = arr[i]
        arr[i] = temp
    
        heapify(arr, n, smallest)

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

def isLeaf(pos):
    global n, arr
    if pos < n and pos >= (n // 2):
        return True
    return False

# if the node has children, then keep on pushing this node by exchangin it with
# the minimum of the child nodes at every step. At the end of this step, the
# node will become a leaf node. At this step we delete this leaf. if the leaf 
# node is from second last layer then we can delete the node and replace with 
# the last leaf node in the last level
def deleteKeyi_old(i):
    global n, arr
    if i >= n:
        raise ValueError('pos is greater than heap size, valid positions are 0 to n - 1')
    
    # if the node is non leaf node then push it downwards to make it a leaf node
    while isLeaf(i) is False:
        print('n = ', n)
        # code here
        l = left(i)
        print('l = ', l)
        r = right(i)
        print('r = ', r)
        if l <= n-1 and arr[l] < arr[i]:
            smallest = l
        else:
            smallest = i
        if r <= n-1 and arr[r] < arr[smallest]:
            smallest = r
        
        if smallest != i:
            print('swapping {} with {}'.format(arr[smallest], arr[i]))
            temp = arr[smallest]
            arr[smallest] = arr[i]
            arr[i] = temp
            
            i = smallest
        
    # now the node to be deleted is a leaf node
    # check if it is the last leaf node, then nothing to be done
    # is deletion at a specific position similar to deletion from root?
    # i.e. swap the node with the last node and then run heapify at the
    # position? Because it looks like we are doing the same thing over here.

def deleteKey(i):
    global n, arr
    if n == 0:
        raise ValueError('Heap is empty')
    if i >= n:
        raise ValueError('pos is greater than heap size, valid positions are 0 to n - 1')
    # exchange the node at the position i with the last node
    temp = arr[i]
    arr[i] = arr[n - 1]
    arr[n - 1] = temp
    
    # decrease the size of the heap by one
    n = n - 1

    # run heapify on the node at position i if it is a non leaf node
    if isLeaf(i) is False:
        heapify(arr, n, i)

def extractMin():
    global n, arr
    if n == 0:
        raise ValueError('Heap is empty')
    min_key = arr[0]
    deleteKey(0)
    return min_key


def insertKey(x):
    global n, arr
    if len(arr) <= n:
        raise ValueError('Heap size exceeded. Exit!')
    else:
        arr[n] = x
        cur = n
        n = n + 1
        par = parent(cur)
        while arr[cur] < arr[par]:
            temp = arr[cur]
            arr[cur] = arr[par]
            arr[par] = temp
            cur = par
            par = parent(cur)

#arr = [4, 5, 6, 7, 8]
arr = [8, 7, 6, 5, 4, 0, 0, 0]
n = len(arr)
n = 5
k = 3
buildHeap(arr,n)
print(arr)
insertKey(10)
print(arr)
insertKey(1)
print(arr)
for i in range(7):
    print('is leaf pos: {} {}'.format(i, isLeaf(i)))

deleteKey(4)
print(arr)
deleteKey(1)
print(arr)
print('the min elements extracted is:', extractMin())
print(arr)
print('the min elements extracted is:', extractMin())
print(arr)

kth_max_heap = []

arr = [8, 7, 6, 5, 4, 10, 16, 2, 1, 3]
i = 0
while i < k-1:
    print('-1')
    heapq.heappush(kth_max_elem, arr[i])
    i += 1

for i in range(k-1, n):
    if arr[i] > kth_max_heap[0]:
        print(heapq.heappushpop(kth_max_heap, arr[i]))

