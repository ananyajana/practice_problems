from collections import OrderedDict

T = int(input())

def common_elems(v1, n, v2, m):
    # we need a hash map of size max(m, n)
    #temp = OrderedDict()
    # we store the count of the elements in the hashmap from both the lists
    # v1 and v2
    temp = dict()
    for i in range(n):
        if v1[i] in temp.keys():
            temp[v1[i]] += 1
        else:
            temp[v1[i]] = 1
    
    for i in range(m):
        if v2[i] in temp.keys():
            temp[v2[i]] += 1
        else:
            temp[v2[i]] = 1

    # if the count of an element is 1, it is not common as it is present only
    # in one of the lists
    # if the count of an elements is >= 2 then it is a commoon element
    # at this stage we use an orderedict because we want the common elements
    # in sorted order
    temp_ordered = OrderedDict(sorted(temp.items()))
    common_list = [] # list to hold the common elements
    for key, value in temp_ordered.items():
        value -= 1
        while (value != 0):
            common_list.append(key)
            value -= 1
    return common_list


for t in range(T):
    n = int(input())
    v1 = list(map(int, input().strip().split()))
    m = int(input())
    v2 = list(map(int, input().strip().split()))
    print('max_len is :', common_elems(v1, n, v2, m))


