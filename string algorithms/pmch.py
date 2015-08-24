__author__ = 'egor'

# Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number
# of occurrences of 'C' as 'G'.
#
# Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
#
# Sample Dataset
#
# >Rosalind_23
# AGCUAGUCAU
#
# Sample Output
#
# 12

with open("/home/egor/Загрузки/rosalind_pmch.txt","r") as f:
    f.readline()
    string=''
    for line in f:
        string+=line.strip()

result=[0]*4

for i in range(len(string)):
    if string[i]=="A":
        result[0]+=1
    if string[i]=="C":
        result[1]+=1
    if string[i]=="G":
        result[2]+=1
    if string[i]=="U":
        result[3]+=1

import math

print(math.factorial(result[0])*math.factorial(result[1]))