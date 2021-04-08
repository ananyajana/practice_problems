#Given a string str of length N. The task is to find out the 
# lexicographically smallest string when at most only one swap 
# is allowed. That is, two indices 1 <= i, j <= n can be chosen 
# and swapped. This operation can be performed at most one time.
# string is sorted lexicogrphically and then copared to the original string
# whenever the first mismatch occurs, those are the characters that need to be
# replaced, remember in the origin string the bigger character is present
# at this location of mismatch, the last occurrence of the smaller character
# is found the original string and replaced with this bogger chara
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

