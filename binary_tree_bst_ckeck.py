INT_MIN = -4294967296
INT_MAX = 4294967296
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

# check if the binary tree is a BST
def is_bst(root):
    return (is_bst_util(root, INT_MIN, INT_MAX))

# returns true if the tree is a bst and its values
# are >= mini and <= maxi
def is_bst_util(root, mini, maxi):
    
    if root is None:
        return True

    # return False if this node violates the min/max constraint
    if root.data < mini or root.data > maxi:
        return False

    # Otherwise check subtrees recursively, tightening
    # the min/max constraint
    return(is_bst_util(root.left, mini, root.data-1) and
            is_bst_util(root.right, root.data+1, maxi))

# another method of checking bst where we
# use two pointers instead of mini and maxi
def isBST(root, l, r):
    if root is None:
        return True

    # if left node exists then check if it's data
    # is less than root
    if l is not None and root.data < l.data:
        return False

    # check similar condition for the right node
    if r is not None and root.data > r.data:
        return False

    # check recursively for every node
    return (isBST(root.left, l, root) and isBST(root.right, root, r))

# another method to check bst: do in-order traversal of tree
# then the nodes should be in ascending order, otherwise not a bas
# or simply we can have a pointer to the previously visited node in
# inorder traversal. if the current node's value is greater than the
# previously visited node, then not a bst
prev = None
def is_bst2(root):
    # prev is the global variable which holds the
    # previously visited node
    global prev

    if root is None:
        return True

    if is_bst2(root.left) is False:
        return False

    # in inrder traversal, left node is visited before current node.
    # at this point left subtree is visited, hence prev holds the
    # previously visited node. We need to check for the constraint
    if prev is not None and prev.data > root.data:
        return False

    # set the prev values
    prev = root
    return is_bst2(root.right)

# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = Node(1)
    bintree.root.left =  Node(2)
    bintree.root.right =  Node(3)
    print(is_bst(bintree.root))
    print(is_bst2(bintree.root))
    print(isBST(bintree.root, None, None))


    bintree1 = binary_tree()
    bintree1.root = Node(4)
    bintree1.root.left =  Node(2)
    bintree1.root.right =  Node(5)
    bintree1.root.left.right =  Node(3)
    bintree1.root.left.left =  Node(1)
    print(is_bst(bintree1.root))
    print(is_bst2(bintree1.root))
    print(isBST(bintree1.root, None, None))
