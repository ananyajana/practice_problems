# problems from geeksforgeeks must do coding questions

T = int(input())
st_list =[]
N_list = []
for t in range(T):
    N_list.append(input())
    st_list.append(input())

class Node:
    # fn to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
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
    
    # method to remove an item from the queue
    def pop(self):
        if self.front is None:
            return -1
        else:
            temp = self.front
            self.front = self.front.next
            return temp.data
    
    def is_empty(self):
        if self.front is None:
            return True
        return False


def rot_oranges(s, n):
    # split the string to extract the individual characters
    n = n.split()
    # convert the characters to int
    for i in range(len(n)):
        n[i] = int(n[i])

    # convert the string containing the elements of the matrix
    s = s.split()

    # mat is the matrix that contains the elements
    mat = []
    r = n[0]
    c = n[1]
    # initialize the matrix with the elements
    mat = [ s[i*c : (i+1)*c] for i in range(r)]
    print(mat)

    # create a queue to hold the rotten oranges
    # every time we dequeue we rotten orange, we
    # rot the fresh oranges(top, down, left, right)
    # around it and then enqueue the newly rotten oranges
    # with timestamp = current rotten oranges timestamp + 1
    # this algorithm is somewhat similar to breadth first search
    # and connected component analysis
    my_queue = Queue()
    for i in range(r):
        for j in range(c):
            if mat[i][j] == '2':
                my_queue.push((i, j, 0))

    # all the rotten oranges have been enqueued
    # start dequeueing and rotting other oranges
    # the order of rotting does not matte
    while my_queue.is_empty() is False:
        # cur_i, cur_j and cur_time are the i, j index
        # of the cell the current rotten orange is in the
        # matrix mat and its timestamp 
        cur_i, cur_j, cur_time = my_queue.pop()
        
                
            
    return -1

for t in range(T):
    s1 = st_list[t]
    n = N_list[t]
    print(n)
    print(s1)
    
    print(rot_oranges(s1, n))
