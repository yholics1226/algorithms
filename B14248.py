# [점프 점프] https://www.acmicpc.net/problem/14248

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
jump = list(map(int, input().split()))
s = int(input())
ch = [0] * n
ch[s-1] = 1
cnt = 1
Q = deque([(s-1, jump[s-1])])
while Q:
    i, j = Q.popleft()
    if i-j >= 0 and ch[i-j] == 0:
        ch[i-j] = 1
        cnt += 1
        Q.append((i-j, jump[i-j]))
    if i+j < n and ch[i+j] == 0:
        ch[i+j] = 1
        cnt += 1
        Q.append((i+j, jump[i+j]))
print(cnt)
