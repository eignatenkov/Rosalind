__author__ = 'egor'

#Problem

#A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

#An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

#Given: A DNA string s of length at most 1000 nt.

#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

#Sample Dataset

#AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

#Sample Output

#20 12 17 21

with open("/home/egor/Загрузки/rosalind_dna.txt","r") as f:
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
    if string[i]=="T":
        result[3]+=1

answer=''

for i in result:
    answer+=str(i)+' '

print(answer.strip())