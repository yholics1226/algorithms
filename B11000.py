# [강의실 배정] https://www.acmicpc.net/problem/11000

import sys, heapq
input = sys.stdin.readline
n = int(input())
lec = [tuple(map(int, input().split())) for _ in range(n)]
lec.sort(key=lambda x: x[0])
H = []
for s, t in lec:
    if H and H[0] <= s:
        heapq.heappop(H)
    heapq.heappush(H, t)
print(len(H))
