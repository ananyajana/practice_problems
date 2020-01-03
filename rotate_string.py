T = int(input())
st_list =[]
tgt_list =[]
for t in range(T):
	st_list.append(input())
	tgt_list.append(input())


def is_rotation(s, t):
	new_s = s
	# rotate clockwise and check
	new_s = new_s[2:] + new_s[0:2]
	#print(new_s)
	if(new_s == t):
		print('1')
		return
	
	#rotate anticlockwise and check
	new_s = s
	new_s = new_s[len(s) - 2:] + new_s[:len(s) - 2]
	if(new_s == t):
		print('1')
		return
	print('0')

for t in range(T):
	#s1 = input()
	s1 = st_list[t]
	t1 = tgt_list[t]
	is_rotation(s1, t1)
	
