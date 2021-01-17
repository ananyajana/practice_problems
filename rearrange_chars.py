# problems from geeksforgeeks must do coding questions
# rearrange characters in string

import heapq

T = int(input())
st_list =[]
for t in range(T):
    st_list.append(input())

        

# make a list of count of all the characters of the string count[c - 'a']
NUM = 26
count = [0] * NUM
# make a priority queue to hold the character and its frequency with frequency
# as the key
pq = []

# Now the list needs to be processed so that the strings could be processed to
# make a priority queue with the count of the elements
for t in range(T):
    s1 = st_list[t]

    for i in range(len(s1)):
        count[ord(s1[i]) - ord('a')] += 1

    print(count)
    for i in range(NUM):
        if count[i]:
            # remember in python heap1 is a min heap, but we want a max
            # heap based priority queue
            heapq.heappush(pq, (count[i] * (-1), chr(ord('a') + i)))

    print(pq)
    
	
