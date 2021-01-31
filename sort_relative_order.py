a1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
a2 = [2, 1, 8, 3]

# copy all the elements of a1 into a different list
temp = a1.copy()
# create another array visited of the same size as temp and
# it holds the indicator whether the corresponding element
# from temp is copied to a1
visited = [0] * len(a1)

# sort the temp array
temp.sort()

# initialize the output index as 0
idx = 0

# binary search for all occurrences of a2[i] in temp

# a binary search based function to find index of FIRST
# occurrence of x in arr[]. If x is not present, then it
# returns -1

def first(arr, low, high, x, n) :
    if (high >= low) :
        mid = low + (high - low) // 2;  # (low + high)/2; 
        if ((mid == 0 or x > arr[mid-1]) and arr[mid] == x) :
            return mid
        if (x > arr[mid]) :
            return first(arr, (mid + 1), high, x, n)
        return first(arr, low, (mid -1), x, n)
         
    return -1

m = len(a1)
n = len(a2)

# consider all elements of a2[]. Find them in temp
# and copy them in 
for i in range(0, n):
    # Find the index of the first occurrence
    # of a2[i] in temp
    f = first(temp, 0, m-1, a2[i], m)

    # if not present, no need to proceed
    if (f == -1):
        continue

    # Copy all occurrences of a2[i] to a1
    j = f
    while(j < m and temp[j] == a2[i]):
        a1[idx] = temp[j]
        idx += 1
        visited[j] = 1
        j += 1

# Now copy all the other elements of temp[] into a1[]
# chich are not present in a2[]
for i in range(0, m):
    if visited[i] == 0:
        a1[idx] = temp[i]
        idx += 1

print('a1: ', a1)
print('a2: ', a2)
print('temp: ', temp)
