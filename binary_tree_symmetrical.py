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
#arr=[1, 2, 3, 7, 6, 5, 4]
arr=[1, 2, 3]

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

def check_symmetry(left, right):
    if left is not None and right is None:
        return False
    elif left is None and right is not None:
        return False
    elif left is None and right is None:
        return True
    else:
        if left.data == right.data:
            return check_symmetry(left.right, right.left) and check_symmetry(left.left, right.right)
        else:
            return False


def is_symmetric(root):
    if root is None:
        return True
    else:
        return check_symmetry(root.left, root.right)
# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    bintree.root.left.left = Node(4)
    bintree.root.right.left = Node(5) 
    
    print(is_symmetric(bintree.root))
