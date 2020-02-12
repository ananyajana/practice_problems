

# problems from geeksforgeeks must do coding questions
T = int(input())
st_list =[]
N_list = []
for t in range(T):
    N_list.append(int(input()))
    st_list.append(input())


def print_tour(lis):
    # set the start and end indices of the queue
    start = 0
    end = 1
    curr_petrol = 1
    n = len(lis)
    # keep traversing the petrol pumps until start != end or the petrol falls negative
    while start != end and curr_petrol > 0:
        curr_petrol = lis[start][0] - lis[start][1]
        if curr_petrol < 0:
            start = (start + 1)%n
            end = (end + 1)%n
        while start!= end and curr_petrol > 0:
            curr_petrol += lis[start][0] - lis[start][1]
                


for t in range(T):
    s = st_list[t].split()
    #print(s)
    # convert the string into int 
    s = [int(s[i]) for i in range(len(s))]
    print(s)
    n = N_list[t]
    #print(n)
    arr = []
    
    # create an array of petrol pump objects
    # the actual given array size is n*2 
    for i in range(0, n*2, 2):
        arr.append([s[i], s[i + 1]])

    #print(arr)
    print(print_tour(arr))
        
