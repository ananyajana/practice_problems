#import operator
#from collections import OrderedDict

T = int(input())

# check the uncomon charasters in two arrays
# if there is match for the character in the other array, then
# the value is -1, else the value corresponding to the keys is 1

def uncommon(arr1, arr2):
    #temp = OrderedDict()
    temp = dict()
    for i in range(len(arr1)):
        temp[arr1[i]] = 1 # common element in second array is not yet found
    for j in range(len(arr2)):
        if arr2[j] in temp.keys():
            temp[arr2[j]] = -1  # common element in second array is found
        else:
            temp[arr2[j]] = 1 # common element was not found in the first array
 
    print(sorted(temp))
    print('list form: ', list(sorted(temp.items())))

    str1 = ''
    for key in sorted(temp.keys()):
        if temp[key] != -1:
            str1 += key

    if not temp:
        return -1
    else:
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

