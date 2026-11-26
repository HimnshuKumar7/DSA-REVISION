n, q = map(int, input().split())
val = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v); graph[v].append(u)

tin =[0] * (n+1); tout =  [0] * (n+1)
st = [(1, 0, 0)] ; timer = 0
while st:
    node, par, state = st.pop()
    if state == 0 :
        timer += 1
        tin[node] = timer; tout[node] = timer
        st.append((node, par, 1))
        for nei in graph[node]:
            if nei != par:
                st.append((nei, node, 0))
    else:
        tout[node] = timer

bit = [0] * (n+2)
def update(i, x):
    while i <= n+1:
        bit[i] += x
        i += ( i & - i)

def query(i):
    ans = 0
    while i > 0:
        ans += bit[i]
        i -= ( i  & -i)

    return ans

for u in range(1, n+1):
    update(tin[u], val[u]); update(tout[u]+1, -val[u])
ans = []
for _ in range(q):
    data = input().split()
    if data[0] == '1':
        idx = int(data[1]); value = int(data[2])
        update(tin[idx], value - val[idx]); update(tout[idx]+1, -(value- val[idx]))
        val[idx] = value
    else:
        idx = int(data[1])
        res = query(tin[idx])
        ans.append(res)

for ele in ans:
    print(ele)
        

