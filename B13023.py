# [ABCDE] https://www.acmicpc.net/problem/13023

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(v, path):
    if len(path) == 5:
        print(1)
        sys.exit(0)
    for w in graph[v]:
        if w not in path:
            dfs(w, path + [w])
for i in range(n):
    dfs(i, [i])
print(0)

# faster version
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
visit = [False] * n
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(v, d):
    if d == 4:
        print(1)
        sys.exit(0)
    for w in graph[v]:
        if not visit[w]:
            visit[w] = True
            dfs(w, d+1)
            visit[w] = False
for i in range(n):
    visit[i] = True
    dfs(i, 0)
    visit[i] = False
print(0)
