

# problems from geeksforgeeks must do coding questions
T = int(input())
st_list =[]
N_list = []
for t in range(T):
    N_list.append(int(input()))
    st_list.append(input())


def print_tour(lis):
    n = len(lis)
    #print(n) 

    start = 0
    end = n-1
    i = 0
    curr_petrol = 0
    while i < n:
        # if the petrol falls -negative at any time, start and end node
        # needs to be changed and current petrol needs to be reset
        curr_petrol += lis[i][0] - lis[i][1]
        if curr_petrol < 0:
            #print('current petrol negative')
            start = (start + 1)%n
            end = (end + 1)%n
            curr_petrol = 0
            i = i + 1
            continue
        while start != end:
            #print('start', start)
            #print('i', i)
            k = start
            start = (start + 1)%n
            curr_petrol += lis[start][0] - lis[start][1]
            # if current petrol falls negative, the current start node has to be changed
            if curr_petrol < 0:
                #print('current petrol negative')
                start = (k + 1)%n
                end = (end + 1)%n
                curr_petrol = 0
                i = i + 1
                break;
        # if the start node equals end node then a route is found and returned
        if start == end:
            return i 
    return -1



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
    print(print_tour(arr))
        
