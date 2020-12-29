#User function Template for python3

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        self.nextRight = None

def height(node):
    # Base case: Tree is empty
    if node is None:
        return 0

    # If tree is not empty then height = 1 + max of left
    # height and right subtree
    return 1 + max(height(node.left), height(node.right))

# Function to get the diameter of a binary tree
def diameter(root):
    # base case when tree is empty
    if root is None:
        return 0

    # get the height of the left and right subtrees
    lheight = height(root.left)
    rheight = height(root.right)

    # get the diameter of left and right sub-trees
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    # return the max of the following tree:
    # 1) diameter of left subtree
    # 2) diameter of right subtree
    # 3) height of left subtree + height of right subtree + 1
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

def connect(root):
    if root is None:
        return

    queue = []
    d = 0
    queue.append((root, d))
    
    while len(queue)> 0:
        node, d1 = queue.pop(0)
        print('data: ', node.data)
        print('level', d1)
        if len(queue) > 0:
            node2, d2 = queue[0]
            if d1 == d2:
                node.nextRight = node2

        # Enqueue left child
        if node.left is not None:
            queue.append((node.left, d1 + 1))

        # Enqueue right child
        if node.right is not None:
            queue.append((node.right, d1 + 1))
        if node.nextRight is not None:
            print('next right is', node.nextRight.data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of the binary tree: - ")
connect(root)
print('Diameter of the tree: ', diameter(root))
