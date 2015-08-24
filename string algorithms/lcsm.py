__author__ = 'egor'

# A common substring of a collection of strings is a substring of every member of the collection. We say that a common
# substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is
# a common substring of "ACGTACGT" and "AACCGGTATA", but it is not as long as possible; in this case, "GTA" is a longest
# common substring of "ACGTACGT" and "AACCGTATA".
#
# Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest
# common substrings of "AACC" and "CCAA".
#
# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
#
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single
# solution.)
#
# Sample Dataset
#
# >Rosalind_1
# GATTACA
# >Rosalind_2
# TAGACCA
# >Rosalind_3
# ATACA
#
# Sample Output
#
# AC

import time

strings=[]

with open("/home/egor/Загрузки/rosalind_lcsm.txt","r") as f:
    f.readline()
    curr=''
    line=f.readline().strip()
    while line!='':
        if line[0]==">":
            strings.append(curr)
            curr=''
        else:
            curr+=line
        line=f.readline().strip()

# function that returns all substring of length k

minstring=min(strings,key=len)
minlen=len(minstring)
lcsm=''

begin=time.perf_counter()

for i in range(minlen):
    if lcsm!='':
        break
    for start in range(i+1):
        j=minstring[start:start+minlen-i+1]
        if all(k.find(j) >=0 for k in strings):
            lcsm=j
            break

end=time.perf_counter()
print(lcsm)
print(end-begin)