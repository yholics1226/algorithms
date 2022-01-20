# [도시 건설] https://www.acmicpc.net/problem/21924

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edges = [[*map(int, input().split())] for _ in range(m)]
edges.sort(key=lambda x : x[2])
ans = 0
for [_, _, c] in edges:
    ans += c
num = 0
unf = [i for i in range(n+1)]

def find(v):
    if v == unf[v]:
        return v
    else:
        unf[v] = find(unf[v])
        return unf[v]

def union(a, b, c):
    global ans, num
    fa = find(a)
    fb = find(b)
    if fa != fb:
        unf[fa] = fb
        ans -= c
        num += 1

for [a, b, c] in edges:
    union(a, b, c)
    if num == n-1:
        print(ans)
        sys.exit(0)
print(-1)
