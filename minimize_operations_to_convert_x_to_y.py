# find minimum number of operations needed to obtain N, only two operations are
# available (1) multiplication with 2, (2) subtraction with 1

''' the idea is to list all possible ways in which a number can be 
obtained using the two operations and then find the shortest path
i.e. breadth first traversal'''
import queue

# A node of BFS traversal
class node:
    def __init__(self, val, level):
        self.val = val
        self.level = level

# Returns minimum number of oeratons needed to obtain n or 
# another way of saying, minimum number of operations needed
# to convert x into y

# that is why this is an example of dynamic programming,
# because  we are enumerating all possible ways and then
# finding the best. The problem has a n optimal substructure
# and repeated calculations
# we can pass(n, 0)
def min_operations(x, y):
    # To keep track of visited numbers in BFS
    visit = set()
    
    # create a queue and enqueue x into it, in our case we can insert n
    q = queue.Queue()    
    n = node(x, 0)
    q.put(n)

    #Do BFS starting from 0
    while not q.empty():
        # Remove an item from queueu
        t = q.get()

        # If the number removed is target number n, return its level
        if t.val == y:
            return t.level

        # Mark dequeued number as visited
        visit.add(t.val)

        # if we can reach y in one more step
        if t.val * 2 == y or t.val - 1 == y:
            return t.level + 1

        # Isert the children of t if not visited already
        if t.val * 2 not in visit:
            n.val = t.val * 2
            n.level = t.level + 1
            q.put(n)
        if t.val - 1 >= 0 and t.val - 1 not in visit:
            n.val = t.val - 1
            n.level = t.level + 1
            q.put(n)

# driver code
x = 4
y = 7
print(min_operations(x, y))
