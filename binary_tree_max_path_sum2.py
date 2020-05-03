INT_MIN = -2**32
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

def max_path_sum_util(root, res):
    #base case
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.data

    # find the maximum sum in left and right subtree. Also
    # find the maximum root to leaf sums in left and right
    # subtrees and store them in ls and rs
    ls = max_path_sum_util(root.left, res)
    rs = max_path_sum_util(root.right, res)

    # if both left and right children exist
    if root.left is not None and root.right is not None:
        # update result if needed
        res[0] = max(res[0], ls + rs + root.data)

        # return maximum possible value for root being
        # on one side
        return max(ls, rs) + root.data

    # if any of the two children is empty, return
    # root sume for root being on one side
    if root.left is None:
        return rs + root.data
    else:
        return ls + root.data

# The main function which returns sum of the maximum
# sum path between two leaves
def max_path_sum(root):
    res = [INT_MIN]
    max_path_sum_util(root, res)
    return res[0]

# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    print(max_path_sum(bintree.root))
