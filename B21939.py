# [문제 추천 시스템 Version 1] https://www.acmicpc.net/problem/21939

import sys, heapq
input = sys.stdin.readline
n = int(input())
minH = []
maxH = []
for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(minH, (l, p))
    heapq.heappush(maxH, (-l, -p))
m = int(input())
sol = set()
for _ in range(m):
    cmd = [*map(str, input().split())]
    if cmd[0][0] == 'a':
        p, l = int(cmd[1]), int(cmd[2])
        heapq.heappush(minH, (l, p))
        heapq.heappush(maxH, (-l, -p))
    elif cmd[0][0] == 's':
        sol.add(int(cmd[1]))
    else:
        if cmd[1] == '1':
            while True:
                l, p = heapq.heappop(maxH)
                if -p in sol:
                    sol.remove(-p)
                else:
                    print(-p)
                    heapq.heappush(maxH, (l, p))
                    break
        else:
            while True:
                l, p = heapq.heappop(minH)
                if p in sol:
                    sol.remove(p)
                else:
                    print(p)
                    heapq.heappush(minH, (l, p))
                    break
