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
def connect(p):
    temp = None

    if not p:
        return

    # set next_right for root
    p.next_right = None

    # set next_right of all levels one by one
    while p is not None:
        q = p

        # connect all children nodees of p and 
        # children nodes of all other nodes
        # at the same level as p
        while q is not None:
            # set the next_right pointer for p's left child
            if q.left:
                # If q has right child, then right
                # child is next_right of p and we
                # also need to set next_right of
                # right child
                if q.right:
                    q.left.next_right = q.right
                else:
                    q.left.next_right = get_next_right(q)
            if q.right:
                q.right.next_right = get_next_right(q)
            # Set next_right for other nodes in preorder(?) fashion
            q = q.next_right
        if p.left:
            p = p.left
        elif p.right:
            p = p.right
        else:
            p = get_next_right(p)


def get_next_right(p):
    temp = p.next_right
    # traverse nodes as p's level and find
    # and return the first node's first child
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
    connect(bintree.root)
    print(bintree.root.left.right.next_right.data)

