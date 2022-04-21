# [도시 분할 계획] https://www.acmicpc.net/problem/1647

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
roads = [[*map(int, input().split())] for _ in range(m)]
roads.sort(key=lambda x: x[2])
unf = [i for i in range(n+1)]
ans = cnt = 0
def find(v):
    if v == unf[v]:
        return v
    unf[v] = find(unf[v])
    return unf[v]
for a, b, c in roads:
    fa, fb = find(a), find(b)
    if fa != fb:
        unf[fa] = fb
        ans += c
        cnt += 1
    if cnt == n-2:
        break
print(ans)
