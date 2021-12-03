# [최소 힙] https://www.acmicpc.net/problem/1927

import sys, heapq
input = sys.stdin.readline
n = int(input())
H = []
for _ in range(n):
    x = int(input())
    if x == 0:
        print(0) if not H else print(heapq.heappop(H))
    else:
        heapq.heappush(H, x)
