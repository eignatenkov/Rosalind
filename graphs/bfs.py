__author__ = 'egor'

# The task is to use breadth-first search to compute single-source shortest distances in an unweighted directed graph.
#
# Given: A simple directed graph with n≤10^3 vertices in the edge list format.
#
# Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). If i
# is not reachable from 1 set D[i] to −1.
#
# Sample Dataset
#
# 6 6
# 4 6
# 6 5
# 4 3
# 3 5
# 2 1
# 1 4
#
# Sample Output
#
# 0 -1 2 1 3 2

with open("/home/egor/Загрузки/rosalind_bfs.txt","r") as f:
    info=[int(i) for i in f.readline().strip().split(' ')]
    n=info[0]
    deg=[[] for i in range(n)]
    for line in f:
        vertices=[int(i) for i in line.strip().split(' ')]
        deg[vertices[0]-1].append(vertices[1]-1)

dist=[-1]*n

dist[0]=0

queue=[0]

while len(queue)>0:
    u=queue[0]
    queue.pop(0)
    for v in deg[u]:
        if dist[v]==-1:
            queue.append(v)
            dist[v]=dist[u]+1

print(' '.join(map(str,dist)))