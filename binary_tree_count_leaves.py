#User function Template for python3

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def height(node):
    # Base case: Tree is empty
    if node is None:
        return 0

    # If tree is not empty then height = 1 + max of left
    # height and right subtree
    return 1 + max(height(node.left), height(node.right))


def countLeaves(root):
    if root is None:
        return 0
    elif root.right is None and root.left is None:
        return 1
    else:
        return countLeaves(root.left) + countLeaves(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('Leaves in the tree: ', countLeaves(root))

