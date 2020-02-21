# to find the max of subarrays, is this similar to
# finding the minimum element of a stack at any time?

from collections import deque
T = int(input())
st_list =[]
N_list = []
for t in range(T):
    N_list.append(input())
    st_list.append(input())

def find_max_of_subarrays(s, n):
    #print('here')
    n, k = n.split()
    #print(s)
    n = int(n)
    k = int(k)
    s = s.split()
    s = [int(s[i]) for i in range(len(s))]
    #print(s)
    # create a double ended queue Qi that will
    # store indices of useful elements in every
    # window and it will maintain decreasing order
    # of values from front to reas in Qi, i.e. arr[Qi.front()]
    # to arr[Qi.rear()] are in sorted in decreasing
    # order
    Qi = deque()

    # Process first k(first window)
    for i in range(k):
        while Qi and s[i] >= s[Qi[-1]]:
            # pop from the back
            Qi.pop()
    
        # add the index of the current element to the end of Qi
        Qi.append(i)
    
    # process the rest of the elements which are outside
    # the first window
    for i in range(k, n):
        # the element at the front ot the queue is the
        # largest element of the previous array, so print it
        print(str(s[Qi[0]]) + " ", end = "")
        
        # rempove those elements which are not part of current
        # window
        while Qi and Qi[0] <= i-k:
            # remove from the front of Qi
            Qi.popleft()
        
        # Now the queue does not have any element which are not
        # part of current window
        Qi.append(i)
    
        # follow the same procedure followied for the first window,
        # removing all the elements less than the current element being
        # processed from the rear of the queue
        while Qi and s[i] >= s[Qi[-1]]:
            Qi.pop()
        
        # Add the current element at the rear of Qi
        Qi.append(i)
    # print the last element
    print(str(s[Qi[0]]))

    
    

    
    
for t in range(T):
    s1 = st_list[t]
    n = N_list[t]
    #print(n)
    #print(s1)
    
    find_max_of_subarrays(s1, n)
