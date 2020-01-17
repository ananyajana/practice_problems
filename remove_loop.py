# problems from geeksforgeeks must do coding questions

T = int(input())
N_list =[]
st_list = []
x_list = []
for t in range(T):
    N_list.append(input())
    st_list.append(input())
    x_list.append(input())

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

def create_linked_list(s, n, x):
    data_list = []
    data_list = s.split()
    #print(data_list)
    #print(s)
    llist = linked_list()
    first = Node(data_list[0])
    llist.head = cur = new_node = first
    #new_node = new_node.next
    cnt = 0
    if cnt == int(x) - 1:
        loop_node = first
    for i in range(1, int(n)):
        new_node.next = Node(int(data_list[i]))
        prev = new_node
        new_node = new_node.next
        cnt += 1
        if cnt == int(x) - 1:
            loop_node = cur

    prev.next = loop_node
    #llist.print_list()
    return llist.head


def find_merge_point(head_a, head_b):
    len1 = len2 = 0
    # find the length of the first list
    cur = head_a
    while(cur):
        cur = cur.next
        len1 += 1

    # find the length of the second list
    cur = head_b
    while(cur):
        cur = cur.next
        len2 += 1

    # find the absolute difference between the two lengths
    # and in the longer list travel upto that many nodes
    if len1 > len2:
        diff = len1 - len2
        cur = head_a
        cur2 = head_b
        small = len2
    else:
        diff = len2 - len1
        cur = head_b
        cur2 = head_a
        small = len1
    cnt = 0
    while(cnt < diff):
        cur = cur.next
        cnt += 1
    
    cnt = 0
    while(cnt < small):
        if cur == cur2:
            return cur.data
        cur = cur.next
        cur2 = cur2.next
        cnt += 1

    return -1

for t in range(T):
    #s1 = input()
    n = N_list[t]
    s = st_list[t]
    x = x_list[t]
    llist1 = linked_list()
    llist1.head = create_linked_list(s, n, x)
    llist1.print_list()
    #llist2.print_list()
    #print(find_merge_point_remove(llist1.head, llist2.head))
