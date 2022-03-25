# [웜홀] https://www.acmicpc.net/problem/1865

import sys
input = sys.stdin.readline
tc = int(input())
def sol():
    for _ in range(n-1):
        flag = False
        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                flag = True
        if not flag:
            return 'NO'
    for s, e, t in edges:
        if dist[e] > dist[s] + t:
            return 'YES'
    return 'NO'
for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    dist = [0] * (n+1)
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    print(sol())
