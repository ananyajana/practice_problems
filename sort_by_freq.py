T = int(input())
st_list =[]
N_list = []
for t in range(T):
    N_list.append(int(input()))
    st_list.append(input())

print(N_list)
print(st_list)
def sort_by_freq(a, n):
    temp_arr = [-999] * n
    freq_arr =[0] * n

    #print('hello ', a)
    last_idx = 0
    for i in range(n):
        for j in range(n):
            # our goal is to find an empty slot in the temp_arr
            # to put the current element and update the corresponding
            # entry in freq array

            # the element in temp_arr is not
            # initialized means that we can put the 
            # current element in that location and
            # to move on to the next element in array a
            # OR
            # if the element is already present in temp_arr that means
            # we only need to update the frequency
            if temp_arr[j] == -999 or a[i] == temp_arr[j]:
                temp_arr[j] = a[i]
                freq_arr[j] += 1
                if last_idx < j:
                    last_idx = j
                break
            # else visit the next slot in temp_arr to see if it is empty

    #print('temp_arr: ', temp_arr)
    #print('last_idx in temp_arr: ', last_idx)
    #print('freq_arr: ', freq_arr)

    m = last_idx + 1
    for i in range(m):
        for j in range(i+1, m):
            # The big frequencies should be towards the front(descending order)
            if freq_arr[i] < freq_arr[j]:
                # exchange the frequencies
                temp1 = freq_arr[i]
                freq_arr[i] = freq_arr[j]
                freq_arr[j] = temp1

                # exchange the actual elements
                temp1 = temp_arr[i]
                temp_arr[i] = temp_arr[j]
                temp_arr[j] = temp1
            # if the frequencies are equal then smaller element would
            # be at the front
            if freq_arr[i] == freq_arr[j] and temp_arr[i] > temp_arr[j]:
                # exchange the actual elements
                temp1 = temp_arr[i]
                temp_arr[i] = temp_arr[j]
                temp_arr[j] = temp1
                
    #print('temp_arr: ', temp_arr)
    #print('last_idx in temp_arr: ', last_idx)
    #print('freq_arr: ', freq_arr)

    final_arr = temp_arr[:m]
    #print('final_arr: ', final_arr)
    return final_arr

for t in range(T):
    s = st_list[t]
    n = N_list[t]

    str_arr = s.split()
    new_arr = []
    for i in range(len(str_arr)):
         new_arr.append(int(str_arr[i]))
    new_arr
    sort_by_freq(new_arr, n)



