# problems from geeksforgeeks must do coding questions

T = int(input())
st_list =[]
for t in range(T):
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

def paren_check(s):
    my_stack = stack()
    word = '{[('
    word2 = '}])'
    for i in range(len(s)):
        #print(s[i])
        if word.find(s[i]) != -1:
            my_stack.push(s[i])
        elif word2.find(s[i]) != -1:
            temp = my_stack.pop()
            if s[i] == ')' and temp != '(':
                return 1
            elif s[i] == '}' and temp != '{':
                return 1
            elif s[i] == ']' and temp != '[':
                return 1
    if my_stack.pop() == -1:
        return 0
    else:
        return 1
    
for t in range(T):
    #print(st_list[t])
    if paren_check(st_list[t]) == 0:
        print('balanced')
    else:
        print('not balanced')
