# Python 3 program to find the minimum
# possible difference between maximum
# and minimum elements when we have to
# add / subtract every number by k
 
# Modifies the array by subtracting /
# adding k to every element such that
# the difference between maximum and
# minimum is minimized

def getMinDiff(arr, n, k):
    if n == 1:
        return 0

    # sort all elements
    arr.sort()

    # Initialize the results
    ans = arr[n-1] - arr[0]

    # the smallest number will be increased and the biggest number
    # will be decreased else, the difference between the resulting
    # maxmum and minimum will be bigger
    # Handle corner elements
    small = arr[0] + k
    big = arr[n-1] - k

    if small > big:
        small, big = big, small

    # traverse middle elements
    for i in range(1, n-1):
        subtract = arr[i] - k
        add = arr[i] + k
        
        # if both subtractio and addition do not change diff
        if subtract >= small or add <= big:
            # this element does not impact the current situation
            continue

        
        # if we are here that means either subtract < small or add > big
        # or both. We do not know which is the case, so we look for all
        # minimum differences at this stage. It could be big - subtract as
        # the current smallest ele could be subtract or add - small as the
        # current biggest ele could be add. So instead of comparing with the
        # previous min difference we compare these two differences and pick
        # up the minimum
        # Either subtraction causes a smaller number or addition
        # causes a bigger number. Update small or big using greedy
        # approach(if big - subtract causes small diff, then update
        # small elese update big
        if big - subtract <= add - small:
            # change the smallest element to reflect the current change
            small = subtract
        else:
            big = add
    
    return min(ans, big - small)

arr = [4, 6]
n = len(arr)
k = 10

print("max difference after minimizing the difference is: ", getMinDiff(arr, n, k))


arr = [1, 15, 10]
n = len(arr)
k = 6

print("max difference after minimizing the difference is: ", getMinDiff(arr, n, k))

arr = [1, 15, 5, 10]
n = len(arr)
k = 3

print("max difference after minimizing the difference is: ", getMinDiff(arr, n, k))
