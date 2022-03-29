# [트리의 지름] https://www.acmicpc.net/problem/1167

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
v = int(input())
tree = [[] for _ in range(v+1)]
for _ in range(v):
    e = [*map(int, input().split())]
    for i in range(1, len(e)-1, 2):
        tree[e[0]].append((e[i], e[i+1]))
def dfs(x, d):
    for y, w in tree[x]:
        if dist[y] == -1:
            dist[y] = d + w
            dfs(y, d + w)
dist = [-1] * (v+1)
dist[1] = 0
dfs(1, 0)
s = dist.index(max(dist))
dist = [-1] * (v+1)
dist[s] = 0
dfs(s, 0)
print(max(dist))
