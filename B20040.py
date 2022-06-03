# [사이클 게임] https://www.acmicpc.net/problem/20040

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
def find(v):
    if v == unf[v]:
        return v
    else:
        unf[v] = find(unf[v])
        return unf[v]
def union(a, b):
    fa = find(a)
    fb = find(b)
    if fa < fb:
        unf[fb] = fa
    else:
        unf[fa] = fb
unf = [i for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i+1)
        break
    union(a, b)
else:
    print(0)
