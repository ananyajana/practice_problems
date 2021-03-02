import operator
T = int(input())

# counting the zero-sum subarrays is easy when
# there are no contiguous zero-sum subarrays
# because the presence of two contiguous zero-sum
# subarrays automatically make up a third zero-sum
# subarray which spans the entire two zero-sum subarrays
# this means we would need to know all the last indices

# this function originally did not take care of the contiguous subarrays case
def zero_sum_subarray(arr, n):
    temp = dict()
    cnt = 0
    cur_sum = 0
    for i in range(n):
        cur_sum += arr[i]
        if (cur_sum in temp.keys()) or (cur_sum == 0) or (arr[i] == 0):
            cnt += 1
            print('count: {}, i: {}, arr[i]: {}'.format(cnt, i, arr[i]))
        else:
            temp[cur_sum] = 1

    return cnt

def zero_sum_subarray1(arr, n):
    temp = dict()
    cur_sum = 0
    out = []
    for i in range(n):
        cur_sum += arr[i]
        # list that holds the indices of a particular subarray sum
        # can this handle the cases 0, 0, -5, 5, 0, 0
        al = []
        if cur_sum == 0:
            out.append((0, i)) # the start index of the subarray is 0 and end index is i

        if cur_sum in temp.keys():
            al = temp.get(cur_sum)
            for j in range(len(al)):
                out.append((al[j] + 1, i))    # this is because this sum was already in hashmap
                # and that means the current same sum is the subarray(last index of last same sum + 1) 
        # append in the al array the current index as the last index of the current sum suarray
        al.append(i)
        temp[cur_sum] = al

    return out


for t in range(T):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print('arr: {}, n: {}'.format(arr, n))
    print('zero sum subarray count: ', zero_sum_subarray(arr, n))
    print('zero sum subarray count: ', len(zero_sum_subarray1(arr, n)))

