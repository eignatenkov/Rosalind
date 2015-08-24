__author__ = 'egor'

# After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons
# to form a new string ready for translation.
#
# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are
# given in FASTA format.
#
# Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will
# exist for the dataset provided.)
#
# Sample Dataset
#
# >Rosalind_10
# ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
# >Rosalind_12
# ATCGGTCGAA
# >Rosalind_15
# ATCGGTCGAGCGTGT
#
# Sample Output
#
# MVYIADKQHVASREAYGHMFKVCA

def dna2rna(str):
    s=list(str)
    for i in range(len(s)):
        if s[i]=="T":
            s[i]="U"
    return ''.join(s)

def rna2prot(rna):
    codon={"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V", "UUA": "L",
            "CUA": "L", "AUA": "I", "GUA": "V", "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V", "UCU": "S", "CCU": "P",
            "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A", "UCA": "S", "CCA": "P", "ACA": "T",
            "GCA": "A", "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
            "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
            "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E", "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
            "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G", "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
            "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}
    protein=''
    for i in range(int(len(rna)/3)):
        name=rna[i*3:i*3+3]
        if codon[name]=="Stop":
            break
        else:
            protein+=codon[name]
    return protein

def rmintron(dna,introns):
    start=0
    while start>=0:
        for i in introns:
            start=dna.find(i)
            if start>=0:
                dna=dna[:start]+dna[start+len(i):]
                break
    return dna


strings=[]

with open("/home/egor/Загрузки/rosalind_splc.txt","r") as f:
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

dna=strings[0]
strings.pop(0)

print(rna2prot(dna2rna(rmintron(dna,strings))))