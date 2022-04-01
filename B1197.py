# [최소 스패닝 트리] https://www.acmicpc.net/problem/1197

import sys
input = sys.stdin.readline
v, e = map(int, input().split())
unf = [i for i in range(v+1)]
edges = [[*map(int, input().split())] for _ in range(e)]
edges.sort(key=lambda x : x[2])
ans = num = 0
def find(v):
    if v == unf[v]:
        return v
    else:
        unf[v] = find(unf[v])
        return unf[v]    
for a, b, c in edges:
    fa = find(a)
    fb = find(b)
    if fa != fb:
        unf[fa] = fb
        ans += c
        num += 1
    if num == v-1:
        break
print(ans)
