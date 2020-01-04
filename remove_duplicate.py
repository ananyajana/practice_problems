T = int(input())
st_list =[]
for t in range(T):
	st_list.append(input())

def remove_duplicate(s):
    new_dict = {}
    res = ''
    for i in range(len(s)):
        if s[i] not in new_dict:
            new_dict[s[i]] = 1
            res = res + s[i]

    print(res)

for t in range(T):
	s1 = st_list[t]
	remove_duplicate(s1)
