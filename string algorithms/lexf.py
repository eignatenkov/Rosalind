__author__ = 'egor'

# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
#
# Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.
#
# Sample Dataset
#
# T A G C
# 2
#
# Sample Output
#
# TT
# TA
# TG
# TC
# AT
# AA
# AG
# AC
# GT
# GA
# GG
# GC
# CT
# CA
# CG
# CC

with open("/home/egor/Загрузки/rosalind_lexf.txt","r") as f:
    digs=f.readline().strip().split(' ')
    n=int(f.readline().strip())

for i in range(pow(len(digs),n)):
    curr=i
    digits=['']*n
    for j in range(n):
        digits[n-j-1]=digs[curr % len(digs)]
        curr = int(curr/len(digs))
    print(''.join(digits))
