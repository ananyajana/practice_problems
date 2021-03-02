import operator
T = int(input())

# the idea is when we get a number we insert as key the number+1 and increment the value which is the count
# if the
# or can we do this, for every number start counting the longest consecutive subsequence from that number
# and update the smaller values as well

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


for t in range(T):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print('arr: {}, n: {}'.format(arr, n))
    print('zero sum subarray count: ', zero_sum_subarray(arr, n))

