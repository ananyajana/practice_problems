INT_MAX=1000000
# hd is a component in the node to capture the horizontal distance
# of the node from the root

    
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
    d = []

    # push root
    d.append(root)

    # Direction 0 shows print right to left
    # and for Direction 1 left to right

    direct = 0

    while len(d) != 0:
        size = len(d)
        
        while (size):
            size -= 1

            # One whole level
            # will be printed in this loop
            if direct == 0:
                temp = d.pop()

                if temp.right:
                    d.insert(0, temp.right)

                if temp.left:
                    d.insert(0, temp.left)

                print(temp.data, end='')
            else:
                temp = d[0]
                d.pop(0)

                if temp.left:
                    d.append(temp.left)

                if temp.right:
                    d.append(temp.right)
                
                print(temp.data, end='') 

            print()

            # change direction
            direct = 1 - direct

# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    print_spiral(bintree.root)
