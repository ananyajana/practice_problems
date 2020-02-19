# to find the max of subarrays, is this similar to
# finding the minimum element of a stack at any time?

T = int(input())
st_list =[]
N_list = []
for t in range(T):
    N_list.append(input())
    st_list.append(input())

def find_max_of_subarrays(s, n):
    n, k = n.split()
    n = int(n)
    k = int(k)
    s = s.split()
    s = [int(s[i]) for i in range(len(s))]
    print(s)
    print(n)
    print(k)
    return -1
    
for t in range(T):
    s1 = st_list[t]
    n = N_list[t]
    #print(n)
    #print(s1)
    
    print(find_max_of_subarrays(s1, n))
