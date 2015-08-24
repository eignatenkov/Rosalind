__author__ = 'egor'

# Given: Positive integers n≤40 and k≤5.

# Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each
# generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).


def fibo(n,k):
    if n == 1:
        return 1;
    if n == 2:
        return 1;
    else:
        return fibo(n-1,k)+k*fibo(n-2,k)

with open("/home/egor/Загрузки/rosalind_fib.txt","r") as f:
    coeffs=[int(x) for x in f.readline().strip().split(' ')]

print(fibo(coeffs[0],coeffs[1]))
