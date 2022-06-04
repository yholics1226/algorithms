# [사이클 게임] https://www.acmicpc.net/problem/20040

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
def find(v):
    if v == unf[v]:
        return v
    unf[v] = find(unf[v])
    return unf[v]
def union(a, b):
    fa, fb = find(a), find(b)
    if fa == fb:
        return True
    elif fa < fb:
        unf[fb] = fa
    else:
        unf[fa] = fb
    return False
unf = [i for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if union(a, b):
        print(i+1)
        break
else:
    print(0)
