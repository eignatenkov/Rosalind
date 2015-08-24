__author__ = 'egor'


with open("/home/egor/Загрузки/rosalind_gbk.txt","r") as f:
    genus=f.readline().strip()
    first=f.readline().strip()
    last=f.readline().strip()

from Bio import Entrez
Entrez.email = "egor.ignatenkov@gmail.com"
query='"'+genus+'"[Organism] AND ("'+first+'"[PDAT] : "'+last+'"[PDAT])'
print(query)
handle = Entrez.esearch(db="nucleotide", term=query)
record = Entrez.read(handle)
print(record["Count"])