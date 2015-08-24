__author__ = 'egor'

# Problem
#
#
# Figure 3. The graph from the dataset
# In an undirected graph, the degree d(u) of a vertex u is the number of neighbors u has, or equivalently, the number of
# edges incident upon it.
#
# Given: A simple graph with n≤103 vertices in the edge list format.
#
# Return: An array D[1..n] where D[i] is the degree of vertex i.
#
# Sample Dataset
#
# 6 7
# 1 2
# 2 3
# 6 3
# 5 6
# 2 5
# 2 4
# 4 1
#
# Sample Output
#
# 2 4 2 2 2 2

with open("/home/egor/Загрузки/rosalind_deg.txt","r") as f:
    info=[int(i) for i in f.readline().strip().split(' ')]
    n=info[0]
    deg=[0]*n
    for line in f:
        vertices=[int(i) for i in line.strip().split(' ')]
        deg[vertices[0]-1]+=1
        deg[vertices[1]-1]+=1

print (' '.join(map(str,deg)))