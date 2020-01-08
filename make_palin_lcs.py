# recursive approach, takes long time
# make palindromes with the minimum number of insertions

T = int(input())
st_list =[]
for t in range(T):
	st_list.append(input())

def Min(a, b):
	return min(a, b)	

def lcs(x, y, m, n):
	L = [[0 for i in range(m + 1)] for j in range(n + 1)]
	for i in range(m + 1):
		for j in range(n + 1):
			if i == 0 or j == 0:
				L[i][j] = 0
			elif x[i - 1] == y[j - 1]:
				L[i][j] = L[i - 1][j - 1] + 1
			else:
				L[i][j] = max(L[i - 1][j], L[i][j - 1])
	
	# L[m][n] contains the length of LCS for x[0...n-1] and y[0...m-1]
	return L[m][n]

def reverse_string(s):
	rev = ''
	for i in s:
		rev = i + rev
	return rev

def find_min_insertion_lcs(s, n):
	rev = reverse_string(s)

	return (n - lcs(s, rev, n, n))

for t in range(T):
	s1 = st_list[t]
	print(find_min_insertion_lcs(s1, len(s1)))
