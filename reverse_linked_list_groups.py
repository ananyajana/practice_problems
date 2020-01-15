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


def reverse_groups(head, k):
    cnt = 0
    if head is None:
        return None

    n = 0
    test = head
    while(test):
        test = test.next
        n += 1
    cur = head
    
    # to hold the new head element
    new_head = None
    # prev_last: to hold the last element of the last group
    # cur_last: to hold the last element of the current group
    prev_last = cur_last = None
    # reversing is done in three steps
    # get the first element as the current last(would-be-last after reversing) element
    # keep the cur_last in the prev_last for the next group
    # reverse the current group
    # change the current group's last pointer(cur_last) to point to next group
    # change the previous group's last pointer to the beginning of the current group after reversing(temp)
    # temp holds the first element of the current group, so after the first group is processed, temp is the new head
    while(cur):
        #print('here :')
        cnt = 0
        temp = None
        while(cur and cnt < k):
            #print('here 2:')
            if cur_last is None:
                cur_last = cur 
            temp2 = cur.next
            cur.next = temp
            temp = cur
            cnt += 1
            cur = temp2

        if new_head is None:
            new_head = temp 
        if prev_last is not None:
            prev_last.next = temp
        if cur_last is not None:
            #cur_last.next = cur
            prev_last = cur_last
            cur_last = None

    head = new_head
    return new_head

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
    k = K_list[t]
    #print(n)
    #print(s1)
    #print(k)
    llist = create_linked_list(s1, n)
    #llist.print_list()
    llist.head = reverse_groups(llist.head, k)
    llist.print_list()
