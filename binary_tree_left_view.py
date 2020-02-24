class Node:
    # fn to initialize the node object
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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
def left_view_util(root, level, max_level):
    # base case
    if root is None:
        return

    # if this is the first node of its level
    if max_level[0] < level:
        print('{}\t'.format(root.data))
        max_level[0] = level

    # recur for left first and then right subtree
    # so that the max_level variable gets changed
    # at the first node encountered at level i.e. 
    # the leftmost node
    left_view_util(root.left, level+1, max_level)
    left_view_util(root.right, level+1, max_level)

# a wrapper over left_view
def left_view(root):
    max_level = [0]
    left_view_util(root, 1, max_level)

# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = Node(1)
    bintree.root.left =  Node(2)
    bintree.root.right =  Node(3)
    #bintree.print_tree_inorder(bintree.root)
    left_view(bintree.root)
