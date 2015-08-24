__author__ = 'egor'

# A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously) in
# the string (e.g., ACG is a subsequence of TATGCTAAGATC). The indices of a subsequence are the positions in the string
# at which the symbols of the subsequence appear; thus, the indices of ACG in TATGCTAAGATC can be represented by
# (2, 5, 9).
#
# As a substring can have multiple locations, a subsequence can have multiple collections of indices, and the same index
# can be reused in more than one appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT in 8
# different ways.
#
# Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
#
# Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions
# exist, you may return any one.
#
# Sample Dataset
#
# >Rosalind_14
# ACGTACGTGACG
# >Rosalind_18
# GTA
# Sample Output
#
# 3 8 10
strings=[]

with open("/home/egor/Загрузки/rosalind_sseq.txt","r") as f:
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
    strings.append(curr)

big=strings[0]
small=strings[1]

pos=[]
bigindex=0

for i in small:
    if bigindex==len(big):
        break
    while big[bigindex]!=i:
        bigindex+=1
        if bigindex==len(big):
            break
    if big[bigindex]==i:
        pos.append(bigindex+1)
        bigindex+=1

print(' '.join(map(str,pos)))