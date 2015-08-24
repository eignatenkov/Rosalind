# Problem
#
# For a collection of strings, a larger string containing every one of the smaller strings as a substring is called
# a superstring.
#
# By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate
# chromosome.
#
# Given: At most 50 DNA strings whose length does not exceed 1 kbp in FASTA format (which represent reads deriving from
# the same strand of a single linear chromosome).
#
# The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire
# chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.
#
# Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
#
# Sample Dataset
#
# >Rosalind_56
# ATTAGACCTG
# >Rosalind_57
# CCTGCCGGAA
# >Rosalind_58
# AGACCTGCCG
# >Rosalind_59
# GCCGGAATAC

# Sample Output
#
# ATTAGACCTGCCGGAATAC

substrings=[]

with open("/home/egor/Загрузки/rosalind_long.txt","r") as f:
    f.readline()
    curr=''
    line=f.readline().strip()
    while line!='':
        if line[0]==">":
            substrings.append(curr)
            curr=''
        else:
            curr+=line
        line=f.readline().strip()
    substrings.append(curr)

def shortestSuperstring(seqs):
    left=[i for i in range(1,len(seqs))]
    candidate=seqs[0]
    while len(left)>0:
        for i in left:
            before=True
            after=True
            for j in reversed(range(int(len(seqs[i])/2),len(seqs[i]))):
                if after:
                    if candidate.endswith(seqs[i][:j]):
                        candidate=candidate+seqs[i][j:]
                        left.remove(i)
                        after=False
                if before:
                    if seqs[i].endswith(candidate[:j]):
                        candidate=seqs[i][:-j]+candidate
                        left.remove(i)
                        before=False
    return candidate

print(shortestSuperstring(substrings))