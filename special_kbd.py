def findoptimal(N):
    # The optimal string length is 
    # N when N is smaller than 7
    if N <= 6:
        return N
    
    # initialize the result
    maxi = 0
    
    # Try all possible break-points
    # for any keystroke N, we need
    # to loop from N-3 keystrokes
    # back to 1 ketstroke to find
    # a breakpoint 'b' after which we
    # will have Ctrl-A, Ctrl-V and Ctrl-V
    # and then only Ctrl-V all the way.

    for b in range(N-3, 0, -1):
        curr = (N - b - 1) * findoptimal(b)
        if curr > maxi:
            maxi = curr
    
    return maxi


for n in range(1, 10):
    print('Maximum number of As with ', findoptimal(n))

