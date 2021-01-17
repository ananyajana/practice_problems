# problems from geeksforgeeks must do coding questions
# rearrange characters in string

import heapq

T = int(input())
st_list =[]
for t in range(T):
    st_list.append(input())

        

# make a list of count of all the characters of the string count[c - 'a']
NUM = 26
# make a priority queue to hold the character and its frequency with frequency
# as the key

# Now the list needs to be processed so that the strings could be processed to
# make a priority queue with the count of the elements
for t in range(T):
    s1 = st_list[t]

    count = [0] * NUM
    pq = []
    for i in range(len(s1)):
        count[ord(s1[i]) - ord('a')] += 1

    print(count)
    for i in range(NUM):
        if count[i]:
            # remember in python heap1 is a min heap, but we want a max
            # heap based priority queue
            heapq.heappush(pq, (count[i] * (-1), chr(ord('a') + i)))

    print(pq)

    # this will store the resultant value
    str = ''

    # work as the previous visited element
    # initial previous elements be. ('#' and its frequency is -1)
    prev = (-1, '#')

    # traverse the queue
    while (len(pq)) != 0:
        # pop the element with the highest frequency
        k = heapq.heappop(pq)
        str = str + k[1]

        print('after popping', pq)

        # if frequency of previous character is less than zero that
        # means it is useless, we need not push it
        if prev[0] > 0:
            # need to convert to list and then back convert again as tuples a re immutable
            prev_ = list(prev)
            prev_[0] = prev_[0] * ( -1)
            prev = tuple(prev_)
            heapq.heappush(pq, prev)
        

        print('after pushing', pq)

        # make the current character as the previous character and
        # decrease the frequency by one
        # converting tuple to a list as the key needs to be decremented
        k_ = list(k)
        k_[0] = k_[0] * (-1)
        k_[0] -= 1
        k = tuple(k_)
        prev = k

    # if the length of the resultant string and original string is not 
    # the same then string is not valid

    if (len(s1)) != len(str):
        print('string not valid')
    else:
        print('string is:', str)

    
    
	
