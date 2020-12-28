#User function Template for python3

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        self.nextRight = None

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
