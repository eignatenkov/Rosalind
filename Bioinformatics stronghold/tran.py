__author__ = 'egor'

# For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of
# the total number of transitions to the total number of transversions, where symbol substitutions are inferred from
# mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).
#
# Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
#
# Return: The transition/transversion ratio R(s1,s2).
#
# Sample Dataset
#
# >Rosalind_0209
# GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
# AGTACGGGCATCAACCCAGTT
# >Rosalind_2200
# TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
# GGTACGAGTGTTCCTTTGGGT

# Sample Output
#
# 1.21428571429

strings=[]

with open("/home/egor/Загрузки/rosalind_tran.txt","r") as f:
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

purines=['A','G']
pyrimidines=['C','T']
transitions=0
transversions=0

for i in range(len(strings[0])):
    if strings[0][i]!=strings[1][i]:
        if strings[0][i] in purines and strings[1][i] in purines or strings[0][i] in pyrimidines and strings[1][i] in pyrimidines:
            transitions+=1
        else:
            transversions+=1

print(transitions/transversions)