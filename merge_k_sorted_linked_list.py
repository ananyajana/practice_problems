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

class Node:
    # fn to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

#linked list contains a node object
class linked_list:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

    def create_linked_list(self, arr):
        n = len(arr)
        i = 1
        if n != 0:
            self.head = new_node = Node(arr[0])
            while i < n:
                new_node.next = Node(arr[i])
                new_node = new_node.next
                i +=1

        return self.head

# compare the elements in front of the linked lists
# have the key as the current element in the min heap
# an the valus is the indices [index in the array, index of the list]]
# first make an array
def merge_k_linked_lists(arr, n):
    new_heap = [] 
    #heapq.heapify(new_heap)

    # initially push all the elements at 0th location
    # of all the lists
    for i in range(n):
        #heapq.heappush(new_heap, [arr[i].head.data,[arr(i).head, i]])
        if arr[i].head is not None:
            heapq.heappush(new_heap, [arr[i].head.data, arr[i].head.next])

    #print(new_heap)
    # the combined array will hold the
    combined_arr = []
    new_ll = linked_list()
    
    # pop the elements and move the pointer one step ahead in the
    # same list to enqueue the next element from it
    while len(new_heap) != 0:
        cur_elem = heapq.heappop(new_heap)
        combined_arr.append(cur_elem[0])
        #ll_idx = cur_elem[1][1]
        #item_ptr = cur_elem[1][0]
        item_ptr = cur_elem[1]
        if item_ptr is not None:
            heapq.heappush(new_heap, [item_ptr.data, item_ptr.next])
    print(combined_arr)


# code execution starts here
if __name__=='__main__':
    # start with the empty list
    k_arrs = [[1, 2, 3], [4, 5], [6, 7, 8]]

    llist1 = linked_list()
    llist1.create_linked_list(k_arrs[0])
    llist2 = linked_list()
    llist2.create_linked_list(k_arrs[1])
    llist3 = linked_list()
    llist3.create_linked_list(k_arrs[2])

    print('list1 is')
    llist1.print_list()
    print('list2 is')
    llist2.print_list()
    print('list3 is')
    llist3.print_list()

    arr = [llist1, llist2, llist3]
    n = len(arr)
    merge_k_linked_lists(arr, n)
