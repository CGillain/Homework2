# fibonacci series: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# fi(n) = fib(n-1) + fib(n-2)

n=10 # get the 10th fibo number

# first in the non recursive way (classical)

def fibo(n):
    if n==1 or n==2:
        return 1
    prev=1
    prev_prev=1

    for i in range(2, n):
        cur = prev + prev_prev
        prev_prev = prev
        prev= cur

    return cur
print("The 10th fibo is {}".format(fibo(10)))

# lets do fibonacci recursive
def rec_fibo(n):
    if n==1 or n==2:
        return 1

    return rec_fibo(n-1) + rec_fibo(n-2)

print("The 10th fibo is {}".format(rec_fibo(10)))