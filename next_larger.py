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
    #print('in next_larger')
    s = s.split()
    #my_stack = stack()
    #nl = []
    str = None
    for i in range(n):
        flag = 0
        # check for the next larger number in the index range i+1 to n
        for j in range(i, n):
            #print('s[{}] {}, s[{}] {}'.format(i, s[i], j, s[j]))
            if int(s[j]) > int(s[i]):
                if str is None:
                    str = s[j] + ' '
                else:
                    str = str + s[j] + ' '
                #nl.append(int(s[j]))
                #print(s[j])
                #print('pushing {} for {}'.format(s[j], s[i]))
                #my_stack.push(s[j])
                flag = 1 # flag the the next larger number is found
                break
        # if the next larger number has not been found
        if flag == 0:
            if str is None:
                str = '-1 '
            else:
                str = str + '-1 '
            #nl.append(-1)
            #print(int(-1))
            #my_stack.push(-1)
            #print('pushing {} for {}'.format(-1, s[i]))
    #print(nl)
    print(str)


for t in range(T):
    s = st_list[t]
    n = N_list[t]
    next_larger(s, n)
