# [트리] https://www.acmicpc.net/problem/1068

import sys
input = sys.stdin.readline
n = int(input())
parent = [*map(int, input().split())]
m = int(input())
child = [set() for _ in range(n)]
for i, p in enumerate(parent):
    if p == -1:
        root = i
    else:
        child[p].add(i)
if m == root:
    print(0)
else:
    child[parent[m]].remove(m)
    cnt = 0
    def dfs(v):
        global cnt
        if not child[v]:
            cnt += 1
        else:
            for nv in child[v]:
                dfs(nv)
    dfs(root)
    print(cnt)

# another solution
import sys
input = sys.stdin.readline
n = int(input())
tree = [*map(int, input().split())]
def dfs(v):
    tree[v] = -2
    for i in range(n):
        if v == tree[i]:
            dfs(i)
dfs(int(input()))
cnt = 0
for i in range(n):
    if tree[i] != -2 and i not in tree:
        cnt += 1
print(cnt)
