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

def print_level_order(root):
    h = height(root)
    for i in range(1, h+1):
        print_given_level(root, i)

def print_given_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data)
    else:
        # if the level is not 0, then proceed to the level
        # number by making one step at a time
        print_given_level(root.left, level-1)
        print_given_level(root.right, level-1)


def height(root):
    if root is None:
        return 0
    else:
        # compute the height of both subtrees and take the maximum
        lheight = height(root.left)
        rheight = height(root.right)

        # use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = Node(1)
    bintree.root.left =  Node(2)
    bintree.root.right =  Node(3)
    bintree.root.left.left =  Node(4)
    bintree.root.left.right =  Node(5)
    #bintree.print_tree_inorder(bintree.root)
    print_level_order(bintree.root)
