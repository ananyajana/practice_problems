# make palindromes with the minimum number of insertions

T = int(input())
st_list =[]
for t in range(T):
	st_list.append(input())

def make_palin(s):
    count = 0
    if len(s) == 0:
        return
    else:
        i = 0
        j = len(s)-1
        while(s[i] == s[j]) and i <= j:
            i += 1
            j -= 1
        if i >= j:
            return 0
        else:
            while i <= j:
                if(s[i] != s[j]):
                    count += 1
                    j -= 1
                else:
                    i += 1
                    j -= 1
            
    #print('not a palindrome')
    return count
    

for t in range(T):
	s1 = st_list[t]
	print(make_palin(s1))
