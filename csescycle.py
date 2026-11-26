n, m = map(int, input().split())
edges = []
graph = [[] for _ in range(n+1)]
parent = [-1] * (n+1) 

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
    graph[u].append(v)

dist = [float('inf')] * (n+1)
dist[1] = 0
x = -1

for _ in range(n-1):
    x = -1
    for u, v, wt in edges:
        if dist[u] != float('inf') and dist[u] + wt < dist[v]:
            dist[v] = dist[u] + wt
            parent[v] = u
            x = v


change = False
for u, v, wt in edges:
    if dist[u] + wt < dist[v]:
        change = True
        x = v
        parent[v] = u
        break

if not change:
    print("NO")
else:
    print("YES")
    
    for _ in range(n):
        x = parent[x]
    cycle = []
    cur = x
    while True:
        cycle.append(cur)
        if cur == x and len(cycle) > 1:
            break
        cur = parent[cur]
    cycle.reverse()
    print(*cycle)