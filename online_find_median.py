import atexit
import io
import sys
import heapq
from collections import defaultdict

root = None
def insertHeaps(x):
    global root
    global min_heap, max_heap
    # having the <= sign is mandatory over here because
    # if the sequence is something like this 21, 23, 22
    # then root will be 22 after th insertion of 21 and 23
    # and hence it will match the 3rd key 22
    if root is None:
        heapq.heappush(max_heap, -x)
        root = x
    else:
        if x <= root:
            heapq.heappush(max_heap, -x)
        else:
            heapq.heappush(min_heap, x)

        min_size = len(min_heap)
        max_size = len(max_heap)
        if (abs(min_size - max_size) > 1):
            balanceHeaps()
        update_root()

# after bal;ance heap the size of the heaps may change
def update_root():
    global min_heap, max_heap, root
    min_size = len(min_heap)
    max_size = len(max_heap)
    if (min_size == max_size):
        l = min_heap[0]
        u = -max_heap[0]
        root = float(l + u)/2
    elif (min_size - max_size) == 1:
        root = min_heap[0]
    elif (max_size - min_size) == 1:
        root = -max_heap[0]

def balanceHeaps():
    global root
    global min_heap, max_heap
    min_size = len(min_heap)
    max_size = len(max_heap)
    if min_size > max_size:
        print('min_size > max_size')
        while ((min_size - max_size) > 1):
            print('balanceHeaps: min_heap is', min_heap)
            print('balanceHeaps: max_heap is', max_heap)
            x = heapq.heappop(min_heap)
            print(' popped element from min_heap', x)
            heapq.heappush(max_heap, -x)
            print('balanceHeaps: min_heap is', min_heap)
            print('balanceHeaps: max_heap is', max_heap)
            min_size = len(min_heap)
            max_size = len(max_heap)
    else:
        while ((max_size - min_size) > 1):
            x = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -x)
            min_size = len(min_heap)
            max_size = len(max_heap)

def getMedian():
    global root
    return root

        

min_heap = [] # our mean heap to be used for the  upper half of the data
max_heap = [] # our max heap to be used for the lower half of the data

print('size of minheap', len(min_heap))
print('size of maxheap', len(max_heap))

#min_heap = [3, 2, 1, 4, 5, 6]
#max_heap = [13, 12, 11, 14, 15, 16]

heapq.heapify(min_heap)
heapq.heapify(max_heap)
#heapq._heapify_max(max_heap)

'''
print('size of minheap', len(min_heap))
print('size of maxheap', len(max_heap))
print('min_heap is', min_heap)
print('max_heap is', max_heap)
'''
insertHeaps(21)
print('median element:', getMedian())
insertHeaps(22)
print('median element:', getMedian())
insertHeaps(23)
print('median element:', getMedian())
print('size of minheap', len(min_heap))
print('size of maxheap', len(max_heap))
print('min_heap is', min_heap)
print('max_heap is', max_heap)
insertHeaps(24)
print('median element:', getMedian())
insertHeaps(25)
print('median element:', getMedian())
insertHeaps(26)
print('median element:', getMedian())
insertHeaps(27)
print('median element:', getMedian())
insertHeaps(28)
print('median element:', getMedian())
print('size of minheap', len(min_heap))
print('size of maxheap', len(max_heap))
print('min_heap is', min_heap)
print('max_heap is', max_heap)
'''
if __name__=='__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        for i in range(n):
            insertHeaps(int(input()))
            # call this function to balance the two heaps, such that
            # their size does not differ by more than 1.
            balanceHeaps()
            # print the median
            print(getMedian())
'''
