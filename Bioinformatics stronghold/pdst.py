__author__ = 'egor'

# Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given in FASTA
# format.
#
# Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is
# allowed an absolute error of 0.001.
#
# Sample Dataset
#
# >Rosalind_9499
# TTTCCATTTA
# >Rosalind_0942
# GATTCATTTC
# >Rosalind_6568
# TTTCCATTTT
# >Rosalind_1833
# GTTCCATTTA
#
# Sample Output
#
# 0.00000 0.40000 0.10000 0.10000
# 0.40000 0.00000 0.40000 0.30000
# 0.10000 0.40000 0.00000 0.20000
# 0.10000 0.30000 0.20000 0.00000

strings=[]

with open("/home/egor/Загрузки/rosalind_pdst.txt","r") as f:
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

def pdist(s,t):
    count=0
    for i in range(len(s)):
        if s[i]!=t[i]:
            count+=1
    return count/len(s)

matrix=[[0 for x in range(len(strings))] for x in range(len(strings))]

for i in range(len(strings)):
    for j in range(len(strings)):
        matrix[i][j]=pdist(strings[i],strings[j])
    print(' '.join(map(str,matrix[i])))
