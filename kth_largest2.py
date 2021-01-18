#User function Template for python3

import heapq

class Solution:
    def kthLargest(self, k, arr, n):
        # code here 
        #print('k: ', k)
        #print('arr: ', arr)
        #print('n: ', n)
        kth_max_heap = []
        #n = len(arr)
        #print('n: ', n)
        i = 0
        res_str = ''
        while i < k-1:
            res_str += '-1 '
            heapq.heappush(kth_max_heap, arr[i])
            i += 1
        
        # pushing the kth element on the heap
        heapq.heappush(kth_max_heap, arr[k-1])
        
        #print('kth_max_heap', kth_max_heap)
        prev = heapq.heappop(kth_max_heap)
        heapq.heappush(kth_max_heap, prev)
        for i in range(k-1, n):
            #print('arr[i]: ', arr[i])
            if arr[i] > kth_max_heap[0]:
                #print('kth_max_heap: ', kth_max_heap)
                prev = heapq.heappushpop(kth_max_heap, arr[i])
                
            res_str = res_str + str(prev) + ' '

        return res_str

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        k,n=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.kthLargest(k,arr,n))

