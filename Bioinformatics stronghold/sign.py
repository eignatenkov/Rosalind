__author__ = 'egor'

# Problem
#
# A signed permutation of length n is some ordering of the positive integers {1,2,…,n} in which each integer is then provided with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For example, π=(5,−3,−2,1,4) is a signed permutation of length 5.
#
# Given: A positive integer n≤6.
#
# Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).
#
# Sample Dataset
#
# 2
#
# Sample Output
#
# 8
# -1 -2
# -1 2
# 1 -2
# 1 2
# -2 -1
# -2 1
# 2 -1
# 2 1

with open("/home/egor/Загрузки/rosalind_sign.txt","r") as f:
    n=int(f.readline().strip())

import itertools
import math

print(math.factorial(n)*pow(2,n))

line=[x for x in range(1,n+1)]

for perm in itertools.permutations(line):
    for i in range(pow(2,n)):
        sign=[2*((i>>k)&1)-1 for k in range(n)]
        readyline=[perm[j]*sign[j] for j in range(n)]
        print(' '.join(map(str,readyline)))