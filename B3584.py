# [가장 가까운 공통 조상] https://www.acmicpc.net/problem/3584

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    p = {}
    for _ in range(n-1):
        a, b = map(int, input().split())
        p[b] = a
    x, y = map(int, input().split())
    s = {x}
    while x in p:
        x = p[x]
        s.add(x)
    while True:
        if y in s:
            print(y)
            break
        else:
            y = p[y]

# another solution
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    p = [0] * (n+1)
    for _ in range(n-1):
        a, b = map(int, input().split())
        p[b] = a
    x, y = map(int, input().split())
    s = {x}
    while p[x]:
        x = p[x]
        s.add(x)
    while True:
        if y in s:
            print(y)
            break
        else:
            y = p[y]
