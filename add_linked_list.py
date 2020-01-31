# problems from geeksforgeeks must do coding questions

T = int(input())
N1_list = []
st1_list = []
N2_list = []
st2_list = []
for t in range(T):
    N1_list.append(int(input()))
    st1_list.append(input())
    N2_list.append(int(input()))
    st2_list.append(input())

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

# this program just swaps values and not te actual links
def pair_swap(head):
    i = 0
    temp = head
    while temp is not None:
        if temp.next is not None:
            temp_val = temp.data
            temp.data = temp.next.data
            temp.next.data = temp_val
            temp = temp.next.next
        else:        
            return head
    return head

for t in range(T):
    #s1 = input()
    s1 = st1_list[t]
    n1 = N1_list[t]
    llist1 = create_linked_list(s1, n1)
    s2 = st2_list[t]
    n2 = N2_list[t]
    llist2 = create_linked_list(s2, n2)
    llist1.print_list()
    llist2.print_list()
