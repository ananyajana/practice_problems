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

class Height:
    def __init(self):
        self.h = 0


def isBalancedOpt(root, height):
    rh = Height()
    lh = Height()

    if root is None:
        height.h = 0
        return True
    leftbalance = isBalancedOpt(root.left, lh)
    rightbalance = isBalancedOpt(root.right, rh)

    height.h = max(lh.h, rh.h) + 1

    if leftbalance is True and rightbalance is True and abs(lh.h - rh.h) <= 1:
        return True
    else:
        return False

def isBalanced(root):
    height = Height()
    return isBalancedOpt(root, height)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Is the tree balanced?: - ", isBalanced(root))
