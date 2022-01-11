# [블로그2] https://www.acmicpc.net/problem/20365

import sys
input = sys.stdin.readline
n = int(input())
cs = input().strip()
d = {'B': 0, 'R': 0}
c = cs[0]
d[c] += 1
for i in range(1, n):
    if cs[i] != c:
        c = cs[i]
        d[c] += 1
print(min(d['B'], d['R']) + 1)
