__author__ = 'egor'
# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example,
# the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is
# called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some
# labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label
# of the next string.

# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes
# a four-digit code between 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows
# for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error
# below.

#Sample Dataset

# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT

# Sample Output

# Rosalind_0808
# 60.919540

with open("/home/egor/Загрузки/rosalind_gc.txt","r") as f:
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

def gc_count(name):
    count=0
    for i in rslnd[name]:
        if i=="G" or i=="C":
            count+=1
    return 100*count/len(rslnd[name])

dnakeys=list(rslnd.keys())

max=dnakeys[0]

for name in rslnd:
    if gc_count(name)>gc_count(max):
        max = name

print(max)
print(gc_count(max))