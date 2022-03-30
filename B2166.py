# [다각형의 면적] https://www.acmicpc.net/problem/2166

import sys
input = sys.stdin.readline
n = int(input())
pts = [tuple(map(int, input().split())) for _ in range(n)]
pts.append(pts[0])
ans = 0
for i in range(n):
    ans += pts[i][0] * pts[i+1][1] - pts[i+1][0] * pts[i][1]
print(round(abs(ans)/2, 1))
