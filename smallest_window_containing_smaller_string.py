T = int(input())

# we need to find the smallest window containing all the characters of another string
# i.e. the smaller string
# we scan the first string from one side and hash only those characters which are part of
# second string and increment the existing count. At the end of this process, we start again scanning the first string
# from either left or right side(let's say right) and reduce the count of the chars until the point where reducing further would lead
# to a zero count i.e the remaining substring does not contain all the characters from the smaller string
# then we start again scanning from the other side(i.e. left) in similar fashion and stop at a similar condition
# the string at this point is a substring which contains all the charaters. But we can have another string
# if we had started from the opposite side(i.e. left) in the very beginning. The strings found from scanning from
# left and scanning from right might not be identical and hence we need to take the smaller substring
# another interesting thing to note here is that there might be some repeated characers in the smaller or the array
# and we need not consider repeat occurences while hashing the characters from it for the first time.
# hence the substring we found could actually be of smaller size than the second or the smaller array


import copy

# arr1 is the source string where we need to find all occurences of the destination string arr2
def smallest_window(arr1, arr2):
    temp = dict()
    # hash the smaller array or the second array
    # don't need to update count for repeat occurences
    for i in range(len(arr2)):
        temp[arr2[i]] = 1

    # wherever we find a char in the the first array which is also presen tin the 
    # second array we update the count in this pass
    for j in range(len(arr1)):
        if arr1[j] in temp.keys():
            temp[arr1[j]] += 1
    print('temp: ', temp)

    # at the end of this step we need to check whether the count of all the elements in > 1
    # if not, that means arr1 does not contain all characters from arr2
    for key in temp.keys():
        if temp[key] == 1:
            return -1
    
    # making two copies of the dictionary as we need to update the copies 
    # in the left and right scan respectively
    # can we use dynamic programming in subway, this seems to have the optimal substructure
    # fir for dynamic programming
    # making deep copies as by default it is shallow copy
    temp1 = copy.deepcopy(temp)
    temp2 = copy.deepcopy(temp)
    print('\n\ntemp: {}\ntemp1: {}\ntemp2: {}'.format(temp, temp1, temp2))

    l_mark1 = 0 # this contains the left most marker of the first viable substring
    for j in range(len(arr1)):
        if arr1[j] in temp1.keys():
            print('char is: ', arr1[j])
            print('before temp1[arr1[j]]: {}'.format(temp1[arr1[j]]))
            temp1[arr1[j]] -= 1
            print('after temp1[arr1[j]]: {}'.format(temp1[arr1[j]]))
            # the count of one of the chars is = 1, we found one end point of a viable substring
            if temp1[arr1[j]] == 1:
                print('j: ', j)
                l_mark1 = j
                break;
    
    r_mark1 = 0    # this contains the rightmost marker of the first viable substring
    for j in reversed(range(len(arr1))):
        if arr1[j] in temp1.keys():
            temp1[arr1[j]] -= 1
            # the count of one of the chars is < 1, we found one end point of a viable substring
            if temp1[arr1[j]] == 1:
                r_mark1 = j
                break;

    print('\n\ntemp: {}\ntemp1: {}\ntemp2: {}'.format(temp, temp1, temp2))
                
        
    r_mark2 = 0    # this contains the rightmost marker of the first viable substring
    for j in reversed(range(len(arr1))):
        if arr1[j] in temp2.keys():
            temp2[arr1[j]] -= 1
            # the count of one of the chars is < 1, we found one end point of a viable substring
            if temp2[arr1[j]] == 1:
                r_mark2 = j
                break;
                
    l_mark2 = 0 # this contains the left most marker of the first viable substring
    for j in range(len(arr1)):
        if arr1[j] in temp2.keys():
            temp2[arr1[j]] -= 1
            # the count of one of the chars is < 1, we found one end point of a viable substring
            if temp2[arr1[j]] == 1:
                l_mark2 = j
                break;

    print('\n\ntemp: {}\ntemp1: {}\ntemp2: {}'.format(temp, temp1, temp2))

    #print('range: ', range(5))
    #print('reversed range: ', reversed(range(5)))
    print('l_mark1:{}, r_mark1: {}, l_mark2: {}, r_mark2: {}'.format(l_mark1, r_mark1, l_mark2, r_mark2)) 
    
    rlen = r_mark1 - l_mark1 + 1
    llen = r_mark2 - l_mark2 + 1
    
    if rlen > llen:
        return arr1[l_mark1:r_mark1+1]
    elif rlen < llen:
        return arr1[l_mark2:r_mark2+1]
    else:
        return (arr1[l_mark1:r_mark1+1], arr1[l_mark2:r_mark2+1])

for t in range(T):
    arr1 = input()
    arr2 = input()
    print('arr1: {}, arr2: {}'.format(arr1, arr2))
    val = smallest_window(arr1, arr2)
    if val == -1:
        print('equal')
    else:
        print('{} '.format(val))

