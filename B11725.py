# [트리의 부모 찾기] https://www.acmicpc.net/problem/11725

from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
par = [-1] * (n+1)
par[1] = 0
Q = deque([1])
while Q:
    x = Q.popleft()
    for y in tree[x]:
        if par[y] < 0:
            par[y] = x
            Q.append(y)
for i in range(2, n+1):
    print(par[i])

# another solution
import sys
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
par = [-1] * (n+1)
par[1] = 0
node = [1]
while node:
    child = []
    for x in node:
        for y in tree[x]:
            if par[y] < 0:
                par[y] = x
                child.append(y)
    node = child
for i in range(2, n+1):
    print(par[i])
