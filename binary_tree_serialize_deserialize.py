#User function Template for python3

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def height(node):
    # Base case: Tree is empty
    if node is None:
        return 0

    # If tree is not empty then height = 1 + max of left
    # height and right subtree
    return 1 + max(height(node.left), height(node.right))

# this function stores a tree in a file pointed by fp
'''
MARKER = -1
def serialize(root, fp):
    if root is None:
        fp.write ("%d " % MARKER)
        return

    fp.write("%d " % root.key)
    serialize(root.left, fp)
    serialize(root.right, fp)
    
# this function constructs a tree from a file pointed by 'fp'
def deserialize(root, fp):
    # read next item from file. If there are no more items or next
    # item is marker then return
'''

# serializing function
def serialize(root, s=""):
    if root is None:
        s += "# "
        return s
    
    s += (str(root.data)+" ")
    s = serialize(root.left, s=s)
    s = serialize(root.right, s=s)
    return s
        
# deserializing function
i = 0

def deserialize(s):
    global i
    if s[i] == '#':
        # cheking if i is not pointing to the last marker that is at eht
        # end of the string, then the next character needs to be checked
        # else not
        if (i < len(s) - 2):
            i += 2
        return None
    else:
        space = s[i:].find(" ")
        sp = space + i
        root = Node(s[i:sp])
        i = sp + 1
        root.left = deserialize(s)
        root.right = deserialize(s)
        return root

def preorder(root):
    if root is None:
        print('# ')
        return None
    else:
        print('%d ' % root.data)
        preorder(root.left)
        preorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
serial = serialize(root)
print("The tree serialized: - ", serial)
root1 = None
root1 = deserialize(serial)
print('the original tree is: ', preorder(root))
print('the deserialized tree is: ', preorder(root))
