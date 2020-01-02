T = int(input())
st_list =[]
for t in range(T):
	st_list.append(input())

def toList(string): 
    x = [] 
    for i in string: 
        x.append(i) 
    return x 
  
def toString(x): 
    return ''.join(x) 


def recDelAdjDup(st, last_rem):
    #print('st for this call ', st)
    if len(st) == 1 or len(st) == 0:
        return toString(st)
    elif st[0] == st[1]:
        #print('here')
        # while the first two characters match delete those
        #last_rem = ord(st[0])
        while len(st) > 1 and st[0] == st[1]:
            st = st[1:]
        st = st[1:]
        return toString(recDelAdjDup(st, last_rem))
    # the first two characters do not match
    # hence we are going to check recursively in the string if the other characters match
    new_str = recDelAdjDup(st[1:], last_rem)
    # check if the first character of the old string matches with the first chracter of the new string
    if len(new_str) != 0 and st[0] == new_str[0]:
        last_rem = ord(st[0])
        return toString((new_str[1:]))

    #if the string becomes empty and the last_removed character is the same as the first character then
    # remove the first character as well and return an empty string
    if last_rem == ord(st[0]) and len(new_st) == 0:
        return new_str

    # if the first character of the string doesn't match with that of new_str then append first character
    # at the beginning and return that string
    return toString((st[0] + new_str))
		
	


for t in range(T):
	#s1 = input()
	s1 = st_list[t]
	s1 = recDelAdjDup(toList(s1), 0)
	print(s1)
