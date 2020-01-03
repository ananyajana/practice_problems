T = int(input())
st_list =[]
for t in range(T):
	st_list.append(input())

def value(r):
	if(r == 'I'):
		return 1
	if(r == 'V'):
		return 5
	if(r == 'X'):
		return 10
	if(r == 'L'):
		return 50
	if(r == 'C'):
		return 100
	if(r == 'D'):
		return 500
	if(r == 'M'):
		return 1000
	return -1

def convert_roman_to_decimal(s0):
	res = 0
	i = 0

	while(i < len(s0)):

		# getting value of symbol s[i]
		s1 = value(s0[i])

		if(i + 1 < len(s0)):
			# getting the value of symbol s0[i + 1]
			s2 = value(s0[i + 1])

			# comparing the two values
			if(s1 >= s2):
				res = res + s1
				i = i + 1
			else:
				res = res + s2 - s1
				i = i + 2
		else:
			res = res + s1
			i = i + 1
	print(res)
	return res

for t in range(T):
	#s1 = input()
	s1 = st_list[t]
	convert_roman_to_decimal(s1)
	
