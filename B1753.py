# [최단경로] https://www.acmicpc.net/problem/1753

import sys, heapq
input = sys.stdin.readline
v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
dist = [4000000] * (v+1)
tree = []
heapq.heappush(tree, (0, k))
dist[k] = 0
while tree:
    d, x = heapq.heappop(tree)
    if d > dist[x]:
        continue
    for nx, nd in graph[x]:
        if d + nd < dist[nx]:
            dist[nx] = d + nd
            heapq.heappush(tree, (dist[nx], nx))
for i in range(1, v+1):
    print(dist[i] if dist[i] < 4000000 else 'INF')
