''' the price of the toys need to be sorted and then picked up starting from the minimum'''

def find_num_toys(arr, k):
    arr.sort()
    
    count = 0
    toy_sum = 0
    for i in range(len(arr)):
        # if the price of the current oty is greater than k
        # then it cannot be bought
        if arr[i] < k:
            toy_sum += arr[i]
            count += 1
            if toy_sum >= k:
                return (count - 1)
        else:
            break

    return count


cost = [1, 12, 5, 111, 200, 1000, 10]
k = 50
print(find_num_toys(cost, k))


    
    
