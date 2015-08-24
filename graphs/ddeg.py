__author__ = 'egor'

# Given: A simple graph with n≤10^3 vertices in the edge list format.
#
# Return: An array D[1..n] where D[i] is the sum of the degrees of i's neighbors.
#
# See Figure 1 for visual example from the sample dataset.
#
# Sample Dataset
#
# 5 4
# 1 2
# 2 3
# 4 3
# 2 4
#
# Sample Output
#
# 3 5 5 5 0
#
# An adjacency list data structure may come in useful.

with open("/home/egor/Загрузки/rosalind_ddeg.txt","r") as f:
    info=[int(i) for i in f.readline().strip().split(' ')]
    n=info[0]
    deg=[[] for i in range(n)]
    ddeg=[0]*n
    for line in f:
        vertices=[int(i) for i in line.strip().split(' ')]
        deg[vertices[0]-1].append(vertices[1]-1)
        deg[vertices[1]-1].append(vertices[0]-1)

for i in range(len(deg)):
    ddeg[i]=sum([len(deg[j]) for j in deg[i]])

print(' '.join(map(str,ddeg)))