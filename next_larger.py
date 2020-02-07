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

class stack:
    def __init__(self):
        self.front = None

    # method to add an item to the queue
    def push(self, item):
        node = Node(item)
        if self.front is not None:
            node.next = self.front
        self.front = node

    # method to remove an item from the queue
    def pop(self):
        if self.front is None:
            return -1
        else:
            temp = self.front
            self.front = self.front.next
            return temp.data

def next_larger(s, n):
    print('in next_larger')
    s = s.split()
    my_stack = stack()
    for i in range(n):
        for j in range(i, n):
            if s[j] > s[i]:
                print('pushing {} for {}'.format(s[j], s[i]))
                my_stack.push(s[j])
                break 
    # push -1 on the stack for the last element
    my_stack.push(-1)
    print(my_stack.pop())
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
for t in range(T):
    s = st_list[t]
    n = N_list[t]
    next_larger(s, n)
