# [우주신과의 교감] https://www.acmicpc.net/problem/1774

import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
locs = [0] + [[*map(int, input().split())] for _ in range(n)]
rep = [i for i in range(n+1)]
ans = 0
cnt = 0

def find(v):
    if v == rep[v]:
        return v
    else:
        rep[v] = find(rep[v])
        return rep[v]

def union(a, b, d=0):
    global cnt, ans
    fa = find(a)
    fb = find(b)
    if fa != fb:
        rep[fb] = fa
        cnt += 1
        ans += d

def diff(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

H = []
for i in range(1, n):
    for j in range(i+1, n+1):
        heapq.heappush(H, [diff(locs[i], locs[j]), i, j])

while cnt < n-1:
    d, a, b = heapq.heappop(H)
    union(a, b, d)

print('%.2f' % ans)
