__author__ = 'egor'

# Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of
# corresponding symbols that differ in s and t.

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

# Return: The Hamming distance dH(s,t).

# Sample Dataset

# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT

# Sample Output

# 7

with open("/home/egor/Загрузки/rosalind_hamm.txt","r") as f:
    s=f.readline().strip()
    t=f.readline().strip()

count=0

for i in range(len(s)):
    if s[i]!=t[i]:
        count+=1

print(count)