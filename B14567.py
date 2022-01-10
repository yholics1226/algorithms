# [선수과목 (Prerequisite)] https://www.acmicpc.net/problem/14567

from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indeg = [0] * (n+1)
dp = [1] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indeg[b] += 1
Q = deque()
for i in range(1, n+1):
    if indeg[i] == 0:
        Q.append(i)
while Q:
    x = Q.popleft()
    for y in graph[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            dp[y] = dp[x] + 1
            Q.append(y)
print(*dp[1:])
