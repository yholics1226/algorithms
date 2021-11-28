# [친구 네트워크] https://www.acmicpc.net/problem/4195

def find(x):
    if rep[x] == x:
        return x
    else:
        rep[x] = find(rep[x])
        return rep[x]

def union(x, y):
    xrep = find(x)
    yrep = find(y)
    if xrep != yrep:
        rep[yrep] = xrep
        cnt[xrep] += cnt[yrep]
    return cnt[xrep]

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    f = int(input())
    rep = dict()
    cnt = dict()
    for _ in range(f):
        a, b = map(str, input().split())
        if a not in rep:
            rep[a] = a
            cnt[a] = 1
        if b not in rep:
            rep[b] = b
            cnt[b] = 1
        print(union(a, b))
