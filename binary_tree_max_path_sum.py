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
#arr=[1, 2, 3, 7, 6, 5, 4]
arr = [-9, 6, -10]

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

# assumes all numbers are non-negative
def max_path_sum(root):
    _, max_sum = find_path_len(root)
    return max_sum
INT_MIN = -2**32
def find_path_len(root):
    if root is None:
        return [0, 0]
    if root.left is None and root.right is None:
        return [root.data, INT_MIN]

    left_path_len, left_max_sum = find_path_len(root.left)
    right_path_len, right_max_sum = find_path_len(root.right)
    node_max_sum = INT_MIN
    max_path_len = INT_MIN


    if root.left is not None and root.right is not None:
        if left_path_len >= right_path_len:
            max_path_len = left_path_len + root.data
        else:
            max_path_len = right_path_len + root.data
        node_max_sum = left_path_len + root.data + right_path_len
        cur_max = left_max_sum if left_max_sum > right_max_sum else right_max_sum
        if node_max_sum < cur_max:
            node_max_sum = cur_max

    if root.left is None:
        max_path_len = right_path_len + root.data
        node_max_sum = root.data + right_path_len
    elif root.right is None:
        max_path_len = left_path_len + root.data
        node_max_sum = left_path_len + root.data 
    #cur_max = left_max_sum > right_max_sum? left_max_sum:right_max_sum

    return [max_path_len, node_max_sum]

# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    print(max_path_sum(bintree.root))
