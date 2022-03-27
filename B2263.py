# [트리의 순회] https://www.acmicpc.net/problem/2263

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
ino = [*map(int, input().split())]
post = [*map(int, input().split())]
idx = [0] * (n+1)
for i in range(n):
    idx[ino[i]] = i
ans = []
def pre(si, ei, sp, ep):
    if si <= ei:
        ans.append(post[ep])
        x = idx[post[ep]]
        pre(si, x-1, sp, sp-si+x-1)
        pre(x+1, ei, sp-si+x, ep-1)
pre(0, n-1, 0, n-1)
print(*ans)
