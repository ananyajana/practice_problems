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

def find_smallest(s):

    # store the last occurrence of every character
    # set -1 as default for every character
    loccur = [-1]*26

    for i in range(len(s) - 1, -1, -1):
        # character index to fill
        # in the last occurrence array
        chI = ord(s[i]) - ord('a')
        if loccur[chI] == -1:
            # if this is true then this character is being visited
            # for the first time from the last
            # thus the last occurrence of this chracter is stored in this index
            loccur[chI] = i

    # the sorted version of the string is tored in sorted_s
    sorted_s = s
    sorted_s.sort()

    for i in range(len(s)):
        if s[i] != sorted_s[i]:
            # Character to replace
            chI = ord(sorted_s[i]) - ord('a')

            # Find the last occurrence
            # of this character
            last_occ = loccur[chI]
            # swap this with the last occurrence
            # swap(s[i], s[last_occ], this is because s[i[ contains the big
            # char and s[last_occ] contains the small char
            # the last index is replaced because to maintain the lexicographic
            # order
            s[i], s[last_occ] = s[last_occ], s[i]
            break

    return "".join(s)


s = 'geeks'
print(find_smallest(list(s)))

