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

def bin_tree_to_dll_util(root):
    if root is None:
        return root

    # convert the left subtree and link to the root
    if root.left:
        # convert the left subtree
        left = bin_tree_to_dll_util(root.left)

        # find the inorder predecessor, after
        # this loop, left will point to the
        # inorder predecessor of root. We can
        # traverse till the end using right pointer
        # now because this tree pointers have been
        # already set to be a doubly linked list
        # to the same thing before the call to
        # bin_tree_to_dll, we would need to 
        # traverse to the rightmost node in the
        # left subtree
        while left.right:
            left = left.right

        # make the root as the next of predecessor
        left.right = root

        # make the predecessor as previous of root
        root.left = left
 
    # convert the right subtree and link to the root
    if root.right:
        # convert the right subtree
        right =  bin_tree_to_dll_util(root.right)

        # find the inorder successor, after
        # this loop, right will point to the
        # inorder successor of the root. If we
        # try to set it before making the right
        # subtree as DLL we would need to find
        # leftmost node in the right subtree
        while right.left:
            right = right.left

        # make root as predecessor of the successor
        right.left = root

        # make the root's successor as the next of root
        root.right = right

    return root

def bin_tree_to_dll(root):
    if root is None:
        return root

    # Convert to doubly linked
    # list using bin_tree_to_dll_util
    root = bin_tree_to_dll_util(root)

    # we need pointer to the left most
    # node which is the head of the
    # constructed Doubly Linked List
    while root.left:
        root = root.left

    return root

def print_list(head):
    if head is None:
        return
    while head:
        print(head.data, end=" ")
        head = head.right


# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    bintree.root = bin_tree_to_dll(bintree.root)
    print_list(bintree.root)
