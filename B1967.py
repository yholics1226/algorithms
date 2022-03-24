# [트리의 지름] https://www.acmicpc.net/problem/1967

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])
def dfs(x, d):
    for y, w in tree[x]:
        if dist[y] == -1:
            dist[y] = d + w
            dfs(y, d + w)
dist = [-1] * (n+1)
dist[1] = 0
dfs(1, 0)
s = dist.index(max(dist))
dist = [-1] * (n+1)
dist[s] = 0
dfs(s, 0)
print(max(dist))

# another solution (faster)
import sys
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
res = [(0, 0)] * (n+1)
for x in range(n, 0, -1):
    m1, m2 = 0, 0
    for y, w in tree[x]:
        d = w + res[y][0]
        if d > m1:
            m1, m2 = d, m1
        elif d > m2:
            m2 = d
    res[x] = (m1, m2)
print(max([sum(x) for x in res]))
