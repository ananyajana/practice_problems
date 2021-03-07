T = int(input())

# to remove an element i.e. one instance of any character such that the frequency of the remaining elements are the same
# create two hash lists: firs hash list will contain the keys as the charS and the values
# as the counts. second hash list will contain the counts as the keys and the chars as the
# values, if the # unique keys is > 2 or =1, then return -1. else delete the

def same_freq(arr1):
    temp = dict()
    for i in range(len(arr1)):
        print('arr[i]: ', arr1[i])
        if arr1[i] not in temp.keys():
            temp[arr1[i]] = 1
        else:
            temp[arr1[i]] += 1

    
    # create a second hashmap containing the counts in the first hasmap as keys 
    temp2 = dict()
    for key in temp.keys():
        print('key: ', key)
        if temp[key] not in temp2.keys():
            temp2[temp[key]] = [key]
        else:
            temp2[temp[key]].append(key)
            #print('temp2[key]: ', temp2[temp[key]])
        print('temp2: ', temp2)

    print('temp is: ', temp)
    print('temp2 is: ', temp2)

    # if the length of the second hashmap is one then it is possible to meet the condition only
    # when either of this is true - 1. the number of chars with that frequency is 1
    # or the frequency is 1
    temp_len = len(list(temp2.keys()))   # number of keys in the first hash map
    print('temp_len: ', temp_len)
    if temp_len == 1:
        for key in temp2.keys():
            if key == 1 or len(temp2[key]) == 1:
                return 0
        return -1

    # if there are more than 2 distinct counts or frequencies, then it is not possible to make the
    # the frequencies equal just by deleting one character
    if temp_len > 2:
        print('returning from here')
        return -1
    
    # there are two ways in which thi is possible
    # 1. if the one freq is +1 or -1 of the other frquency
    # if one of the frequencies is 1 
    prev_key = None # this stores the previous key see in the temp2 hashmap
    # this is the only other key present in the hashmap apart from the current key
    for key in temp2.keys():
        val_list = temp2[key]
        # if one key is +1 or -1 of the other key, then return success
        if prev_key is not None and (key +1 == prev_key or key -1 == prev_key) and len(val_list) == 1:
            return 0
        prev_key = key
        # if one of the keys is 1, and there is only one character with that frequency return success
        if len(val_list) == 1 and key == 1:
            #return val_list[0]
            return 0
    
    print('returning from the last')
    return -1


for t in range(T):
    arr1 = input()
    print('arr1: {}'.format(arr1))
    val = same_freq(arr1)
    if val == -1:
        print('No')
    else:
        print('{} can be rmeoved '.format(val))

