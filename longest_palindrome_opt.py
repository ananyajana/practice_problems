T = int(input())
st_list =[]
for t in range(T):
	st_list.append(input())

def longestPal(st):
	n = len(st)
	#creta an empty table with all entries as 0
	# if an entry (i, j) is True then st[i:j] is a palindrome, else not
	table = [[0 for x in range(n)] for y in range(n)]
	maxLength = 1
	i = 0

	# all diagonal entries are palindromes of length 1
	while( i < n):
		table[i][i] = True
		i = i + 1
	
	# check for substring of length 2
	start = 0
	i = 0
	while i < n - 1:
		if(st[i] == st[i + 1]):
			table[i][i + 1] = True
			if maxLength == 1:
				start = i
				maxLength = 2
		i = i + 1
	
	# check for lengths greater than 2
	# k is the length of substring
	k = 3
	while k <= n:
		# Fix the starting index
		i = 0;
		while i < n - k + 1:
			# get the ending index of the substring
			# starting from i and of length k
			j = i + k -1

			# checking for the substring from ith index to jth
			# index iff st[i + 1][j - 1] = True and
			# st[i] == st[j]

			if(table[i + 1][j - 1] and st[i] == st[j]):
				table[i][j] = True

				if k > maxLength:
					start = i
					maxLength = k
			i = i + 1
		k = k + 1
	print(st[start: start + maxLength])



for t in range(T):
	#s1 = input()
	s1 = st_list[t]
	longestPal(s1)
