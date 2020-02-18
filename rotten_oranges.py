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

    def peep(self):
        if self.front is not None:
            return self.front
        else:
            return None

# check if the indices are valid
def is_valid(i, j, r, c):
    if i >= 0 and i < r and j >= 0 and j < c:
        return True
    else:
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
    #print(mat)

    # create a queue to hold the rotten oranges
    # every time we dequeue we rotten orange, we
    # rot the fresh oranges(top, down, left, right)
    # around it and then enqueue the newly rotten oranges
    # with timestamp = current rotten oranges timestamp + 1
    # this algorithm is somewhat similar to breadth first search
    # and connected component analysis
    my_queue = Queue()
    # this delimiter denotes the beginning of a new time frame
    delim = (-1, -1)
    for i in range(r):
        for j in range(c):
            if mat[i][j] == '2':
                my_queue.push((i, j))
    my_queue.push(delim)

    # all the rotten oranges have been enqueued
    # start dequeueing and rotting other oranges
    # the order of rotting does not matte
    
    # this variable contains the minimum time taken to rot all oranges
    ans = 0
    while my_queue.is_empty() is False:
        # check if the current element at the beginning of the queue
        # is a delimiter, if not then start the process of rotting oranges
        item = my_queue.pop()

        # flag to denote the first orange being rotter in 
        # every list in queue(till delim)
        flag = False

        while item != delim and item is not None:
            # i, j are the indices
            # of the cell the current rotten orange is in the
            # matrix mat and its timestamp 
            #item = my_queue.pop()
            #print(item[0])
            #print(item)
            #print(item[1])
            i, j = item[0], item[1]
            
            # the right hand side is a valida cell and the orange
            # in it is fresh
            if is_valid(i+1, j, r, c) and mat[i+1][j] == '1':
                if flag is False:
                    ans += 1
                    flag = True
                mat[i+1][j] = '2'
                my_queue.push((i+1, j))
            # check the left adjacent cell and if that can be rotten
            if is_valid(i-1, j, r, c) and mat[i-1][j] == '1':
                if flag is False:
                    ans += 1
                    flag = True
                mat[i-1][j] = '2'
                my_queue.push((i-1, j))
            # check if the top adjacent cell can be rotten
            if is_valid(i, j+1, r, c) and mat[i][j+1] == '1':
                if flag is False:
                    ans += 1
                    flag = True
                mat[i][j+1] = '2'
                my_queue.push((i, j+1))
            # check if the bottom adjacent cell can be rotten
            if is_valid(i, j-1, r, c) and mat[i][j-1] == '1':
                if flag is False:
                    ans += 1
                    flag = True
                mat[i][j-1] = '2'
                my_queue.push((i, j-1))
            
            item = my_queue.pop()

        # pop the delimiter, there is no need of prcessing this element
        #my_queue.pop()    
        # if all the items have not been processed in the current time frame
        # then add a delimiter to the queue to mark the batch of oranges 
        # processed in the current time frame   
        if my_queue.is_empty() is False:
            my_queue.push(delim)    


    # now we need to check the entire matrix for fresh orang
    # if there is at least one fresh orange which could not be
    # rotten return -1 else return the time taken to rot all oranges
    #print(mat)
    for i in range(r):
        for j in range(c):
            if mat[i][j] == '1':
                #print('returning -1')
                return -1

    #print('returning ans')
    return ans

for t in range(T):
    s1 = st_list[t]
    n = N_list[t]
    #print(n)
    #print(s1)
    
    print(rot_oranges(s1, n))
