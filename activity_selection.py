""" The following implementation assumes that the activities
are already sorted according to their finish time"""

# print the maximum set of activities that can be done by a single person, one
# at a time

# no. of total activities
# s[] - > an array that contains the start times of the tasks
# f[] - > an array that contains the finish time of the tasks
def print_max_activities(s, f):
    n = len(f)
    print('The following activities are selected')

    # the first activity is always selected
    i = 0
    print(i)

    # consider ther est of the activities
    for j in range(n):
        # If this activity has start time greater than the previous 
        # finish time then select it
        if s[j] >= f[i]:
            print(j)
            i = j

# code to test the avobe program
s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
print_max_activities(s, f)
