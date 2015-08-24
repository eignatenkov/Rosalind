__author__ = 'egor'

# The task is to use depth-first search to compute the number of connected components in a given undirected graph.
#
# Given: A simple graph with n≤10^3 vertices in the edge list format.
#
# Return: The number of connected components in the graph.
#
# Sample Dataset
#
# 12 13
# 1 2
# 1 5
# 5 9
# 5 10
# 9 10
# 3 4
# 3 7
# 3 8
# 4 8
# 7 11
# 8 11
# 11 12
# 8 12
#
# Sample Output
#
# 3

with open("/home/egor/Загрузки/rosalind_cc.txt","r") as f:
    info=[int(i) for i in f.readline().strip().split(' ')]
    n=info[0]
    deg=[[] for i in range(n)]
    for line in f:
        vertices=[int(i) for i in line.strip().split(' ')]
        deg[vertices[0]-1].append(vertices[1]-1)
        deg[vertices[1]-1].append(vertices[0]-1)

visited=[False]*n

def explore(j):
    visited[j]=True
    for k in deg[j]:
        if visited[k]==False:
            explore(k)

cc=0

for v in range(n):
    if visited[v]==False:
        cc+=1
        explore(v)

print(cc)