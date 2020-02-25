class Node:
    # fn to initialize the node object
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class QueueNode:
    # fn to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.front = None

    # method to add an item to the queue
    def push(self, item):
        node = QueueNode(item)
        if self.front is None:
            self.front = node
        else:
            temp = self.front
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    # method to remove an item from the queue
    def pop(self):
        if self.front is None:
            return -1
        else:
            temp = self.front
            self.front = self.front.next
            return temp.data

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

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
    if root is None:
        return
    # create an empty queue for ;eve; order traversal
    my_queue = MyQueue()

    # enqueue the queue and initialize the height
    my_queue.push(root)

    while my_queue.is_empty() is False:
        node = my_queue.pop()
        print(node.data)

        # enqueue left child
        if node.left is not None:
            my_queue.push(node.left)

        # enqueue right child
        if node.right is not None:
            my_queue.push(node.right)

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
