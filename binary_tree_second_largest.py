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
#arr=[1, 2, 3, 4, 5, 6, 7]
#arr=[4, 2, 6, 1, 3, 5, 7]
arr=[4, 2, 6, 1, 3, 5]

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


def find_second_largest(root):
    if root is None:
        return

    # traverse to the right subtree as far as possible
    # prev stores the last node from which we traversed
    temp = root.right
    prev = None
    while temp.right is not None:
        prev = temp
        temp = temp.right

    # The current node does not have a right child.
    # If it doesn't have a left child as well, then
    # prev contains the second largest element.
    if temp.left is None:
        return prev
    else:
        temp = temp.left
        # traverse the right subtree of the left child as far as possible
        while temp.right is not None:
            temp = temp.right

        return temp
# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    print('find_second_largest %d'%(find_second_largest(bintree.root).data))

