INT_MAX=1000000


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

# global array to hold the indices of the recently visited nodes
# at a particular level represented by indices
a = [None]*100

def connect_nodes_utils(p):
    global a
    # the following step might be redundant as a is already initialized
    # but in cases where connect_nodes_utils is called multiple times,
    # the array a is reused and hence it might be necessary to reinitialize
    for i in range(100):
        a[i] = None

    connect_nodes(p, 0)


# function to connect nodes using preorder
# traversal
def connect_nodes(p, l):
    if p is None:
        return

    # assigning left neighbor
    p.next_right = a[l]

    # updating value of the recent
    # node at level
    a[l] = p
    connect_nodes(p.right, l+1)
    connect_nodes(p.left, l+1)
    
# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    connect_nodes_utils(bintree.root)
    print(bintree.root.left.right.next_right.data)

