# [회의실 배정] https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline
n = int(input())
m = [[*map(int, input().split())] for _ in range(n)]
m.sort(key=lambda x : (x[1], x[0]))
t = ans = 0
for s, e in m:
    if s >= t:
        t = e
        ans += 1
print(ans)
