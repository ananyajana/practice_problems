''' to minimize the amount of money to buy all candies, this can be done
by sorting the price array in ascending order, buying the candies from the lowest price one by one and then selecting the k candies from the right or the
highest price. Similarly to find the maximum amount of money spent to buy all
candies the exact oppostite of this needs to happen - buying cadies from the
right and picking candies from the left of the sorted array.'''

def find_candy_count(candies, n, k):
    arr = candies.copy()
    # this is for maximum price
    #arr.sort(reverse=True)
    # this is for minimum price
    arr.sort()
    print('sorted_arr is:', arr) 
    # start traversing the array from the left
    cost = 0
    for i in range(n):
        # buying each candy brings down the 
        # number of k candies from the right
        if i > 0 and i > n - 1 - ((i-1)*k):
            break
        cost += arr[i]
        # update the count of candies left
        # thid does not change the range n 
        #n = n - k

    print('minimum cost:', cost)


N = 4
K = 2
candies = [3, 2, 1, 4]
find_candy_count(candies, N, K)

