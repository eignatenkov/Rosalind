__author__ = 'egor'

# Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were
# generated with a single-nucleotide error. For each read s in the dataset, one of the following applies:
#
# s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
# s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one
# correct read in the dataset (or its reverse complement).

# Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol
# substitution, and you may return the corrections in any order.)
#
# Sample Dataset
#
# >Rosalind_52
# TCATC
# >Rosalind_44
# TTCAT
# >Rosalind_68
# TCATC
# >Rosalind_28
# TGAAA
# >Rosalind_95
# GAGGA
# >Rosalind_66
# TTTCA
# >Rosalind_33
# ATCAA
# >Rosalind_21
# TTGAT
# >Rosalind_18
# TTTCC
#
# Sample Output
#
# TTCAT->TTGAT
# GAGGA->GATGA
# TTTCC->TTTCA

strings=[]

with open("/home/egor/Загрузки/rosalind_corr.txt","r") as f:
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


def rev(s):
    answer=''
    for i in range(len(s)):
        ind=len(s)-1-i
        if s[ind] == "A":
            answer+="T"
        else:
            if s[ind]=="T":
                answer+="A"
            else:
                if s[ind]=="C":
                    answer+="G"
                else:
                    answer+="C"
    return answer

def hamm(s,t):
    count=0
    for i in range(len(s)):
        if s[i]!=t[i]:
            count+=1
    return count

def ham0(a, alist):
    answer=0
    reva=rev(a)
    for b in alist:
        if hamm(a,b)==0 or hamm(reva,b)==0:
            answer+=1
            if answer>1:
                return True
    return False

def ham1(a, alist):
    reva=rev(a)
    for b in alist:
        if hamm(a,b)==1:
            return b
        elif hamm(reva,b)==1:
            return rev(b)
    return -1


goodstrings=[i for i in strings if ham0(i,strings)]
badstrings=list(set(strings)-set(goodstrings))
for a in badstrings:
    print(a+'->'+ham1(a,goodstrings))
