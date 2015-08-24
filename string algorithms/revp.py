__author__ = 'egor'

# A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse
# palindrome because its reverse complement is GCATGC. See Figure 2.
#
# Given: A DNA string of length at most 1 kbp in FASTA format.
#
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may
# return these pairs in any order.
#
# Sample Dataset
#
# >Rosalind_24
# TCAATGCATGCGGGTCTATATGCAT
#
# Sample Output
#
# 4 6
# 5 4
# 6 6
# 7 4
# 17 4
# 18 4
# 20 6
# 21 4

def revc(s):
    answer = []
    for i in range(len(s)):
        ind=len(s)-1-i
        if s[ind] == "A":
            answer.append("T")
        else:
            if s[ind]=="T":
                answer.append("A")
            else:
                if s[ind]=="C":
                    answer.append("G")
                else:
                    answer.append("C")

    return ("".join(answer))

with open("/home/egor/Загрузки/rosalind_revp.txt","r") as f:
    dna=''
    f.readline()
    for line in f:
        dna+=line.strip()

palindroms=[]

for i in range(len(dna)):
    for j in range(4,14,2):
        if i+j<=len(dna):
            if dna[i:i+j]==revc(dna[i:i+j]):
                palindroms.append([i+1,j])

for i in palindroms:
    print(' '.join(map(str,i)))