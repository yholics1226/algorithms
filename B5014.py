# [스타트링크] https://www.acmicpc.net/problem/5014

import sys
from collections import deque
f, s, g, u, d = map(int, sys.stdin.readline().split())
cnt = [-1] * (f+1)
cnt[s] = 0
Q = deque([s])
while Q:
    x = Q.popleft()
    nx = x + u
    if nx <= f and cnt[nx] == -1:
        cnt[nx] = cnt[x] + 1
        Q.append(nx)
    nx = x - d
    if nx > 0 and cnt[nx] == -1:
        cnt[nx] = cnt[x] + 1
        Q.append(nx)
    if cnt[g] != -1:
        print(cnt[g])
        sys.exit(0)
print("use the stairs")
