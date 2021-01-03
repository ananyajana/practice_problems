import atexit
import io
import sys
import heapq
from collections import defaultdict

def insertHeaps(x):
    global min_heap, max_heap
    min_size = len(min_heap)
    max_size = len(max_heap)
    if (min_size == max_size) or ((max_size - min_size) == 1):
        heapq.heappush(min_heap, x)
    elif (min_size - max_size) == 1:
        heapq.heappush(max_heap, -x)

def getMedian():
    global min_heap, max_heap
    min_size = len(min_heap)
    max_size = len(max_heap)
    if (min_size == max_size):
        l = min_heap[0]
        u = -max_heap[0]
        return float(l + u)/2
    elif (min_size - max_size) == 1:
        return min_heap[0]
    elif (max_size - min_size) == 1:
        return max_heap[0]

        

min_heap = [] # our mean heap to be used for the  upper half of the data
max_heap = [] # our max heap to be used for the lower half of the data

print('size of minheap', len(min_heap))
print('size of maxheap', len(max_heap))

#min_heap = [3, 2, 1, 4, 5, 6]
#max_heap = [13, 12, 11, 14, 15, 16]

heapq.heapify(min_heap)
heapq._heapify_max(max_heap)

print('size of minheap', len(min_heap))
print('size of maxheap', len(max_heap))
print('min_heap is', min_heap)
print('max_heap is', max_heap)

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
