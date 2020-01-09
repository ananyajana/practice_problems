
T = int(input())
st_list =[]
for t in range(T):
	st_list.append(input())

NUM_CHARS = 256

def longest_unique_substr(s):
    n = len(s)
    # to store the length of the current substring
    cur_len = 1
    # to store the result
    max_len = 1
    # to store previous index
    prev_index = 0
    i = 0

    # initialize the visited array as -1. -1 is used to indicate
    # that the character has not been visited yet.
    visited = [-1] * NUM_CHARS 
    
    # mark the first character as visited by storing the index of
    # first character in visited array.
    visited[ord(s[0])] = 0

    # start from the second character. First character is already 
    # processed(cur_len and max_len are initialized as 1, 
    # visited[ord(s[0])] is set

    for i in range(1, n):
        prev_index = visited[ord(s[i])]

        # if the current character is not present in the already
        # processed substring or it is not part of the current NRCS
        # then increment cur_len
        if prev_index == -1 or (i - cur_len > prev_index):
            cur_len += 1

        # if the current character is present in the current NRCS
        # then update the NRCS to start from the next character of
        # previous instance
        else:
            # also when we are changing NRCS, we should also check
            # whether length of the previous NRCS was greater than
            # max_len or not
            if cur_len > max_len:
                max_len = cur_len

            cur_len = i - prev_index

        # upda the index of the current character
        visited[ord(s[i])] = i
    
    # compare the length of the last NRCS with max_len and update
    # max_len if needed
    if cur_len > max_len:
        max_len = cur_len
    
    return max_len

for t in range(T):
	s1 = st_list[t]
	print(longest_unique_substr(s1))
