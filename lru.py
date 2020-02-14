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

class doubly_ended_queue:
    def __init__(self):
        self.front = None
        self.end = None

    # method to add/enqueue an item to the end of the queue
    def push(self, item):
        node = Node(item)
        if self.front is None:
            self.front = self.end = node
        else:
            self.end.next = node
            node.prev = self.end
            self.end = node

    # method to remove/dequeue an item from the front of the queue
    def pop(self):
        if self.front is None:
            return -1
        else:
            temp = self.front
            self.front = self.front.next
            # if we have deleted the last node, update the end pointer
            if self.front is None:
                self.end = None
            # the node deleted was not the last node in the list, 
            # hence update the new front node's previous pointer
            else:
                self.front.prev = None
            temp.next = None
            return temp.data

    # method to remove/dequeue an item from the end
    def pop_from_end(self):
        if self.end is None:
            return -1
        else:
            temp = self.end
            self.end = self.end.prev
            # if the node deleted was not the last node in the list
            if self.end is not None:
                self.end.next = None
            # the last node has been deleted, update the front pointer
            else:
                self.front = None
            temp.next = temp.prev = None
            return temp.data
    
    # method to add/enqueue a data to the front of the queue
    def push_at_front(self, item):
        node = Node(item)
        if self.front is None:
            self.front = self.end = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node


    def print_queue(self):
        temp = self.front
        print('printing from the front')
        while temp.next is not None:
            print(temp.data)
            temp = temp.next
        print(temp.data)

        temp = self.end
        print('printing from the back')
        while temp.prev is not None:
            print(temp.data)
            temp = temp.prev
        print(temp.data)

class LRUCache:
    #self.hsmap = dict()
    #self.capacity_count = 0
    #self.head = self.tail = None
    
    def __init__(self, cap):
        self.capacity_count = cap
        self.hsmap = dict()
        self.head = self.tail = None

    def get(self, key):
        if self.head is None:
            return -1

    def set(self, key, value):
        if self.capacity == n:
            return -1


for t in range(T):
    s = st_list[t]
    n = N_list[t]

    #lru = LRUCache(3)
    #print(lru.get(5))

    my_queue = doubly_ended_queue()
    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)

    my_queue.print_queue()

    my_queue.push_at_front(4)
    my_queue.push_at_front(5)

    my_queue.print_queue()
    data1 = my_queue.pop_from_end()
    print(data1)
    data1 = my_queue.pop_from_end()
    print(data1)
    
    my_queue.print_queue()
