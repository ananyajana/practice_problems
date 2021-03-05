import operator
from collections import OrderedDict

T = int(input())

# check the uncomon charasters in two arrays
# if there is match for the character in the other array, then
# the value is -1, else the value corresponding to the keys is 1

def uncommon(arr1, arr2):
    temp = OrderedDict()
    for i in range(len(arr1)):
        temp[arr1[i]] = 1 # common element in second array is not yet found
    for j in range(len(arr2)):
        if arr2[j] in temp.keys():
            temp[arr2[j]] = -1  # common element in second array is found
        else:
            temp[arr2[j]] = 1 # common element was not found in the first array
    #temp_copy = temp.copy()
    #temp_copy = {k:v for k, v in temp.items() if v != -1}
    '''
    for key in temp_copy.keys():
        if temp_copy[key] == -1:  # the match is found, we can delete the corresponding key:
            del temp_copy[arr2[j]]
    for k,v in temp_copy.items():
        if v == -1:
           del temp_copy[k]
    '''

    str1 = ''
    #for key in temp_copy.keys():
    #for k,v in temp_copy.items():
    #for k,v in temp.items():
    for key in temp.keys():
        if temp[key] != -1:
            #if v != -1:
            #str1 += k
            str1 += key

    #if not temp_copy:
    if not temp:
        return -1
    else:
        #return temp_copy
        return str1

for t in range(T):
    #n = int(input())
    #arr1 = list(map(int, input().strip().split()))
    arr1 = input()
    #arr2 = list(map(int, input().strip().split()))
    arr2 = input()
    print('arr1: {}, arr2: {}'.format(arr1, arr2))
    val = uncommon(arr1, arr2)
    if val == -1:
        print('equal')
    else:
        print('{} '.format(val))

