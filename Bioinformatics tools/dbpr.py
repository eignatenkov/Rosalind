__author__ = 'egor'

# Given: The UniProt ID of a protein.
#
# Return: A list of biological processes in which the protein is involved (biological processes are found in a
# subsection of the protein's "Gene Ontology" (GO) section).
#
# Sample Dataset
#
# Q5SLP9
#
# Sample Output
#
# DNA recombination
# DNA repair
# DNA replication

with open("/home/egor/Загрузки/rosalind_dbpr.txt","r") as f:
    prot=f.readline().strip()

from Bio import ExPASy
from Bio import SwissProt

handle=ExPASy.get_sprot_raw(prot)
record = SwissProt.read(handle)

processes=[x[2][2:] for x in record.cross_references if x[0]=='GO' and x[2][:2]=='P:']

for x in processes:
    print(x)