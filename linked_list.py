class Node:
    # fn to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

#linked list contains a node object
class linked_list:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

# code execution starts here
if __name__=='__main__':
    # start with the empty list
    llist = linked_list()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    # three nodes have been created. We gave references to these blocks
    # as head, second and third
    
    llist.head.next = second
    second.next = third

    llist.print_list()
