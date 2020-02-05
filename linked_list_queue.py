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

class MyQueue:
    def __init__(self):
        self.head = None

    # method to add an item to the queue
    def push(self, item):
        node = Node(item)
        if self.front is None:
            self.front = node
        else:
            temp = self.front
            while temp.next is not None:
                temp = temp.next
            temp.next = node
    
    # method to remove an item from the queue
    def pop(self):
        if self.front is None:
            return -1
        else:
            temp = self.front
            self.front = self.front.next
            return temp.data
    
for t in range(T):
    s1 = st_list[t]
    n = N_list[t]
