# problems from geeksforgeeks must do coding questions
# dynamic programming approach to solve the problem
# the problem has optimal substructure i.e. if we solve
# the subproblem: minimum time needed to rot every orange
# we can solve the entire problem.
# overlapping subproblems? The minimum time needed to rot
# an orange is dependent on theminimum time needed to rot
# its neighbors

C = None
R = None

INT_MAX = 10000

# memoization table to memoize the values
table = []

# visited array to keep track of the visited nodes
visited = []

# matrix containing the array entries
mat = []

T = int(input())
st_list =[]
N_list = []
for t in range(T):
    N_list.append(input())
    st_list.append(input())


# function to return the minimum of four numbers
def min_find(p, q, r, s):
    #print('p :{}, q :{}, r :{}, s :{}'.format(p, q, r, s))
    if (p < q):
        temp1 = p
    else:
        temp1 = q
    if (r < s):
        temp2 = r
    else:
        temp2 = s
    if (temp1 < temp2):
        #print('{} < {}'.format(temp1, temp2))
        return temp1
    else:
        #print('{} < {}'.format(temp2, temp1))
        return temp2


# function to return the minimum distance to any rotten orange
# from [i, j]
def dist(i, j):
    #print(table)
    #print('i :', i)    
    #print('j :', j)    
    # if i, j are outside the array
    #print('mat[{}][{}]: {}'.format(i, j, mat[i][j]))
    if i >= R or i < 0 or j >= C or j < 0:
        #print('out of range')
        return INT_MAX

    # if result already exists in the table
    # use the memoized result
    elif table[i][j] > 0 and table[i][j] < INT_MAX:
        return table[i][j]
    
    # if 0 then can't lead to any path so return INT_MAX
    elif int(mat[i][j]) == 0:
        table[i][j] = INT_MAX
        return INT_MAX

    # if 2 then we have reached our rotten oranges
    # so return from here
    elif int(mat[i][j]) == 2:
        table[i][j] = 0
        #print('returning 0')
        return 0

    # if this node is already visited, then return to avoind infinite
    # loops
    elif visited[i][j] == 1:
        return INT_MAX

    else:
        # Mark the current node as visited
        visited[i][j] = 1
        temp1 = dist(i+1, j)
        #print('i+1: {}, j :{}, temp1 :{}'.format(i+1, j, temp1))
        temp2 = dist(i-1, j)
        #print('i-1: {}, j :{}, temp2 :{}'.format(i-1, j, temp2))
        temp3 = dist(i, j+1)
        #print('i: {}, j+1 :{}, temp3 :{}'.format(i, j+1, temp3))
        #print('temp3 :{}'.format(temp3))
        temp4 = dist(i, j-1)
        #print('i: {}, j-1 :{}, temp4 :{}'.format(i, j-1, temp4))
        #print('temp4 :{}'.format(temp4))

        # take the minimum of all
        table[i][j] = 1 + min_find(temp1, temp2, temp3, temp4)

        visited[i][j] = 0

    return table[i][j]

# function to return the min time required to rot all oranges
def rot_oranges(s):
    max = 0
    
    global table, mat, visited

    # calculate the minimum distance to any rotten 
    # orange from all the fresh oranges
    for i in range(R):
        for j in range(C):
            if int(mat[i][j]) == 1:
                dist(i, j)

    # pick the maximum distance of fresh orange
    # to some rotten orange
    for i in range(R):
        for j in range(C):
            if int(mat[i][j]) == 1 and table[i][j] > max:
                max = table[i][j]

    #print(table)
    # if all oranges can be rotten
    #print(max)
    if (max < INT_MAX):
        return max

    return -1    

    
for t in range(T):
    s1 = st_list[t]
    n = N_list[t]
    r, c = n.split()
    r = int(r)
    c = int(c)
    
    #global R, C
    R = r
    C = c
    #print('R :{}, C :{}'.format(R, C))
    #print(n)
    #print(s1)
    

    table = [[0 for i in range(c)] for j in range(r)]

    visited = [[0 for i in range(c)] for j in range(r)]
    s = s1.split()
    mat = [ s[i*c : (i+1)*c] for i in range(r)]    
    #print(mat)

    print(rot_oranges(s1))
