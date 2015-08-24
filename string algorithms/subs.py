__author__ = 'egor'

# Given: Two DNA strings s and t (each of length at most 1 kbp).

# Return: All locations of t as a substring of s.

# Sample Dataset

#GATATATGCATATACTT
#ATAT

#Sample Output

#2 4 10

with open("/home/egor/Загрузки/rosalind_subs.txt","r") as f:
    big=f.readline().strip()
    small=f.readline().strip()

pos=[]

for i in range(len(big)):
    if big[i:(i+len(small))]==small:
        pos.append(i+1)

print(' '.join(map(str,pos)))