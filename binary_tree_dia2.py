#User function Template for python3

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        self.nextRight = None

class Height:
    def __init(self):
        self.h = 0


def diameterOpt(root, height):

    # to store the height of the left and right subtree
    lh = Height()
    rh = Height()

    # base condition - when binary tree is empty
    if root is None:
        height.h = 0
        return 0

    # ldiameter --> diameter of left subtree
    # rdiameter --> diameter of right subtree

    # height of left subtree and right subtree is obtained from lh and rh
    # and returned value of function is stored in ldiameter and rdiameter

    ldiameter = diameterOpt(root.left, lh)
    rdiameter = diameterOpt(root.right, rh)

    # height of tree will be max of left subtree
    # height of right subtree height plus 1

    height.h = max(lh.h, rh.h) + 1

    # return maximum of the following
    # 1) left diameter
    # 2) right diameter
    # 3) left height + right height + 1
    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))


# function to calculate diameter of binary tree
def diameter(root):
    height = Height()
    return diameterOpt(root, height)


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
