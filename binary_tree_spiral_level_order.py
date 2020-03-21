INT_MAX=1000000
# hd is a component in the node to capture the horizontal distance
# of the node from the root


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


class Node:
    # fn to initialize the node object
    def __init__(self, data):
        self.data = data
        self.hd = INT_MAX
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

def print_spiral(root):
    itr = False
    h = height(root)
    for i in range(1, h+1):
        print_given_level(root, i, itr)
        itr = not itr

def print_given_level(root, level, itr):
    if(root == None):
        return
    if (level == 1):
        print(root.data, end=" ")
    elif (level > 1):
        if(itr):
            print_given_level(root.left, level - 1, itr)
            print_given_level(root.right, level - 1, itr)
        else:
            print_given_level(root.right, level - 1, itr)
            print_given_level(root.left, level - 1, itr)

def height(node):
    if (node == None):
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if (lheight > rheight):
            return(lheight + 1)
        else:
            return (rheight + 1)
        
# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    print_spiral(bintree.root)
