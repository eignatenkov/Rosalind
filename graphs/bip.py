__author__ = 'egor'

# Given: A positive integer k≤20 and k simple graphs in the edge list format with at most 103 vertices each.
#
# Return: For each graph, output "1" if it is bipartite and "-1" otherwise.
#
# Sample Dataset
#
# 2
#
# 3 3
# 1 2
# 3 2
# 3 1
#
# 4 3
# 1 4
# 3 1
# 1 2
#
# Sample Output
#
# -1 1


def explore(j, col):
    visited[j] = True
    bip[j]=col
    for l in graph[j]:
        if visited[l]:
            if bip[l]==col:
                return -1
        else:
            explore(l, 1-col)

with open("/home/egor/Загрузки/rosalind_bip.txt","r") as f:
    k=int(f.readline().strip())
    answer=[1]*k
    for i in range(k):
        f.readline()
        info=[int(i) for i in f.readline().strip().split(' ')]
        n=info[0]
        graph=[[] for i in range(n)]
        for j in range(info[1]):
            line=f.readline()
            vertices=[int(i) for i in line.strip().split(' ')]
            graph[vertices[0]-1].append(vertices[1]-1)
            graph[vertices[1]-1].append(vertices[0]-1)
        bip=[-1]*n
        visited=[False]*n
        for v in range(n):
            if visited[v]==False:
                if explore(v,0)==-1:
                    answer[i]=-1

print(' '.join(map(str,answer)))