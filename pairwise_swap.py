# problems from geeksforgeeks must do coding questions

T = int(input())
N_list = []
st_list = []
for t in range(T):
    N_list.append(int(input()))
    st_list.append(input())

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
            print(temp.data)
            temp = temp.next

def create_linked_list(s, n):
    data_list = []
    data_list = s.split()
    #print(data_list)
    #print(s)
    llist = linked_list()
    first = Node(data_list[0])
    llist.head = new_node = first
    #new_node = new_node.next
    for i in range(1, n):
        new_node.next = Node(int(data_list[i]))
        new_node = new_node.next

    #llist.print_list()
    return llist

def pair_swap(head):
    i = 0
    temp = head
    new_head = None
    prev_prev = None
    while(temp):
        if temp.next is not None:
            # if prev exist make it prev_prev because
            # prev will be set to current temp node
            if prev is not None:
                prev_prev = prev
            # if this is not the first pair, then the
            # last node of the previ
            if prev_prev is not None:
                prev_prev.next = temp.next
            prev = temp
            temp2 = temp.next
            #if the new head is not set previously, set it
            # this happens only once
            if new_head is None:
                new_head = temp.next

            # swap the pointers to reverse the pair
            temp.next = temp.next.next
            new_head.next = temp
            
            # set the pointer to the first node of the next pair
            temp = temp.next 
    if new_head is not None:
        return new_head
    else:
        return head

for t in range(T):
    #s1 = input()
    s1 = st_list[t]
    n = N_list[t]
    llist = create_linked_list(s1, n)
    #llist.print_list()
    llist.head = pair_swap(llist.head)
