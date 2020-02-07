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

    def top(self):
        if self.front is None:
            return -1
        else:
            temp = self.front
            return temp.data

def next_larger(s, n):
    s = s.split()
    my_stack = stack()
    str = None
    my_stack.push(s[0])
    for i in range(1, n):
        if int(s[i]) > int(my_stack.top()):
            my_stack.pop()
            if str is None:
                str = s[i] + ' '
            else:
                str = str + s[i] + ' '
        my_stack.push(s[i])
    
    print(str)


for t in range(T):
    s = st_list[t]
    n = N_list[t]
    next_larger(s, n)
