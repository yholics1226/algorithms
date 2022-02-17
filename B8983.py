# [사냥꾼] https://www.acmicpc.net/problem/8983

import sys
input = sys.stdin.readline
m, n, l = map(int, input().split())
pos = [*map(int, input().split())]
pos.sort()
cnt = 0
for _ in range(n):
    x, y = map(int, input().split())
    lt, rt = 0, m-1
    while lt <= rt:
        mid = (lt + rt) // 2
        if abs(pos[mid] - x) + y <= l:
            cnt += 1
            break
        elif pos[mid] < x:
            lt = mid + 1
        else:
            rt = mid - 1
print(cnt)

# another solution
import sys
input = sys.stdin.readline
m, n, l = map(int, input().split())
p = [*map(int, input().split())]
p.sort()
a = [[*map(int, input().split())] for _ in range(n)]
a.sort(reverse=True)
cnt = 0
for i in range(m):
    while a:
        if i < m-1 and abs(p[i] - a[-1][0]) >= abs(p[i+1] - a[-1][0]):
            break
        x, y = a.pop()
        if abs(p[i] - x) + y <= l:
            cnt += 1
print(cnt)
