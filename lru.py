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
        if self.front is not None:
            temp = self.front
            print('printing from the front')
            while temp.next is not None:
                print(temp.data)
                temp = temp.next
            print(temp.data)

            #temp = self.end
            #print('printing from the back')
            #while temp.prev is not None:
            #    print(temp.data)
            #    temp = temp.prev
            #print(temp.data)
        else:
            print('queue empty')
    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

class LRUCache:
    def __init__(self, cap):
        self.capacity = cap
        self.hsmap = dict()
        self.my_queue = doubly_ended_queue()

    def get(self, key):
        #print('in get')
        #self.my_queue.print_queue()
        #print(self.hsmap)
        if self.my_queue.is_empty() is True:
            return -1
        else:
            # if the key is not in hashmap, it's a cache miss
            if key not in self.hsmap:
                return -1
            # dequeue and enqueue all elements from the queue except the key
            else:
                cnt = 0
                while cnt < self.capacity and self.my_queue.is_empty() is False:
                    rem_val = self.my_queue.pop()
                    if rem_val != key:
                        self.my_queue.push(rem_val)
                    cnt += 1
                self.my_queue.push(key)
                return self.hsmap[key]

    def set(self, key, value):
        #print('in set')
        #self.my_queue.print_queue()
        #print(self.hsmap)
        # if key is not in hash map, then cache size should be checked, if cache size has
        # not reached its max capacity, then add the element to the end
        # of the queue, if max capacity is reached, then dequeue from the
        # front and then enqueue
        if key not in self.hsmap:
            # if we are here, it's a new key, we need to check if current capacity is not
            # full, then just enqueue that new key
            # else, dequeue a value from the queue and then enqueue the new key
            if len(self.hsmap) == self.capacity:
                rem_val = self.my_queue.pop()
                del self.hsmap[rem_val]
            self.my_queue.push(key)
            self.hsmap[key] = value
        else:
            while my_queue.is_empty() is False:
                rem_val = my_queue.pop()
                if rem_val != key:
                    self.my_queue.push(rem_val)
            self.my_queue.push(key)
            self.hsmap[key] = value
            return self.hsmap[key]


for t in range(T):
    s = st_list[t]
    n = N_list[t]
    
    # create an instance of the class lru cache
    lru = LRUCache(3)

    #page_refs = [1, 2, 3]
    page_refs = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    for i in range(len(page_refs)):
        if lru.get(page_refs[i]) == -1:
            print('cache miss :', page_refs[i])
            lru.set(page_refs[i], page_refs[i]  + 10)
        else:
            print('cache hit :', page_refs[i])

'''
    # testing doubly ended queue functionality
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
    data1 = my_queue.pop_from_end()
    print(data1)
    data1 = my_queue.pop_from_end()
    print(data1)
    my_queue.print_queue()
    data1 = my_queue.pop_from_end()
    print(data1)
    my_queue.print_queue()
'''
