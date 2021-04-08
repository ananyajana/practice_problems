'''
You are given a string s of lower case english alphabets. You can choose any two characters in the string and replace all the occurences of the first character with the second character and replace all the occurences of the second character with the first character. Your aim is to find the lexicographically smallest string that can be obtained by doing this operation at most once.
'''

# the first question to answer is how to choose the two charas? will the answer
# be non-unique? I think no, the answer should be unique..
# will the lexicographically smallest char always be selected? I think np. e.g
# the string acbd , the characters to be swapped are probably c and b
# we probably need to see what characters are present in the string e.g. if we find the fist chracters is not lexicogrpahy smallest then that has to be one of
# the characters to be reaplced?
# the string needs to  be sroted lexicographically and then compared to the
# original string. Whereever the first mismatch occurs in the corresponding characters, those are the characters to be swapped 

# but in this case lexicogrphic sorting is bit difficult all occurrences
# of a particular character can be replaced

# we also need to store first occurrences of all the chars
# to find the lexicographically smaller string, the leftmost char must be
# replaced with some charawhich is smaller than it. This will happen if the 
# smaller char appears after it in the array
# traverse the string from the left and for every charac, fin dthe smallest 
# char(even smaller than current char) that  appears after and then swap all their occurrences to get the string
# if no such char is found then the previous string is the required string

MAX=256

# function to retur the lexicographically smallest after swapping alli
# occurrences of any two charas

def find_smallest(str):
    n = len(s)
    i, j = 0, 0
    # to store the first index of every chara of string
    chk = [-1 for i in range(MAX)]

    # store the first occurring index for every char
    for i in range(n):
        # if the current char is appearing for the first time in str
        if chk[ord(str[i])] == -1:
            chk[ord(str[i])] = i

    # starting from the leftmost char
    for i in range(n):
        flag = False
        # For every char smaller than ord(str[i])
        for j in range(ord(str[i])):
            # if there is a char in str which is amller than
            # ord(str[i]) and appears after it
            if chk[j] > chk[ord(str[i])]:
                flag = True
                break

        # if the required char  pair is found
        if flag:
            break

    # if sapping is possible
    if i < n:
        # chars to be swapped
        ch1 = str[i]
        ch2 = chr(j)

        # for every char
        for i in range(n):
            # Replace every ch1 with ch2 and vice versa
            if str[i] == ch1:
                str[i] = ch2

            elif str[i] == ch2:
                str[i] = ch1
    return ''.join(str)
    


#s = 'geeks'
#s = 'ccad'
s = 'abba'
print(find_smallest(list(s)))

