# using max heap method for sliding window maximum
# pick the first k elements and create a max heap of size k
# perform heapify and print root element
# store the next and the last element from the array
# run a loop from k-1 to n
#   i.replace the value of element which is got out of the window with
#   new element which came inside the window
#   ii. perform heapify
#   iii. print the root of the heap

# why does it not mattwe whiche element is going out of heap?
# can I come up with some counter example that it will not work?

T = int(input())
st_list =[]
N_list = []
for t in range(T):
    N_list.append(input())
    st_list.append(input())
    
import heapq

def find_max_of_subarrays(s, n):
    #print('here')
    n, k = n.split()
    #print(s)
    n = int(n)
    k = int(k)
    s = s.split()
    s = [int(s[i]) for i in range(len(s))]
    i = 0
    j = k-1
    
    # create heap and heapify
    heap = s[i:j+1]
    print('subarray before heapify :', heap)
    heapq._heapify_max(heap)
    print('subarray after heapify :', heap)
    # print the max element from the first window of size k
    print(heap[0], end = " ")
    last = s[i] # first element of the current subarray is the outgoing element
    i += 1  # increment the beginning of the window
    j += 1  # increment the end of the window
    nexts = s[j]
    
    # for every remaining element
    while j < n:
        # add the next element of the window
        # we are replacing the last element of
        # the heap array, but that may not be the
        # outgoing element?
        heap[heap.index(last)] = nexts
        
        # heapify to get the maximum of the 
        # current window at the root again
        heapq._heapify_max(heap)
        
        print('heap at window {}'.format(heap, i))
        # print the current maximum
        print(heap[0], end=" ")
        last = s[i]
        j += 1
        i += 1
        if j < n:
            nexts = s[j]
        
    

for t in range(T):
    s1 = st_list[t]
    n = N_list[t]
    #print(n)
    #print(s1)
    
    find_max_of_subarrays(s1, n)
