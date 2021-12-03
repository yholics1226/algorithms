# [정수 삼각형] https://www.acmicpc.net/problem/1932

import sys
input = sys.stdin.readline
n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            tri[i][j] += tri[i-1][0]
        elif j == i:
            tri[i][j] += tri[i-1][-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])
print(max(tri[-1]))
