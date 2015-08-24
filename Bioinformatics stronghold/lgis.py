__author__ = 'egor'

# Given: A positive integer n≤10000 followed by a permutation π of length n.
#
# Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
#
# Sample Dataset
#
# 5
# 5 1 4 2 3
#
# Sample Output
#
# 1 2 3
# 5 4 2

import math

with open("/home/egor/Загрузки/rosalind_lgis.txt","r") as f:
    size=int(f.readline().strip())
    perm=[int(x) for x in f.readline().strip().split(' ')]
    newperm=[-1*x for x in perm]

def lgis(string):
    p=[0]*size
    m=[0]*(size+1)

    l=0

    for i in range(size):
        lo=1
        hi=l
        while lo<=hi:
            mid=math.ceil((lo+hi)/2)
            if string[m[mid]]<string[i]:
                lo = mid+1
            else:
                hi = mid-1
        newL = lo
        p[i]=m[newL-1]
        m[newL] = i
        if newL>l:
            l=newL

    s=[0]*l
    k=m[l]
    for i in reversed(range(l)):
        s[i]=string[k]
        k=p[k]
    return s

print(' '.join(map(str,lgis(perm))))
print(' '.join(map(str,[-1*x for x in lgis(newperm)])))