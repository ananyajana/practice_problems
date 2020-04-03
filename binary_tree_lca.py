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

def find_path(root, path, k):
    # base case
    if root is None:
        return False

    # store this node is path vector. The node
    # will be removed if not in path from root to k
    path.append(root.data) 

    # see if the k is the same as root's key
    if root.data == k:
        return True

    # check if k is found in left to right sub-tree
    if (( root.left != None and find_path(root.left, path, k)) or
    (root.right != None and find_path(root.right, path, k))):
        return True

    # if not present in subtree rooted with root, remove
    # root from path and return False
    path.pop()
    return False

def find_lca(root, n1, n2):
    # to store paths to n1 and n2 from the root
    path1 = []
    path2 = []

    # Find paths from root to n1 and root to n2
    # If either n1 and n2 is not present, return -1
    if (not find_path(root, path1, n1) or not find_path(root, path2, n2)):
        return -1

    # compare the paths to get the first different value
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1

    return path1[i-1]

# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    print('LCA(4, 5) = %d'%(find_lca(bintree.root, 4, 7,)))

