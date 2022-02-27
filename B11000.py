# [강의실 배정] https://www.acmicpc.net/problem/11000

import sys, heapq
input = sys.stdin.readline
n = int(input())
lec = [tuple(map(int, input().split())) for _ in range(n)]
lec.sort(key=lambda x: x[0])
H = []
heapq.heappush(H, lec[0][1])
for i in range(1, n):
    if H[0] <= lec[i][0]:
        heapq.heappop(H)
    heapq.heappush(H, lec[i][1])
print(len(H))
