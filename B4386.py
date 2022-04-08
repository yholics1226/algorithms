# [별자리 만들기] https://www.acmicpc.net/problem/4386

import sys
input = sys.stdin.readline
n = int(input())
locs = [tuple(map(float, input().split())) for _ in range(n)]
unf = [i for i in range(n)]
ans = cnt = 0
def find(v):
    if v == unf[v]:
        return v
    else:
        unf[v] = find(unf[v])
        return unf[v]
def union(a, b, d=0):
    global cnt, ans
    fa = find(a)
    fb = find(b)
    if fa != fb:
        unf[fb] = fa
        cnt += 1
        ans += d
def diff(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
lines = [[i, j, diff(locs[i], locs[j])] for i in range(n-1) for j in range(i+1, n)]
lines.sort(key=lambda x: x[2], reverse=True)
while cnt < n-1:
    a, b, d = lines.pop()
    union(a, b, d)
print('%.2f' % ans)
