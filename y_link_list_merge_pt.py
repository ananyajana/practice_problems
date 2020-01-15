# problems from geeksforgeeks must do coding questions

T = int(input())
num_list =[]
X_list =[]
Y_list =[]
Z_list =[]
for t in range(T):
    num_list.append(input())
    X_list.append(input())
    Y_list.append(input())
    Z_list.append(input())

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


def create_y_linked_list(nums, first, second, third):
    '''
    print(nums)
    print(first)
    print(second)
    print(third)
    '''
    x, y, z = nums.split()
    x = int(x)
    y = int(y)
    z = int(z)
    '''
    print(x)
    print(y)
    print(z)
    '''
    llist1 = linked_list()
    llist2 = linked_list()
    llist3 = linked_list()
    
    first = first.split()
    nd = Node(first[0])
    llist1.head = nd
    cnt = 1
    while(cnt < x):
        nd.next = Node(first[cnt])
        nd.next.next = None
        nd = nd.next
        cnt += 1
        prev1 = nd
    #llist1.print_list()
        
    second = second.split()
    nd = Node(second[0])
    llist2.head = nd
    cnt = 1
    while(cnt < y):
        nd.next = Node(second[cnt])
        nd.next.next = None
        nd = nd.next
        prev2 = nd
        cnt += 1
    #llist2.print_list()

    third = third.split()
    nd = Node(third[0])
    llist3.head = nd
    cnt = 1
    while(cnt < z):
        nd.next = Node(third[cnt])
        nd.next.next = None
        nd = nd.next
        cnt += 1
    #llist3.print_list()

    # the three linked lista have been created. Now let the
    # last node of first and second point to the first node 
    # of third and this is our y shaped list
    
    prev1.next = prev2.next = llist3.head
    llist1.print_list()
    llist2.print_list()
    #llist3.print_list()

for t in range(T):
    #s1 = input()
    nums = num_list[t]
    x = X_list[t]
    y = Y_list[t]
    z = Z_list[t]
    llist = create_y_linked_list(nums, x, y, z)
    #llist.print_list()
