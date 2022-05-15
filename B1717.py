# [집합의 표현] https://www.acmicpc.net/problem/1717

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, m = map(int, input().split())
unf = [i for i in range(n+1)]
def find(v):
    if v != unf[v]:
        unf[v] = find(unf[v])
    return unf[v]
def union(a, b):
    fa, fb = find(a), find(b)
    if fa < fb:
        unf[fa] = fb
    elif fa > fb:
        unf[fb] = fa
for _ in range(m):
    op, a, b = map(int, input().split())
    if op:
        print('YES' if find(a) == find(b) else 'NO')
    else:
        union(a, b)
