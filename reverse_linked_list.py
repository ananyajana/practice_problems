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
    def reverse_list(self):
        if self.head is None:   
            return None
        cur = new_head = self.head
        temp = None
        temp2 = cur.next
        cur.next = temp
        temp = cur
        new_head = cur
        cur = temp2
        while(cur):
            temp2 = cur.next
            cur.next = temp
            temp = cur
            new_head = cur
            cur = temp2

        self.head = new_head

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

for t in range(T):
    #s1 = input()
    s1 = st_list[t]
    n = N_list[t]
    llist = create_linked_list(s1, n)
    #llist.print_list()
    llist.reverse_list()
    llist.print_list()
