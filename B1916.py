# [최소비용 구하기] https://www.acmicpc.net/problem/1916

import sys, heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
s, e = map(int, input().split())
cost = [float('inf')] * (n+1)
tree = []
heapq.heappush(tree, (0, s))
cost[s] = 0
while tree:
    c, x = heapq.heappop(tree)
    if c > cost[x]:
        continue
    for nx, nc in graph[x]:
        if c + nc < cost[nx]:
            cost[nx] = c + nc
            heapq.heappush(tree, (cost[nx], nx))
print(cost[e])
