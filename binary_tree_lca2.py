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


def find_lca(root, n1, n2):
    # Base case
    if root is None:
        return None

    # If either n1 or n2 matches with root's key, report
    # the presence by returning root
    if root.data == n1 or root.data == n2:
        return root


    # look for the keys in the left and right subtrees
    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)

    # if both the above calls return non-null, then one
    # key is present in one subtree and the other in the
    # other subtree
    if left_lca and right_lca:
        return root


    # Otherwise check if left subtree or right subtree
    # is lca
    return left_lca if left_lca is not None else right_lca

# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    print('LCA(4, 5) = %d'%(find_lca(bintree.root, 4, 5).data))

