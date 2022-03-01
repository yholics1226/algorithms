# [N과 M (2)] https://www.acmicpc.net/problem/15650

n, m = map(int, input().split())
def dfs(e, k, path):
    if k == 0:
        print(*path)
    else:
        for i in range(e+1, n+1):
            dfs(i, k-1, path + [i])
dfs(0, m, [])

# another solution
n, m = map(int, input().split())
res = []
def dfs(s):
    if len(res) == m:
        print(*res)
    else:
        for i in range(s, n+1):
            res.append(i)
            dfs(i+1)
            res.pop()
dfs(1)

# using itertools
from itertools import combinations
n, m = map(int, input().split())
for x in combinations(range(1, n+1), m):
    print(*x)

# using itertools and starmap
from itertools import *
n, m = map(int, input().split())
*starmap(print, combinations(range(1, n+1), m)),
