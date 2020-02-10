# problems from geeksforgeeks must do coding questions

T = int(input())
st_list =[]
N_list = []
for t in range(T):
    N_list.append(int(input()))
    st_list.append(input())

# the stack can have another array/linked list of minimum element
# seen at every step
class Node:
    # fn to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.front = None
        self.min = None

    # method to add an item to the queue
    def push(self, item):
        if self.min > item:
            # set the current minimum if the current item value is less
            self.min = item
            item = 2 * item - self.min
            #print('current self.min :', self.min)
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
    def get_min(self):
        return self.min
        

for t in range(T):
    s = st_list[t]
    n = N_list[t]
    my_stack = stack()
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(5)
    my_stack.push(4)
    my_stack.push(1)

    print('min in stack :', my_stack.get_min())
    my_stack.pop()
    print('min in stack :', my_stack.get_min())
    my_stack.pop()
    print('min in stack :', my_stack.get_min())
    my_stack.pop()
    print('min in stack :', my_stack.get_min())
    my_stack.pop()
    print('min in stack :', my_stack.get_min())
    my_stack.pop()
