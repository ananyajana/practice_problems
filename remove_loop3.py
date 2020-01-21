# problems from geeksforgeeks must do coding questions

T = int(input())
st_list =[]
N_list = []
X_list = []
for t in range(T):
    N_list.append(int(input()))
    st_list.append(input())
    X_list.append(int(input()))

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

def create_loop(head, x):
	if x == 0:
		return head
	cnt = 0
	cur = cur2 = head
	while cnt < x - 1:
		cur = cur.next
		cnt += 1

	while cur2.next:
		cur2 = cur2.next

	cur2.next = cur
	return head
	

def print_list_ten_elems(head):
    cnt = 0
    cur = head
    while(cnt < 10) and cur:
        print(cur.data)
        cur = cur.next
        cnt += 1

def detect_loop(head):
    slow_p = head
    fast_p = head
    while(slow_p and fast_p and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p:
            return 1
    return 0

def remove_loop(head):
    slow_p = head
    fast_p = head
    cur = None
    loop_node = None
    while(slow_p and fast_p and fast_p.next):
        print('in while')
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p:
            loop_node = cur = slow_p
            break

    if slow_p is None or fast_p is None or slow_p.next is None or fast_p is None:
        return

    temp = loop_node
    cnt = 0
    if temp is not None:
        while temp.next != loop_node:
            cnt += 1
            temp = temp.next
        cnt += 1
    #print('# of nodes in the loop: ', cnt)

    # set one node to the the head of the list and another
    # pointer to the k th node in the list
    i = 0
    temp = cur = head
    while i < cnt:
        temp = temp.next
        i += 1

    # start traversing k nodes from head and kth node
    prev = None
    #print('cur data :', cur.data)
    #print('temp data :', temp.data)
    while cur != temp:
        #print('cur data :', cur.data)
        #print('temp data :', temp.data)
        prev = temp
        cur = cur.next
        temp = temp.next

    # prev.next points to loop node
    if prev is not None:
        prev.next = None

    
        
    

for t in range(T):
    #s1 = input()
    s1 = st_list[t]
    n = N_list[t]
    x = X_list[t]
    llist = create_linked_list(s1, n)
    llist.head = create_loop(llist.head,  x)
    #print_list_ten_elems(llist.head)
    #llist.print_list()
    if detect_loop(llist.head)  == 1:
        print('True')
    else:
        print('False')
    remove_loop(llist.head)

    llist.print_list()
	
