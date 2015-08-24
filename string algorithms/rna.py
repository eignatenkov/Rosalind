__author__ = 'egor'

#An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

#Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

#Given: A DNA string t having length at most 1000 nt.

#Return: The transcribed RNA string of t.

#Sample Dataset

#GATGGAACTTGACTACGTAAATT

#Sample Output

#GAUGGAACUUGACUACGUAAAUU

with open("/home/egor/Загрузки/rosalind_rna.txt","r") as f:
    s=list(f.readline().strip())

for i in range(len(s)):
    if s[i]=="T":
        s[i]="U"

print("".join(s))