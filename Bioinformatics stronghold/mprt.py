__author__ = 'egor'

# Problem
#
# To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means
# "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as
# N{P}[ST]{P}.
#
# You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt
# database, by inserting the ID number into http://www.uniprot.org/uniprot/uniprot_id
# Alternatively, you can obtain a protein sequence in FASTA format by following
#
# http://www.uniprot.org/uniprot/uniprot_id.fasta
# For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.
#
# Given: At most 15 UniProt Protein Database access IDs.
#
# Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of
# locations in the protein string where the motif can be found.
#
# Sample Dataset
#
# A2Z669
# B5ZC00
# P07204_TRBM_HUMAN
# P20840_SAG1_YEAST

# Sample Output
#
# B5ZC00
# 85 118 142 306 395
# P07204_TRBM_HUMAN
# 47 115 116 382 409
# P20840_SAG1_YEAST
# 79 109 135 248 306 348 364 402 485 501 614

import urllib.request

def readprot(file):
    str=''
    for i in file.split('\n')[1:]:
        str=str+i.strip()
    return str


def glycocheck(protein):
    ind=[]
    import regex as re
    matches=re.finditer('N[^P][ST][^P]',protein, overlapped=True)
    for i in matches:
        ind.append(i.start()+1)
    return ind


with open("/home/egor/Загрузки/rosalind_mprt.txt","r") as f:
    for line in f:
        accessID=line.strip()
        data = urllib.request.urlopen("http://www.uniprot.org/uniprot/"+accessID+".fasta").read().decode('utf-8')
        result=glycocheck(readprot(data))
        if len(result)>0:
            print(line+' '.join(map(str,result)))