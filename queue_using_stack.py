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

    def empty(self):
        if self.front is None:
            return True
        else:
            return False
s1 = stack()
s2 = stack()

def qPush(x):
    #code here
    s1.push(x)

def qPop():
    #code here
    while s1.empty() is False:
        s2.push(s1.pop())
    elem = s2.pop()
    while s2.empty() is False:
        s1.push(s2.pop())
    
    return elem
for t in range(T):
    s = st_list[t]
    n = N_list[t]
    next_larger(s, n)
