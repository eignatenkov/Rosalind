__author__ = 'egor'

with open("/home/egor/Загрузки/dfs.txt","r") as f:
    info=[int(i) for i in f.readline().strip().split(' ')]
    n=info[0]
    graph=[[] for i in range(n)]
    for line in f:
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

print(isdag)