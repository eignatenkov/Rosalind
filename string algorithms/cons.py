__author__ = 'egor'
# Problem
#
# A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given
# a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.
#
# Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in
# which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents
# the number of times that C occurs in the jth position, and so on (see below).
#
# A consensus string c is a string of length n formed from our collection by taking the most common symbol at each
# position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of
# the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus
# strings.
#
# DNA Strings
# A T C C A G C T
# G G G C A A C T
# A T G G A T C T
# A A G C A A C C
# T T G G A A C T
# A T G C C A T T
# A T G G C A C T

# Profile
# A   5 1 0 0 5 5 0 0
# C   0 0 1 4 2 0 6 1
# G   1 1 6 3 0 1 0 0
# T   1 5 0 0 0 1 1 6

# Consensus	A T G C A A C T

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
#
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then
# you may return any one of them.)
#
# Sample Dataset
#
# >Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# >Rosalind_3
# ATGGATCT
# >Rosalind_4
# AAGCAACC
# >Rosalind_5
# TTGGAACT
# >Rosalind_6
# ATGCCATT
# >Rosalind_7
# ATGGCACT
# Sample Output
#
# ATGCAACT
# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6

with open("/home/egor/Загрузки/rosalind_cons.txt","r") as f:
    rslnd={}
    line=f.readline().strip()
    while line!='':
        name="".join(list(line)[1:len(line)])
        line=f.readline().strip()
        while line!='' and line[0]!=">":
            if name not in rslnd:
                rslnd[name]=line
            else:
                rslnd[name]+=line
            line=f.readline().strip()

length=len(list(rslnd.values())[0])
profile=[[0]*(length+1) for i in range(4)]

profile[0][0]="A:"
profile[1][0]="C:"
profile[2][0]="G:"
profile[3][0]="T:"

for name in rslnd:
    for i in range(len(rslnd[name])):
        if rslnd[name][i]=="A":
            profile[0][i+1]+=1
        else:
            if rslnd[name][i]=="C":
                profile[1][i+1]+=1
            else:
                if rslnd[name][i]=="G":
                    profile[2][i+1]+=1
                else:
                    profile[3][i+1]+=1

cons=''
for i in range(length):
    a=[profile[j][i+1] for j in range(4)]
    m=max(a)
    maxs=[j for j, k in enumerate(a) if k==m]
    if maxs[0]==0:
        cons+="A"
    else:
        if maxs[0]==1:
            cons+="C"
        else:
            if maxs[0]==2:
                cons+="G"
            else:
                cons+="T"

print(cons)

for i in range(4):
    print(' '.join(map(str, profile[i])))