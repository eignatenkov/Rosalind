__author__ = 'egor'

# A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.
#
# Given: A positive integer n≤7.
#
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
#
# Sample Dataset
#
# 3
#
# Sample Output
#
# 6
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

with open("/home/egor/Загрузки/rosalind_perm.txt","r") as f:
    n=int(f.readline().strip())

import math
import itertools

print(math.factorial(n))

line=[x for x in range(1,n+1)]

for i in itertools.permutations(line):
    print(' '.join(map(str,i)))