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

arr=[20, 8, 22, 5, 3, 4, 25]

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
        

def find_data(root, data):
    if root is None:
        return None
    if root.data == data:
        return root
    else:
        # try to find the node in the left subtree, if not present
        # try to find it in right subtree
        left = find_data(root.left, data)
        if left is None:
            return find_data(root.right, data)
        else:
            return left

from collections import defaultdict

# method to print the bottom view        
def vertical_traversal(root):
    if root is None:
        return

    # initialize a variable 'hd' with 0
    # for the root element
    hd = 0

    # dictionary to store key value pair
    new_dict = defaultdict(list)

    # set the horizontal distance of root from root
    root.hd = 0

    # create a queue to store the tree nodes in level order traversal
   
    my_queue = MyQueue()
    my_queue.push(root)

    # while the queue is not empty(standard level order loop)
    while my_queue.is_empty() is False:
        temp = my_queue.pop()
        
        # extract the horizontal distance value from the dequeued tree node
        hd = temp.hd
        
        # put the dequeued node in dictionary with
        # key as the horizontal distance and the data
        # in the tree node as the value in dictionary
        new_dict[hd].append(temp.data)

        # if the dequeued node has a left child
        # add it to the queue with the horizontal distance as hd-1

        if temp.left is not None:
            temp.left.hd = hd - 1
            my_queue.push(temp.left)

        # if the dequeued node is a right node
        # then enqueue it with the horizontal distance as hd+1
        if temp.right is not None:
            temp.right.hd = hd + 1
            my_queue.push(temp.right)

    # now the dictionary needs to be printed out in sorted order of hd
    #print(new_dict)
    #print('after sorting')
    #new_dict_sorted = {k: v for k, v in sorted(new_dict.items(), key = lambda item: item[1])}
    #print(new_dict_sorted)

    for key in sorted(new_dict.keys()):
        for i in range(len(new_dict[key])):
            print('{} '.format(new_dict[key][i]), end=" ")
    print('\n')
    

def print_vertical_view_util(root, curr, hd, new_dict):
    if root is None:
        return

    # if the node for a particular horizontal distance is not
    # present in dictionary , then add it
    new_dict[hd].append([root.data, curr])

    # recurse into the left subtree
    print_vertical_view_util(root.left, curr+1, hd-1, new_dict)

    # recurse into the right subtree
    print_vertical_view_util(root.right, curr+1, hd+1, new_dict)

def vertical_view2(root):
    # the map will have the horizontal distance as the key and
    # the node' data and height tuple as value
    new_dict = defaultdict(list)
    # util to fill the map with the entries
    print_vertical_view_util(root, 0, 0, new_dict)

    for key in sorted(new_dict.keys()):
        for i in range(len(new_dict[key])):
            print('{} '.format(new_dict[key][i][0]), end='')
    #print('\n')


# code execution starts here
if __name__=='__main__':
    # start with the empty list
    bintree = binary_tree()
    bintree.root = create_binary_tree(0)
    #bintree.print_tree_inorder(bintree.root)

    # find the node with data 3 and insert 10 as a left child
    node1 = find_data(bintree.root, 3)
    #print('the data at the node returned is: ', node1.data)
    node1.left = Node(10)
    node1.right = Node(14)

    # find the node with data 4 and insert data 14 as its right child
    #node1 = find_data(bintree.root, 4)
    #print('the data at the node returned is: ', node1.data)
    #node1.right = Node(14)

    #print('the tree after inserting the nodes :')
    #bintree.print_tree_inorder(bintree.root)

    #bottom_view(bintree.root)
    #vertical_traversal(bintree.root)
    vertical_view2(bintree.root)
