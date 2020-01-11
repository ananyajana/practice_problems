
T = int(input())
st_list =[]
N_list =[]
for t in range(T):
    N_list.append(int(input()))
    st_list.append(input().split())


def longest_common_prefix(s, n):
    match_idx = -1
    s1 = s[0]
    for i in range(len(s1)):
        for k in range(1, n):
            if i < len(s[k]):
                if s1[i] != s[k][i]:
                    # return the string till previous match_idx or else -1
                    return match_idx if match_idx < 0 else s1[:match_idx + 1]
                #print(' i here :', i)
            else:
                # return the string till previous match_idx or else -1
                return match_idx if match_idx < 0 else s1[:match_idx + 1]

        # if we have reached here, all the strings are checked for the particular
        # index i and they match so far
        if k == n - 1:
            #print(' i here2 :', i)
            match_idx = i
            #print('match_idx here :', match_idx)

    # done with checking all the strings for a common prefix    
    return s1[:match_idx + 1] 
    

for t in range(T):
    s = st_list[t]
    n = N_list[t]
    print(longest_common_prefix(s, n))
