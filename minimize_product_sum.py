import numpy as np

def get_minimum_product_sum(a, b, n):
    # sort A and B so that minimum and maximum
    # value can easily be fetched.
    A.sort()
    B.sort()

    # Multiplying minimum value of A and maximum value o fB
    result = 0
    for i in range(n):
        result += (A[i] * B[n - i - 1])

    return result

# code to invoke
A = [3, 1, 1]
B = [6, 5, 4]
n = len(A)
print(get_minimum_product_sum(A, B, n))


