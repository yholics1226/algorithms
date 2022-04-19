# [친구] https://www.acmicpc.net/problem/1058

import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    x = input()
    for j in range(n):
        if x[j] == 'Y':
            graph[i].append(j)
res = {i: set(graph[i]) for i in range(n)}
for i in range(n):
    for j in graph[i]:
        res[i].update(set(graph[j]))
ans = max(len(res[i]) for i in range(n))
print(max(ans-1, 0))
