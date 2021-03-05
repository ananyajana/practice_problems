#import operator
#from collections import OrderedDict

T = int(input())

# check the uncomon charasters in two arrays
# if there is match for the character in the other array, then
# the value is -1, else the value corresponding to the keys is 1 or 2
# depending on which array it was present

def uncommon(arr1, arr2):
    #temp = OrderedDict()
    temp = dict()
    for i in range(len(arr1)):
        temp[arr1[i]] = 1 # common element in second array is not yet found
    # this part does not handle the case where multiple instances of the same char is present
    # in the arr
    for j in range(len(arr2)):
        # the second condition below is to take care of the fact
        # that a character can appear multiple times in an array
        # we say a match only when two occurrences of the same char
        # aqre present in two different arrays. The second condition
        # takes care of the fact only the first time a number is
        # encountered in the second array after being encountered in first array
        # its value would be -1 in dictionary
        if arr2[j] in temp.keys() and temp[arr2[j]] != 2:
            temp[arr2[j]] = -1  # common element in second array is found
        else:
            temp[arr2[j]] = 2 # common element was not found in the first array
 
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

