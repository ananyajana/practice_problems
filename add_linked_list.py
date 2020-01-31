# problems from geeksforgeeks must do coding questions

T = int(input())
N1_list = []
st1_list = []
N2_list = []
st2_list = []
for t in range(T):
    N1_list.append(int(input()))
    st1_list.append(input())
    N2_list.append(int(input()))
    st2_list.append(input())

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
    def reverse_list(self):
            if self.head is None:
                return None
            cur = new_head = self.head
            temp = None
            temp2 = cur.next
            cur.next = temp
            temp = cur
            new_head = cur
            cur = temp2
            while(cur):
                temp2 = cur.next
                cur.next = temp
                temp = cur
                new_head = cur
                cur = temp2

            self.head = new_head


def create_linked_list(s, n):
    data_list = []
    data_list = s.split()
    #print(data_list)
    #print(s)
    llist = linked_list()
    first = Node(int(data_list[0]))
    llist.head = new_node = first
    #new_node = new_node.next
    for i in range(1, n):
        new_node.next = Node(int(data_list[i]))
        new_node = new_node.next

    #llist.print_list()
    return llist

def add_numbers(head_a, head_b):

    if head_a is None:
        return head_b
    if head_b is None:
        return head_a
    carry = 0
    temp1 = head_a
    temp2 = head_b

    result = linked_list()
    temp = result.head
    flag = 0
    
    prev = None

    # if the number is 123 it is represented as 3->2->1
    # while both the lists are not empty
    while temp1 is not None and temp2 is not None:
        # add the current digits and the carry
        res_sum = temp1.data + temp2.data + carry
        # if the result is > 9 then carry needs to be set
        if res_sum > 9:
            carry = 1
            res_sum = res_sum - 10
        else:
            carry = 0
        temp = Node(res_sum)
        if prev is not None:
            prev.next = temp
        if flag is 0:
            result.head = temp
            flag = 1

        prev = temp
        temp = temp.next
        temp1 = temp1.next
        temp2 = temp2.next

    while temp1 is not None:
        res_sum = temp1.data + carry
        # if the result is > 9 then carry needs to be set
        if res_sum > 9:
            carry = 1
            res_sum = res_sum - 10
        else:
            carry = 0
        temp = Node(res_sum)
        if prev is not None:
            prev.next = temp
        prev = temp
        temp = temp.next
        temp1 = temp1.next

    while temp2 is not None:
        res_sum = temp2.data + carry
        # if the result is > 9 then carry needs to be set
        if res_sum > 9:
            carry = 1
            res_sum = res_sum - 10
        else:
            carry = 0
        temp = Node(res_sum)
        if prev is not None:
            prev.next = temp
        prev = temp
        temp = temp.next
        temp2 = temp2.next
    # taking care of the last carry after exhausting all digits of the numbers
    if carry is 1:
        temp = Node(carry)
        if prev is not None:
            prev.next = temp
        
    return result


for t in range(T):
    #s1 = input()
    s1 = st1_list[t]
    n1 = N1_list[t]
    llist1 = create_linked_list(s1, n1)
    s2 = st2_list[t]
    n2 = N2_list[t]
    llist2 = create_linked_list(s2, n2)
    #llist1.print_list()
    #llist2.print_list()
    llist1.reverse_list()
    llist2.reverse_list()
    #print('after reversing')
    #llist1.print_list()
    #llist2.print_list()
    new_list = add_numbers(llist1.head, llist2.head)
    new_list.print_list()
