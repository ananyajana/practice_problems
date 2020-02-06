# problems from geeksforgeeks must do coding questions

T = int(input())
st_list =[]
N_list = []
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
    llist = linked_list()
    first = Node(int(data_list[0]))
    llist.head = new_node = first
    for i in range(1, n):
        new_node.next = Node(int(data_list[i]))
        new_node = new_node.next

    return llist

def delete_node(curr_node):
    if curr_node is not None:
        if curr_node.next is not None:
            temp = curr_node.data
            curr_node.data = curr_node.next.data
            curr_node.next.data = curr_node.data
            curr_node.next = curr_node.next.next
        else:
            curr_node = None

for t in range(T):
    #s1 = input()
    s1 = st_list[t]
    n = N_list[t]
    llist = create_linked_list(s1, n)
    llist.print_list()
    ptr = llist.head.next
    delete_node(ptr)
    #print(' the sorted list is :')
    llist.print_list()
