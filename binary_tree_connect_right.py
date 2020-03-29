INT_MAX=1000000
# hd is a component in the node to capture the horizontal distance
# of the node from the root


class QueueNode:
    # fn to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.front = None

    # method to add an item to the queue
    def push(self, item):
        node = QueueNode(item)
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
        else:
            return False


class Node:
    # fn to initialize the node object
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next_right = None

#linked list contains a node object
class binary_tree:
    def __init__(self):
        self.root = None
    
    def print_tree_inorder(self, root):
        if(root):
            self.print_tree_inorder(root.left)
            print(root.data)
            self.print_tree_inorder(root.right)
# recursive function to print the left view of a binary tree

#arr=[20, 8, 22, 5, 3, 4, 25]
arr=[1, 2, 3, 7, 6, 5, 4]

# create a tree with the array from the given index
# i.e. create a tree with the elements arr[i:n]
def create_binary_tree(i):
    global arr
    if i >= len(arr):
        return None
    else:
        root = Node(arr[i])
        root.left = create_binary_tree(2*i + 1)
        root.right = create_binary_tree(2*i + 2)
        return root

# set next right of all descendants of p. This function makes sure
# that all the next right nodes at level i are set before the nodes
# at level i+1
def connect_recur(p):
    if p is None:
        return

    # before setting next_right of left and right children, set next_right
# of children of other nodes at the same level because we can access
# children of other nodes using p's next_right only
    if p.next_right is not None:
        connect_recur(p.next_right)

    # set the next_right pointer for p's left child
    if p.left:
        if p.right:
            p.left.next_right = p.right
            p.right.next_right = get_next_right(p)
        else:
            p.left.next_right = get_next_right(p)
        # recursively call for the next level of nodes
        # starting from the left child. Note that we call
        # only for the left child. The call for the right
        # child will be made in the call for the right child
        connect_recur(p.left)
    elif p.right:
        p.right.next_right = get_next_right(p)
        connect_recur(p.right)
    else:
        connect_recur(get_next_right(p))

# this function returns the leftmost child of nodes at the same
# level as p. This function is used to get_next right of p's right
# child. If right child of p is NULL then this can also be used for
# the left child
def get_next_right(p):
    temp = p.next_right

    # traverse nodes at p's level and find and return
    # the first node's first child

    while temp is not None:
        if temp.left is not None:
            return temp.left
        if temp.right is not None:
            return temp.right
        temp = temp.next_right
    return None

# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    connect_recur(bintree.root)
    #print(bintree.root.left.right.next_right.data)

