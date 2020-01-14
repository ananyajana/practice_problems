# problems from geeksforgeeks must do coding questions

T = int(input())
st_list =[]
N_list = []
K_list = []
for t in range(T):
    N_list.append(int(input()))
    st_list.append(input())
    K_list.append(int(input()))

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

    return llist

def rotate_list(head, k):
    cnt = 0
    if head is None:
        return None

    cur = temp = head
    while(cur and cnt < k):
        #print('here:')
        prev_cur = cur
        cur = cur.next
        cnt += 1
    
    temp = new_cur = prev = cur
    while(new_cur):
        #print('here2:')
        prev = new_cur
        new_cur = new_cur.next

    prev_cur.next = prev.next
    prev.next = head
    
    return temp
    

for t in range(T):
    #s1 = input()
    s1 = st_list[t]
    n = N_list[t]
    k = K_list[t]
    llist = create_linked_list(s1, n)
    if k != n:
        #print('k != n')
        llist.head = rotate_list(llist.head, k)
    llist.print_list()
