# [숨바꼭질] https://www.acmicpc.net/problem/6118

# sol 1: Dijkstra
import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
d = [50000] * (n+1)
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
H = []
heapq.heappush(H, (0, 1))
d[0] = d[1] = 0
while H:
    c, x = heapq.heappop(H)
    if c > d[x]:
        continue
    for nx in g[x]:
        if c+1 < d[nx]:
            d[nx] = c+1
            heapq.heappush(H, (d[nx], nx))
dmax = max(d)
print(d.index(dmax), dmax, d.count(dmax))

# sol 2: BFS
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = [-1] * (n+1)
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
Q = deque([1])
d[1] = 0
while Q:
    x = Q.popleft()
    for y in g[x]:
        if d[y] == -1:
            d[y] = d[x] + 1
            Q.append(y)
dmax = max(d)
print(d.index(dmax), dmax, d.count(dmax))
