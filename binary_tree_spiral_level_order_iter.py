INT_MAX=1000000
# hd is a component in the node to capture the horizontal distance
# of the node from the root

class stack_Node:
    # fn to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.front = None

    # method to add an item to the queue
    def push(self, item):
        node = stack_Node(item)
        if self.front is not None:
            node.next = self.front
        self.front = node
    
    # method to remove an item from the queue
    def pop(self):
        if self.front is None:
            return -1
        else:
            temp = self.front
            self.front = self.front.next
            return temp.data
    
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
    if root == None:
        return

    # create two stacks to store
    # alternative levels
    s1 = [] # for levels to be printed from right to left
    s2 = [] # for levels to be printed from left to right

    # append first level to first stack 's1'
    s1.append(root)

    # keep printing while any of the
    # stacks has some nodes
    while not len(s1) == 0 or not len(s2) == 0:
        # print nodes of the current level from s1
        # and append nodes of the next level to s2
        while not len(s1) == 0:
            temp = s1[-1]
            s1.pop()
            print(temp.data, end='')        

            # Note that right is appended before left
            if temp.right:
                s2.append(temp.right)
            if temp.left:
                s2.append(temp.left)

        # print nodes of the current level from s2
        # and append nodes of the next level to s1
        while not len(s2) == 0:
            temp = s2[-1]
            s2.pop()
            print(temp.data, end='')        
            # Note that right is appended before left
            if temp.left:
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)

# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    print_spiral(bintree.root)
