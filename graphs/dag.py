__author__ = 'egor'

# Given: A positive integer k≤20 and k simple directed graphs in the edge list format with at most 10^3 vertices and
# 3⋅10^3 edges each.
#
# Return: For each graph, output "1" if the graph is acyclic and "-1" otherwise.
#
# Sample Dataset
#
# 3
#
# 2 1
# 1 2
#
# 4 4
# 4 1
# 1 2
# 2 3
# 3 1
#
# 4 3
# 4 3
# 3 2
# 2 1
#
# Sample Output
#
# 1 -1 1

with open("/home/egor/Загрузки/rosalind_dag.txt","r") as f:
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
        visited=[False]*n
        pre=[0]*n
        post=[0]*n
        time=0
        isdag=1

        def explore(j,clock):
            visited[j]=True
            pre[j]=clock
            clock+=1
            for k in graph[j]:
                if visited[k]==False:
                    clock=explore(k,clock)
            post[j]=clock
            clock+=1
            return clock

        for v in range(n):
            if visited[v]==False:
                time=explore(v,time)

        for v in range(n):
            for u in graph[v]:
                if post[u]>post[v]:
                    isdag=-1
                    break
            if isdag ==-1:
                break

        answer[i]=isdag

print(' '.join(map(str,answer)))