import sys, heapq
input = sys.stdin.readline

n,m = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, c = map(int, input().split())
    adj[u].append((v, c))

dist = [[float('inf')] *2 for _ in range(n+1)]
dist[1][0] = 0
pq = [(0, 1, 0)]

while pq:
    c, node, state = heapq.heappop(pq)

    if c != dist[node][state]:
        continue

    for v, w in adj[node]:
        if c + w < dist[v][state]:
            dist[v][state] = c + w
            heapq.heappush(pq, (c+w, v, state))

        if not state:
            nd = c + w // 2
            if nd < dist[v][1]:
                dist[v][1] = nd
                heapq.heappush(pq, (nd, v, 1))

print(dist[n][1])




