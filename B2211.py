# [네트워크 복구] https://www.acmicpc.net/problem/2211

import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
cost = [float('inf')] * (n+1)
conn = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])
print(n-1)
tree = []
heapq.heappush(tree, (0, 1))
cost[1] = 0
while tree:
    c, b = heapq.heappop(tree)
    if c > cost[b]:
        continue
    for [nc, nb] in graph[b]:
        if c + nc < cost[nb]:
            conn[nb] = b
            cost[nb] = c + nc
            heapq.heappush(tree, (cost[nb], nb))
for i in range(2, n+1):
    print(i, conn[i])
