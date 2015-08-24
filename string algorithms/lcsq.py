__author__ = 'egor'

# Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.
#
# Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)
#
# Sample Dataset
#
# >Rosalind_23
# AACCTTGG
# >Rosalind_64
# ACACTGTGA
#
# Sample Output
#
# AACTGG

strings=[]

with open("/home/egor/Загрузки/rosalind_lcsq.txt","r") as f:
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

def lcstable(x,y):
    c=[[0 for i in range(len(y)+1)] for j in range(len(x)+1)]
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i]==y[j]:
                c[i+1][j+1]=c[i][j]+1
            else:
                c[i+1][j+1]=max(c[i+1][j],c[i][j+1])
    return c

def backtrack(c,x,y,i,j):
    if i==0 or j==0:
        return ''
    elif x[i-1]==y[j-1]:
        return backtrack(c,x,y,i-1,j-1)+x[i-1]
    else:
        if c[i][j-1]>c[i-1][j]:
            return backtrack(c,x,y,i,j-1)
        else:
            return backtrack(c,x,y,i-1,j)

import sys
sys.setrecursionlimit(10000)

print(backtrack(lcstable(strings[0],strings[1]),strings[0],strings[1],len(strings[0]),len(strings[1])))