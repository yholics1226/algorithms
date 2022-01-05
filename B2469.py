# [사다리 타기] https://www.acmicpc.net/problem/2469

from collections import deque
import sys
input = sys.stdin.readline
k = int(input())
n = int(input())

res = [*map(str, input().strip())]
start = sorted(res)

prev = deque()
post = deque()
flag = 0
for _ in range(n):
    tmp = [*map(str, input().strip())]
    if tmp[0] == '?':
        flag = 1
    elif flag:
        post.append(tmp)
    else:
        prev.append(tmp)

while prev:
    tmp = prev.popleft()
    for i in range(k-1):
        if tmp[i] == '-':
            start[i], start[i+1] = start[i+1], start[i]

while post:
    tmp = post.pop()
    for i in range(k-1):
        if tmp[i] == '-':
            res[i], res[i+1] = res[i+1], res[i]

ans = ['*'] * (k-1)
for i in range(k-1):
    if start[i] == res[i+1] and start[i+1] == res[i]:
        ans[i] = '-'
        start[i], start[i+1] = start[i+1], start[i]

if start != res:
    ans = ['x'] * (k-1)
print(''.join(ans))
