''' We are given two number N ad S. Our task is to find the biggest number
which has N digits and whose sum of digits is S'''

''' The biggest number that can be formed using N digits is N consecutive 9s.
In that case the sum of digits would be N*9. But we need to match the sum
S and hence we can start putting 9s from the most important bits and where
the current sum of digits falls less than 9, we can fill that digits with
that difference. A key observation is that all the digits except the lsb
will be 9'''

import numpy as np

def largest_number_possible(n, s):
    num = 0
    while s != 0 and n!= 0:
        if s > 9:
            num = num*10 + 9
            s = s - 9
            n = n - 1
        else:
            num = num*10 + s
            s = 0
            n = n - 1

    return num

# this is not possible hence we get the largest number possiblw with the digits sum as 18
N = 2
S = 20
print(largest_number_possible(N, S))
N = 3
S = 20
print(largest_number_possible(N, S))

        

