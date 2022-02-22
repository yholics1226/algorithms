# [제곱수 찾기] https://www.acmicpc.net/problem/1025

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [[*map(int, input().rstrip())] for _ in range(n)]
ans = -1
for i in range(n):
    for j in range(m):
        for dx in range(-n, n):
            for dy in range(-m, m):
                if dx == dy == 0:
                    continue
                tmp = 0
                x, y = i, j
                while 0 <= x < n and 0 <= y < m:
                    tmp = tmp * 10 + a[x][y]
                    if tmp > ans:
                        sqrt = tmp ** 0.5
                        if sqrt == int(sqrt):
                            ans = tmp
                    x += dx
                    y += dy
print(ans)
