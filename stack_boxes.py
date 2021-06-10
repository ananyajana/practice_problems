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

# this version does not work, just keeping for the sak eof the logic
def max_height_stack_boxes(n, height, width, length):
    all_rots_tuples = []
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

# we create all three orientations of the box and put it in the list
# such that effectively the total number of boxes is 3*n and then do
# the algorithm 

# geeksforgeeks version
class Box:
    # representation of a box
    def __init__(self, h, w, d):
        self.h = h
        self.w = w
        self.d = d

    def __lt__(self, other):
        # I was initially thinking that this condition should be
        # based on sum, but yes, mult seems th correct way
        return  self.d * self.w < other.d * other.w

def max_stack_height(n, height, width, length):
    # put an array with all rotations of the given boxes.
    # e.g. for {1, 2, 3}, we have a total of three possibilities
    #{1, 2, 3}, {2, 3, 1}, {3, 1, 2}
    rot = [Box(0, 0, 0) for _ in range(3 * n)]
    index = 0
    
    for i in range(n):
        rot[index].h = height[i]
        rot[index].w = max(width[i], length[i])    
        rot[index].d = min(width[i], length[i])    
        index += 1
        
        # second combination
        rot[index].h = width[i]
        rot[index].w = max(height[i], length[i])    
        rot[index].d = min(height[i], length[i])    
        index += 1

        # third combination
        rot[index].h = length[i]
        rot[index].w = max(height[i], width[i])    
        rot[index].d = min(height[i], width[i])    
        index += 1

    # all the combinations of the boxes are in arry now
    n *= 3
    
    # sort the array rot[] in non-increasing order of base area
    rot.sort(reverse = True)

    # initialize ll msh values for all indices with the height of the box
    msh = [0] * n
    
    for i in range(n):
        msh[i] = rot[i].h

    # compute the optimized msh values in bottom up manner
    for i in range(1, n):
        # becaseu the rot array is already sorted on base value
        for j in range(0, i):
            if (rot[i].w < rot[j].w and rot[i].d < rot[j].d):
                if msh[i] < msh[j] + rot[i].h:
                    msh[i] = msh[j] + rot[i].h
    print('len :', len(msh))
    print(msh)
    maxm = -1
    for i in range(n):
        maxm = max(maxm, msh[i])

    return maxm

height = [4,1,4,10]
width = [6,2,5,12]
length = [7,3,6,32]

n = len(height)
#max_height_stack_boxes(n, height, width, length)
print(max_stack_height(n, height, width, length))
