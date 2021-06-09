''' we need to stack boxes such that each of the base dimension of the 
lower box is strictly greater than that of the upper box. the height, width
and length can be changed. find the maximum height possible height.'''

''' we make some observations 
1. even if we interchange the width and length, height does not change
2. since the lower box base dims must be greater and assuming that
the dims are integers, the sum of the lowerbox dim >= upper box dim + 2
3. for every box 3! = 6 permutations or arrangements are possible

We can have the base case as a stack of single box where the max height
is the height of that particular boxi or maybe we should try to stack the 
other dim combinations of the same box as well. in that case, the biggest
dim combination should be the lower box e.g. the box with (10, 12, 32)
can be placed as (10, 12, 32) and then (32, 10, 12). Is max possible
count of same box apprearing is 2?i

One more important observation is that for a box its dims i.e. h, w, l can
actually be in any array not necessarily that h has to be in height, etci

another important observation is that a box can be stacked on top of it
just by interchanging the width and length'''

import numpy as np

def max_height_stack_boxes(n, height, width, length):
    # create a memoization table, what is the maximum possible
    # height of the stack keeping the current box as the very bottom
    table = [0 for i in range(n)]

    # fill in the base cases
    for i in range(n):
        # let's check if two combinations are possible for the box
        # we can sort the three elements and try making the 
        # sorted_list[0] as height and sorted_list[2] as height
        # sorted_list[1] can never be the height as one of the dims
        # are common and that is the biggest dim which can't fit
        # inside any other dim
        # but we may not want to do this since by stacking these two
        # we are taking out some possibilities i.e. some other boxes
        # could have been stacked between the two
        # so we just try to maximize the base while filling the base
        # case and no stacking of the same box
        arr = []

            
        arr.append(height[i])
        arr.append(width[i])
        arr.append(length[i])
        print('before sorting: arr: ', arr)
        for j in range(3):
            for k in range(j, 3):
                if arr[j] > arr[k]:
                    # if the jth element is greater than kth element then swap
                    temp = arr[j]
                    arr[j] = arr[k]
                    arr[k] = temp
        print('after sorting: arr: ', arr)


height = [4,1,4,10]
width = [6,2,5,12]
length = [7,3,6,32]

n = len(height)
max_height_stack_boxes(n, height, width, length)
