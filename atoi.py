
T = int(input())
st_list =[]
for t in range(T):
	st_list.append(input())

def atoi(s):
    sign = +1
    if(s[0] == '-'):
        sign = -1
        s = s[1:]
    if s.isdigit() is False:
        return -1
    else:
        sum = 0
        for i in range(len(s)):
            sum = sum * 10 + ord(s[i]) - ord('0')
        return sign*sum
    

for t in range(T):
	s1 = st_list[t]
	print(atoi(s1))
