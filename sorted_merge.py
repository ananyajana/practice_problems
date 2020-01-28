# problems from geeksforgeeks must do coding questions

T = int(input())
N_list = []
list1 =[]
list2 =[]
for t in range(T):
    N_list.append(input())
    list1.append(input())
    list2.append(input())

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

def merge(head_a, head_b):
    if head_a is None:
        return head_b
    if head_b is None:
        return head_a

for t in range(T):
    #s1 = input()
    n = N_list[t]
    n1, n2 = n.split()
    l1 = list1[t]
    l2 = list2[t]
    llist1 = create_linked_list(l1, int(n1))
    llist2 = create_linked_list(l2, int(n2))
    llist1.print_list()
    llist2.print_list()

    llist1.head = merge(llist1.head, llist2.head)
    llist1.print_list()
