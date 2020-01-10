
T = int(input())
st_list =[]
tgt_list =[]
for t in range(T):
    x, y = input().split()
    st_list.append(x)
    tgt_list.append(y)

def strstr(s, t):
    for i in range(len(s)):
        k = 0
        idx = i
        #print('in loop :', idx)
        #print(s[i])
        #print(t[k])
        while s[i] == t[k] and i < (len(s) - 1) and k < (len(t) - 1):
            #print('inside while loop {}, {}'.format(s[i], t[k]))
            i += 1
            k += 1
        if k == len(t) - 1 and s[i] == t[k]:
            #print('before breaking:', idx)
            break;
    return idx
    

for t in range(T):
	s1 = st_list[t]
	t1 = tgt_list[t]
	print(strstr(s1, t1))
