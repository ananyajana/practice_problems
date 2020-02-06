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


def sort_0_1_2(head):
    temp = start = head
    last = prev = new_head = None

	
    while temp.next is not None:
        temp = temp.next
    #set the last pointer to the last node of the linked list
    last = end = temp
    # the linked list is traversed, whenever '0' node is found, it is
    # appended at the beginning and whenever '2' node is found, it is
    # appended at the end. In the most basic approach we will try with
    # a single node, but this can be tried with a series of '0' or '2'
    # nodes as well
    temp = head
    while temp is not None and (temp != end):
        # if temp.data matches '0' then append at the beginning
        if temp.data == 0:
	    # if this is the first node then nothing should be done,
	    # else remove temp from current position and append at the head
            if prev is not None:
                prev.next = temp.next
                temp.next = start
                start = temp
                temp = prev
        if temp.data == 2:
            # if this is the last node then nothing to be done,
            # else append temp at the end
            if temp.next is not None:
                prev.next = temp.next
                temp.next = None
                last.next = temp
                last = temp
                temp = prev
        cur = temp
        temp = temp.next
        if prev is None or prev.next != temp:
            prev = cur
    return start

for t in range(T):
    #s1 = input()
    s1 = st_list[t]
    n = N_list[t]
    llist = create_linked_list(s1, n)
    #llist.print_list()
    llist.head = sort_0_1_2(llist.head)
    print(' the sorted list is :')
    llist.print_list()