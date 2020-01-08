# recursive approach, takes long time
# make palindromes with the minimum number of insertions

T = int(input())
st_list =[]
for t in range(T):
	st_list.append(input())

def Min(a, b):
	return min(a, b)	

def find_min_insertion(s, n):
	# create a memoization table
	table = [[0 for i in range(n)] for i in range(n)]
	l, h, gap = 0, 0, 0

	# fill in the table
	for gap in range(1, n):
		l = 0
		for h in range(gap, n):
			if s[l] == s[h]:
				table[l][h] = table[l+1][h-1]
			else:
				table[l][h] = (Min(table[l][h-1], table[l+1][h]) +1)
			l += 1
	# return the min number of insertions for s[0...n-1]
	return table[0][n - 1]

for t in range(T):
	s1 = st_list[t]
	print(find_min_insertion(s1, len(s1)))
