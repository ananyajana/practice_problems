# after the fir4st person(kth from beginning) is killed, n-1 persons are left. 
# So we call josephus(n-1, k) to get the position with n-1 persons. Bu the 
# position returned by Josephus(n-1, k) will consider the position starting 
# from k%n + 1. Hence adjuistment in the position is required.

def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n-1, k) + k-1)%n + 1
