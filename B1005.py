# [ACM Craft] https://www.acmicpc.net/problem/1005

from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    delay = [0] + list(map(int, input().split()))
    res = [0] * (n+1)
    order = [[] for _ in range(n+1)]
    inDeg = [0] * (n+1)
    for _ in range(k):
        a, b = map(int, input().split())
        order[a].append(b)
        inDeg[b] += 1
    q = deque()
    for i in range(1, n+1):
        if inDeg[i] == 0:
            q.append(i)
            res[i] = delay[i]
    while q:
        x = q.popleft()
        for y in order[x]:
            res[y] = max(res[y], delay[y] + res[x])
            inDeg[y] -= 1
            if inDeg[y] == 0:
                q.append(y)
    w = int(input())
    print(res[w])

# using cache (faster)
from functools import lru_cache
import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
t = int(input())
@lru_cache(None)
def btime(x):
    if not order[x]:
        return ct[x]
    else:
        for y in order[x]:
            ct[x] = max(ct[x], delay[x] + btime(y))
        return ct[x]
for _ in range(t):
    btime.cache_clear()
    n, k = map(int, input().split())
    delay = [0] + list(map(int, input().split()))
    ct = copy.deepcopy(delay)
    order = [[] for _ in range(n+1)]
    for _ in range(k):
        a, b = map(int, input().split())
        order[b].append(a)
    w = int(input())
    print(btime(w))
