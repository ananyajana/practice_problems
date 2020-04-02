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

# sets the next right of root and calls
# connectRecur() for other methods
def connect(p):
    # set the next right of root
    p.next_right = None

    # set the next right for the rest of
    # the nodes (other than root)
    connect_recur(p)

# set the next right of all descendants of p.
# Assumption: p is a complete binary tree
def connect_recur(p):
    if p is None:
        return

    # set the next_right pointer for p's left child
    if p.left:
        p.left.next_right = p.right

    # set the next right pointer for p's right
    # child p.next_right will be None if p is
    # the right most child at its level
    if p.right:
        if p.next_right:
            p.right.next_right = p.next_right.left
        else:
            p.right.next_right = None
 
    # set the next_right for other nodes in pre order fashion
    connect_recur(p.left)
    connect_recur(p.right)

if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    connect(bintree.root)
    print(bintree.root.left.right.next_right.data)

