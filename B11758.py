# [CCW] https://www.acmicpc.net/problem/11758

import sys
input = sys.stdin.readline
x, y = [0] * 3, [0] * 3
for i in range(3):
    x[i], y[i] = map(int, input().split())
cp = (x[0]*y[1]+x[1]*y[2]+x[2]*y[0])-(x[1]*y[0]+x[2]*y[1]+x[0]*y[2])
if cp > 0:
    print(1)
elif cp < 0:
    print(-1)
else:
    print(0)
