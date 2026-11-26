from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
edges = []
rev = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, x = map(int, input().split())
    edges.append((u, v, x))
    graph[u].append(v)
    rev[v].append(u)

vis1 = [False]*(n+1)
q = deque([1])
while q:
    u = q.popleft()
    for v in graph[u]:
        if not vis1[v]:
            vis1[v] = True
            q.append(v)

visn = [False] * (n+1)
q= deque([n])
visn[n] = True
while q:
    u = q.popleft()
    for v in rev[u] :
        if not visn[v]:
            visn[v] = True
            q.append(v)

dist = [float('-inf')]*(n+1)
dist[1] = 0
for _ in range(n-1):
    changed = False
    for u, v, w in edges:
        if dist[u] + w > dist[v]:
            changed = True
            dist[v] = dist[u] + w
    if not changed:
        break

for u, v, w in edges:
    if dist[u] == float('-inf'):
        continue

    if dist[u] + w > dist[v]:
        if vis1[u] and visn[v]:
            print(-1)
            break
else:
    print(dist[n]) 



