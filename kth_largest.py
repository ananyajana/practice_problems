#User function Template for python3
# function to build min heap


# need to maintain of minheap or k elements.
# whenever a next element comes, the kth largest element is checked.
# if it is smaller than the minimum element then ignored. Otherwise
# the minheap is poppoed and the new element inserted
'''
T = int(input())
st_list =[]
for t in range(T):
    st_list.append(input())

for t in range(T):
    s1 = st_list[t]
'''        
import heapq

kth_max_heap = []

arr = [8, 7, 6, 5, 4, 10, 16, 2, 1, 3]
n = len(arr)
k = 3
i = 0
while i < k-1:
    print('-1')
    heapq.heappush(kth_max_heap, arr[i])
    i += 1

# pushing the kth element on the heap
heapq.heappush(kth_max_heap, arr[k-1])

print('kth_max_heap', kth_max_heap)


for i in range(k-1, n):
    if arr[i] > kth_max_heap[0]:
        #print('arr[i]: ', arr[i])
        #print('kth_max_heap: ', kth_max_heap)
        print(heapq.heappushpop(kth_max_heap, arr[i]))
    else:
        print(kth_max_heap[0])

