''' we need to find the length of the maximum length of the chain possible
given the pairs. The constraint of forming the chain is that given the pairs
(a, b), (c, d) a valid chain is (a, b), (c, d) if b < c '''

import numpy as np

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def second_ele(self):
        return self.b

    def first_ele(self):
        return self.a

    def pair_print(self):
        print('({}, {})'.format(self.a, self.b))

# is the combination unique? possibly not
## is it dependent on how the pairs are formed? yes e.g. take a pati(1, 99)
# where 1 is the minimum number amongst all thenumbers in all the paris and 99
# is the maximum of all the numbers in all the pairs. In that case  the only
# chain the (1, 99) can be part of is itself i.e. chain length 1
# probably we need to construct a table where we can store the maximum length of 
# the chains

def max_chain_length(pair_arr, n):
    # let's create an array to hold the maximum chain length possible
    # starting from a particular pair. Since there are n pairs, the
    # array needs to hold n numbers
    # we initialize the array with 1 in each entry because the 
    # max chain length woul dbe at least 1 conidering the pair
    # to be the only element possible
    max_len_arr_all = [1] * n
    
    # now we need to find the next optimum pairs for each
    # of these pairs. The optimum pair would be the one which keeps
    # the current maximum oof all these pairs in this chain as small
    # as possible e.g. if (a, b), (c, d) are prt of an optimum chain
    # then d needs to be as small as possible, so that there is higher
    # chance of fitting other numbers
    # is this problem the same as scheduling problem? yes
    # but we will use dynamic programming to solve it this time
    # with the help of a memoization table

    for i in range(1, n):
        for j in range(i):
            # if the current max chain length for this element is less
            # than the max_chain length formed by including the next smaller element
            # then update the chain length, we also need to check if the first elem of the
            # current elem is greater the second elem of the next smaller elem
            if max_len_arr_all[i] < max_len_arr_all[j] + 1: 
                print('there is a chance of update')
                f_ele = pair_arr[i].first_ele()
                s_ele = pair_arr[j].second_ele()
                print('f_ele:{}. s_ele:{}'.format(f_ele, s_ele))
                if f_ele > s_ele:
                    print('update')
                    max_len_arr_all[i] = max_len_arr_all[j] + 1

    print(max_len_arr_all)
    max_elem = np.amax(np.array(max_len_arr_all))
    return max_elem



def second_elem(pair):
    return pair.second_ele()

def first_elem(pair):
    return pair.first_ele()
    
pair = [Pair(5, 24) , Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90)]
print('before sorting:')
for i in range(len(pair)):
    pair[i].pair_print()
pair.sort(key=second_elem)
print('after sorting:')
for i in range(len(pair)):
    pair[i].pair_print()

N = len(pair)
print(max_chain_length(pair, N))
