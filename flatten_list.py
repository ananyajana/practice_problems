# problems from geeksforgeeks must do coding questions

T = int(input())
sz_list =[]
N_list = []
lists = []
for t in range(T):
    N_list.append(int(input()))
    sz_list.append(input())
    lists.append(input())

class Node:
    # fn to initialize the node object
    def __init__(self, data):
        self.data = data
        self.right = None
        self.bottom = None

#linked list contains a node object
class linked_list:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.bottom

    def print_list_horz(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.right


def create_linked_list(s, n):
    data_list = s
    #data_list = s.split()
    #print(data_list)
    #print(s)
    llist = linked_list()
    first = Node(data_list[0])
    llist.head = new_node = first
    #new_node = new_node.next
    for i in range(1, n):
        new_node.bottom = Node(int(data_list[i]))
        new_node = new_node.bottom

    #llist.print_list()
    return llist


for t in range(T):
    #s1 = input()
    sz = sz_list[t]
    n = N_list[t]
    x = lists[t]
    print(n)
    print(sz)
    print(x)

    sub_list = []
    sub_list = sz.split()
    print(sub_list)
    for i in range(len(sub_list)):
        sub_list[i] = int(sub_list[i])
    print(sub_list)

    elem_list = []
    elem_list = x.split()
    print(elem_list)
    for i in range(len(elem_list)):
        elem_list[i] = int(elem_list[i])
    print(elem_list)

    
    cnt = 0
    llists = ['0']*n
    for i in range(n):
        k = sub_list[i]
        temp_list = ['0']*k
        for j in range(k):
            temp_list[j] = elem_list[cnt + j]
        cnt += k
        print('temp list {} is {}'.format(i, temp_list))
        llists[i] = create_linked_list(temp_list, k)

    for i in range(n):
        llists[i].print_list()
        
    llist = linked_list()
    llist.head = llists[0].head
    for i in range(n - 1):
        llists[i].head.right = llists[i + 1].head

    llist.print_list_horz()
