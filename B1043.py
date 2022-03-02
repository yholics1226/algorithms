# [거짓말] https://www.acmicpc.net/problem/1043

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = set(input().rstrip().split()[1:])
pt = [set(input().rstrip().split()[1:]) for _ in range(m)]
res = [1] * m
for _ in range(m):
    for i, p in enumerate(pt):
        if res[i] and s & p:
            res[i] = 0
            s |= p
print(sum(res))
