T = int(input())
st_list =[]
for t in range(T):
	st_list.append(input())

def recDelAdjDup(st):
	#print('st for this call ', st)
	last_rem = ''
	if len(st) == 1 or len(st) == 0:
		return st
	elif st[0] == st[1]:
		#print('here')
		while len(st) > 1 and st[0] == st[1]:
			#print('here2')
			#print('st before', st)
			st = st[1:]
			last_rem = st[0]
			#print('st after', st)
		if last_rem == st[0]:
			st = st[1:]
		return recDelAdjDup(st)
	else:
		s0 = st[0]
		return s0 + recDelAdjDup(st[1:])
		
	


for t in range(T):
	#s1 = input()
	s1 = st_list[t]
	s1 = recDelAdjDup(s1)
	print(s1)
