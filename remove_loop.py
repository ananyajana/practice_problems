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

def remove_loop(head):
    slow_p = head
    fast_p = head
    cur = None
    while(slow_p and fast_p and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p:
            cur = slow_p

    # initialize a ptr to the head node
    cur2 = head
    # initialize a ptr to one of the nodes inside the head node
    temp = cur
    # move head ptr one by one to check if the loop is reached.
    # if loop is reached then it should be reachable from temp
    while(1):
        # the node we are searching for is not yet found
        # neither the starting point of temp is reached
        # so increment ptr
        if temp.next != cur2 or temp.next != cur:
            temp = temp.next

        # if cur2 is reached then there is a loop, break the loop
        if temp.next == cur2:
            break
        cur2 = cur2.next

    # after the end of loop temp is the node pointing to the last
    # node of the loop. So, make next of temp node as None
    cur.next = None
    

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
