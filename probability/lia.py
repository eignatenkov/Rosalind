__author__ = 'egor'

# Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
#
# Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
#

import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

with open("/home/egor/Загрузки/rosalind_lia.txt","r") as f:
    data=[int(i) for i in f.readline().strip().split(' ')]

answer=0
size=pow(2,data[0])
for i in range(data[1],size+1):
    answer+=nCr(size,i)*pow(.25,i)*pow(.75,size-i)

print(answer)