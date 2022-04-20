# [행렬] https://www.acmicpc.net/problem/1080

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [[*map(int,list(input().rstrip()))] for _ in range(n)]
b = [[*map(int,list(input().rstrip()))] for _ in range(n)]
def reverse(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            a[i][j] = 1 - a[i][j]
def check():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True
cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            reverse(i, j)
            cnt += 1
if check():
    print(cnt)
else:
    print("-1")
