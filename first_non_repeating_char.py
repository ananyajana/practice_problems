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

class doubly_linked_list:
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

    def peep(self):
        if self.front is not None:
            return self.front.data
        else:
            return None

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

    def find(self, val):
        if self.front is not None:
            temp = self.front
            # search for the particular value in node or 
            # until the entire list is traversed
            while temp is not None and temp.data != val:
                temp = temp.next
            return temp
        return None
    
    def del_node(self, node):
        if self.front is not None:
            temp = self.front
            while temp is not None and temp != node:
                temp = temp.next
            if temp is not None:
                if temp == self.front:
                    self.front = self.front.next
                    if self.front is not None:
                        self.front.prev = None
                    temp.next = None
                elif temp == self.end:
                    self.end = self.end.prev
                    if self.end is not None:
                        self.end.next = None
                    temp.prev = None
                else:
                    temp.next.prev = temp.prev
                    temp.prev.next = temp.next
                    temp.next = temp.prev = None

           

def first_non_repeating_chars(s, n):
    non_repeated_chars = doubly_linked_list()
    repeated_chars = dict()
    first_nrcs_array = [-1]*n
    s = s.split()

    print(s)
    print('len is :', len(s))
    for i in range(len(s)):
        if s[i] in repeated_chars:
            if non_repeated_chars.is_empty() is True:
                first_nrcs_array[i] = -1
            else:
                first_nrcs_array[i] = non_repeated_chars.peep()
        else:
            node = non_repeated_chars.find(s[i])
            if node is None:
                non_repeated_chars.push(s[i])
                print('i is:', i)
                first_nrcs_array[i] = non_repeated_chars.peep()
            else:
                non_repeated_chars.del_node(node)
                repeated_chars[s[i]] = True
                if non_repeated_chars.is_empty() is True:
                    first_nrcs_array[i] = -1
                else:
                    first_nrcs_array[i] = non_repeated_chars.peep()
                    
                
    print(first_nrcs_array)
                
    

for t in range(T):
    s = st_list[t]
    n = N_list[t]

    first_non_repeating_chars(s, n)
