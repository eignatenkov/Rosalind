# Given: A permutation of at most 12 symbols defining an ordered alphabet 𝒜 and a positive integer n (n≤4).
#
# Return: All strings of length at most n formed from 𝒜, ordered lexicographically. (Note: As in “Enumerating k-mers
#  Lexicographically”, alphabet order is based on the order in which the symbols are given.)
#
# Sample Dataset
#
# D N A
# 3

# Sample Output
#
# D
# DD
# DDD
# DDN
# DDA
# DN
# DND
# DNN
# DNA
# DA
# DAD
# DAN
# DAA
# N
# ND
# NDD
# NDN
# NDA
# NN
# NND
# NNN
# NNA
# NA
# NAD
# NAN
# NAA
# A
# AD
# ADD
# ADN
# ADA
# AN
# AND
# ANN
# ANA
# AA
# AAD
# AAN
# AAA


with open("/home/egor/Загрузки/rosalind_lexv.txt","r") as f:
    digs=f.readline().strip().split(' ')
    n=int(f.readline().strip())

digs.insert(0,"0")


for i in range(pow(len(digs),n)):
    curr=i
    digits=['']*n
    err=0
    for j in range(n):
        digits[n-j-1]=digs[curr % len(digs)]
        if j>0 and digits[n-j-1]=='0' and digits[n-j]!='0':
            err=1
            break
        curr = int(curr/len(digs))
    if err==0:
        print(''.join(digits).strip('0'))