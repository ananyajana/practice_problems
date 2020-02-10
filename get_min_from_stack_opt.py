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
    # whenenever an item < self.min in encountered, the
    # actual pushed element is 2*item - self.min instead of
    # the item and self.min is set to item.
    # it is guaranteed that 2*item  - self.min < item 
    # so now there is a scenario where the element sitting in stack is
    # less than self.min because the actual item has not been pushed,
    # rather is modified version involving the previous self.min is
    # pushed. so that the previous self.min can be retrieved
    def push(self, item):
        if self.min is None:
            self.min = item
        if self.min > item:
            # set the current minimum if the current item value is less
            temp = item
            item = 2 * item - self.min
            self.min = temp
            #print('current self.min :', self.min)
        node = Node(item)
        if self.front is not None:
            node.next = self.front
        self.front = node
        print('pushed :', item)
        #print('push: min is now :', self.min)


    # method to remove an item from the queue
    # whenever the popped element is less than self.min we have an unusual 
    # situation, we know the item popped is not the actual item but a modified
    # version of it.the previous self.min
    # is retrieved by doing 2*self.min - item and then item is set to self.min
    def pop(self):
        if self.front is None:
            return -1
        else:
            temp = self.front
            self.front = self.front.next
            if temp.data < self.min:
                data = 2 * self.min - temp.data
                popped_data = self.min
                self.min = data
            else:
                popped_data = temp.data
            #print('pop: min is now :', self.min)
            return popped_data

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
    my_stack.push(5)
    my_stack.push(3)
    my_stack.push(4)
    my_stack.push(2)
    my_stack.push(1)

    print(' min in stack :', my_stack.get_min())
    for i in range(5):
        data = my_stack.pop()
        print('popped data is:', data)
        print('min in stack is :', my_stack.get_min())
