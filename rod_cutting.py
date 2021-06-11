''' rod cutting problem, we have a rod of length, we can only cut pieces of length x, y and z.
We need to find all possible ways summing up x,y, z with repitition such that the sum is equal
to n.'''

''' we can build a table containing n entries from 1 to n where each entry keeps the maximum count
of segments needed to build that number using x, y, z. As the base case, we put 1 in the table[x], 
table[y] and table[z] locations'''

def max_seg_count(n, x, y, z):
    # build the memoization table
    table = [0] * (n + 1)
    
    # fill in the base cases, since x, y, z are
    # given the max posible number of segments
    # needed to build the number is 1.
    # in some cases, these numbers can be updated
    # later e.g. if we have x = 1, y = 2
    # initially table[2] = 1 but later it can be
    # be updates as table[2] = 2 
    table[x] = table[y] = table[z] = 1

    min_seg = min(x, y, z)

    # now fill the table in a bottom up manner
    for i in range(1, n+1):
        # we can take one of the numbers x, y, z in turn and try to 
        # find the maximum possible segment count to build n - that number
        # which is picked

        # but we need to take care of the fact that i < x or i < y or i < z
        x_entry = table[i - x] if i >= x else 0
        y_entry = table[i - y] if i >= y else 0
        z_entry = table[i - z] if i >= z else 0
        # if i is less than all the elements, then there is no update
        # else there canbe an update
        if x_entry != 0 or y_entry != 0 or z_entry != 0:
            entry = 1 + max(x_entry, y_entry, z_entry)
            if entry > table[i]:
                table[i] = entry

    print(table)
  
    return table[n]
        

n = 4
x = 2
y = 1
z = 1

###

'''
n = 5
x = 5
y = 3
z = 2
'''
print(max_seg_count(n, x, y, z))
