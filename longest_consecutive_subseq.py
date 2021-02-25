import operator
T = int(input())

# the idea is when we get a number we insert as key the number+1 and increment the value which is the count
# if the
# or can we do this, for every number start counting the longest consecutive subsequence from that number
# and update the smaller values as well
def longest_consecutive_subsequence(arr, n):
    temp = dict()
    for i in range(n):
        if arr[i] not in temp.keys():
            temp[arr[i] + 1] = 1
        else:
            temp[arr[i] + 1] = temp[arr[i]] + 1
            del temp[arr[i]]

    print(temp)
    #inverse = [(value, key) for key, value in stats.items()]
    #print max(inverse)[1]
    max_len = max(temp.iteritems(), key=operator.itemgetter(1))[0]
    return max_len

def longest_consecutive_subsequence1(arr, n):
    temp = dict()
    max_len = 1
    for i in range(n):
        if arr[i] not in temp.keys():
            temp[arr[i]] = 1
    print(temp)

    for i in range(n):
        l = 0 # take the number as a part of the sequence and traverse in 
        # heap to see if the other keys are present
        j = 0
        while((arr[i]-j) in temp.keys()):
            print('inside the while loop i: {}, j: {}, arr[i]: {}'.format(i, j, arr[i]))
            l += 1
            j += 1

            if l > max_len:
                max_len = l
    return max_len

for t in range(T):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print('arr: {}, n: {}'.format(arr, n))
    print(longest_consecutive_subsequence1(arr, n))


