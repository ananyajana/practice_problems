# problems from geeksforgeeks must do coding questions
# dynamic programming approach to solve the problem
# the problem has optimal substructure i.e. if we solve
# the subproblem: minimum time needed to rot every orange
# we can solve the entire problem.
# overlapping subproblems? The minimum time needed to rot
# an orange is dependent on theminimum time needed to rot
# its neighbors


T = int(input())
st_list =[]
N_list = []
for t in range(T):
    N_list.append(input())
    st_list.append(input())

INT_MAX = 10000000

# function to return the minimum of four numbers
def min(p, q, r, s):
    if (p < q):
        temp1 = p
    else:
        temp1 = q
    if (r < s):
        temp2 = r
    else:
        temp2 = s
    if (temp1 < temp2):
        return temp1
    else:
        return temp2


# function to return the minimum distance to any rotten orange
# from [i, j]
def dist(arr, i, j, table, visited):
    return table, visited
    

# function to return the min time required to rot all oranges
def rot_oranges(s, n):
    r, c = n.split()
    r = int(r)
    c = int(c)
    max = 0
    
    mat = [ s[i*c : (i+1)*c] for i in range(r)]    

    # DP table to memoize the values
    table = [[0 for i in range(c)] for j in range(r)]

    # visited array to keep track of already visited nodes
    # in order to avoid infinite loops
    visited = [[0 for i in range(c)] for j in range(r)]

    # calculate the minimum distance to any rotten 
    # orange from all the fresh oranges
    for i in range(r):
        for j in range(c):
            if mat[i][j] == '1':
                table, visited = dist(mat, i, j, table, visited)

    # pick the maximum distance of fresh orange
    # to some rotten orange
    for i in range(r):
        for j in range(c):
            if mat[i][j] == '1' and table[i][j] > max:
                max = table[i][j]

    # if all oranges can be rotten
    if (max < INT_MAX):
        return max

    return -1    

    
for t in range(T):
    s1 = st_list[t]
    n = N_list[t]
    #print(n)
    #print(s1)
    
    print(rot_oranges(s1, n))
