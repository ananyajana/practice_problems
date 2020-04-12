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

def is_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is not None and root2 is not None:
        if root1.data == root2.data:
            if is_identical(root1.left, root2.left) is True:
                return is_identical(root1.right, root2.right)
            else:
                return False
        else:
            return False
    else:
        return False

# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    bintree2 = binary_tree()
    bintree2.root = None
    print(is_identical(bintree.root, bintree2.root))
