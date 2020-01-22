# problems from geeksforgeeks must do coding questions

T = int(input())
st_list =[]
N_list = []
X_list = []
for t in range(T):
    n, x = input().split()
    N_list.append(int(n))
    X_list.append(int(x))
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

def nth_from_end(head, x):
    cnt = 0
    temp = head	
    while temp:
        cnt += 1
        temp = temp.next

    if cnt < x:
        return -1
    else:
        k = cnt - x
        j = 0
        temp = head
        while j < k:
            temp = temp.next
            j += 1
        return temp.data

for t in range(T):
    #s1 = input()
    s1 = st_list[t]
    n = N_list[t]
    x = X_list[t]
    llist = create_linked_list(s1, n)
    #llist.print_list()
    print(nth_from_end(llist.head, x))
