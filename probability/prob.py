__author__ = 'egor'

# Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
#
# Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that
# a random string constructed with the GC-content found in A[k] will match s exactly.

with open("/home/egor/Загрузки/rosalind_prob.txt","r") as f:
    s=f.readline().strip()
    a=[float(x) for x in f.readline().strip().split(' ')]

result=[]

import math

for i in a:
    answer=1
    for j in s:
        if j=='G' or j=='C':
            answer*=i/2
        else:
            answer*=(1-i)/2
    result.append(math.log(answer,10))

print(' '.join(map(str,result)))