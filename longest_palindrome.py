
str1 = 'fdghfhdbacabk'
str2 = 'abcida'

len1 = len(str1)
#print(len1)

match = False

longest_len = 0
longest_i = 0
longest_j = 0

for i in range(0, len1 - 1):
	for j in range(i+1, len1):
		longest_len = 0
		match = False
		for k in range(0, j // 2):
			if (str1[i + k] == str1[j - k]):
				#print(str1[i + k])
				match = True
				
			else:
				match = False
				break;
		if(match is True):
			if (longest_len < (j - i + 1)):
				longest_len = j - i + 1
				longest_i = i
				longest_j = j + 1

print("longest len palindrome :", str1[longest_i:longest_j])	
#print("longest len :", longest_len)	
#print("longest i :", longest_i)	
#print("longest j :", longest_j)	

			
