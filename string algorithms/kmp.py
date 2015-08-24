__author__ = 'egor'

# Problem
#
# A prefix of a length n string s is a substring s[1:j]; a suffix of s is a substring s[k:n].
#
# The failure array of s is an array P of length n for which P[k] is the length of the longest substring s[j:k] that is
# equal to some prefix s[1:k−j+1], where j cannot equal 1 (otherwise, P[k] would always equal k). By convention, P[1]=0.
#
# Given: A DNA string s (of length at most 100 kbp) in FASTA format.
#
# Return: The failure array of s.
#
# Sample Dataset
#
# >Rosalind_87
# CAGCATGGTATCACAGCAGAG
#
# Sample Output
#
# 0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0

with open("/home/egor/Загрузки/rosalind_kmp.txt","r") as f:
    f.readline()
    string=''
    for line in f:
        string+=line.strip()

failure=[0]*len(string)

for k in range(1,len(string)):
    for j in range(k-failure[k-1],k+1):
        if string[j:k+1]==string[:k-j+1]:
            failure[k]=(k-j+1)
            break

print(' '.join(map(str,failure)))