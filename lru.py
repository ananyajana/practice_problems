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
        self.prev = None

class doubly_linked_queue:
    def __init__(self):
        self.front = None

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
            node.prev = temp

    # method to remove an item from the queue
    def pop(self):
        if self.front is None:
            return -1
        else:
            temp = self.front
            self.front = self.front.next
            self.front.prev = None
            temp.next = None
            return temp.data
    def print_queue(self):
        temp = self.front
        print('printing from the front')
        while temp.next is not None:
            print(temp.data)
            temp = temp.next
        print(temp.data)

        print('printing from the back')
        while temp.prev is not None:
            print(temp.data)
            temp = temp.prev
        print(temp.data)

for t in range(T):
    s = st_list[t]
    n = N_list[t]
    my_queue = doubly_linked_queue()
    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)
    my_queue.push(4)
    my_queue.push(5)

    my_queue.print_queue()
