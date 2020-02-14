

# problems from geeksforgeeks must do coding questions
T = int(input())
st_list =[]
N_list = []
for t in range(T):
    N_list.append(int(input()))
    st_list.append(input())


def print_tour(lis,n):
    # consider the first petrol pump as the starting point
    start = 0
    end = 1
    curr_petrol = lis[start][0] - lis[start][1]

    # run a loop while all petrol pumps are not visited
    # and we have reached first petrol pump again with 0 or more petrol
    # we keep enqueueing the nodes until tour is complete or petrol
    # falls negative, if petrol amount becomes negative we keep dequeueing
    # until the queue is empty
    while(end != start or curr_petrol < 0):
        #run a loop while all petrol pumps are not visited
        # and we have reached first petrol pump again with 0
        # or more petrol
        # dequeueing nodes while the current petrol is negative
        while(curr_petrol < 0 and start != end):
            # as the curr_petrol is negative, the start needs
            # to be changed
            # remove the starting petrol pump, change start
            curr_petrol -= lis[start][0] - lis[start][1]
            start = (start + 1)%n

            # if 0 is being considered as start again, then there is no possible solution
            if start == 0:
                return -1
        # add a petrol pump to the current tour
        curr_petrol += lis[end][0] - lis[end][1]
        end = (end + 1)%n

    return start


for t in range(T):
    s = st_list[t].split()
    #print(s)
    # convert the string into int 
    s = [int(s[i]) for i in range(len(s))]
    #print(s)
    n = N_list[t]
    #print(n)
    arr = []
    
    # create an array of petrol pump objects
    # the actual given array size is n*2 
    for i in range(0, n*2, 2):
        arr.append([s[i], s[i + 1]])

    #print(arr)
    print(print_tour(arr, n))
        
