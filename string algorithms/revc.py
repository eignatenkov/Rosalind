__author__ = 'egor'

#In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

#The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

#Given: A DNA string s of length at most 1000 bp.

#Return: The reverse complement sc of s.

#Sample Dataset

#AAAACCCGGT

#Sample Output

#ACCGGGTTTT

with open("/home/egor/Загрузки/rosalind_revc.txt","r") as f:
    s=list(f.readline().strip())

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

print("".join(answer))