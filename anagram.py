T = int(input())
st_list =[]
tgt_list =[]
for t in range(T):
	x, y = input().split() 
	st_list.append(x)
	tgt_list.append(y)

def is_anagram(s, t):
	new_dict = dict()
	for i in range(len(s)):
		if s[i] in new_dict:
			new_dict[s[i]] += 1
		else:
			new_dict[s[i]] = 1

	#print(new_dict)
	for i in range(len(t)):
		if t[i] in new_dict:
			new_dict[t[i]] -= 1
		else:
			print("NO")
			return
	
	#print(new_dict)
	for key in new_dict:
		if new_dict[key] != 0:
			print("NO")
			return
	print("YES")
			

for t in range(T):
	#s1 = input()
	s1 = st_list[t]
	t1 = tgt_list[t]
	is_anagram(s1, t1)
