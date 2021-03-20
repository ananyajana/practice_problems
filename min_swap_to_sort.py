# program to find the minimum number of swaps
# required to sort an array

# function returns the minimum number of swaps required
# to sort an array
def min_swap(arr):
    n = len(arr)

    # create two arrays and use
    # as pairs whpse first array is element
    # and second array is position of first element
    arrpos = [*enumerate(arr)]
    
    # Sort the array by the array element
    # values to get right position of every element
    arrpos.sort(key = lambda it : it[1])
    # to keep track of visited elements. Initialize all
    # elements as not visited or False
    vis = {k: False for k in range(n)}
    
    # initialize the result
    ans = 0
    for i in range(n):
        # aready swapped ot already present at
        # correct position
        if vis[i] or arrpos[i][0] == i:
            continue
        
        # find number of nodes in this cycle and add it to ans
        cycle_size = 0
        j = i
        while not vis[j]:
            # mark node as visited
            vis[j] = True

            # move to the next node
            j = arrpos[j][0]
            cycle_size += 1

        # update the answer by adding the current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)

    return ans

arr = [1, 4, 3, 2]
print(min_swap(arr))

