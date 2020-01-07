# recursive approach, takes long time
# make palindromes with the minimum number of insertions
import sys

T = int(input())
st_list =[]
for t in range(T):
	st_list.append(input())

def make_palin(s, l, h):
	# base cases
	if(l > h):
		return sys.maxsize
	if(l == h):
		return 0
	if(l == h - 1):
		return 0 if(s[l] == s[h]) else 1
	
	# if the first and last characters are the same 
	# then we do not need to insert anything for these two chars
	if(s[l] == s[h]):
		return make_palin(s, l+1, h -1)
	# if first and last char are not the same, then we need to insert
	# at least one char for them and then for the rest
	else:
		return (min(make_palin(s, l, h-1), make_palin(s, l+1, h)) + 1)
	
    

for t in range(T):
	s1 = st_list[t]
	print(make_palin(s1, 0, len(s1) - 1))
