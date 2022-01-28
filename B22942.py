# [데이터 체커] https://www.acmicpc.net/problem/22942

import sys
input = sys.stdin.readline
n = int(input())

class Point:
    def __init__(self, p, isOpen, no):
        self.p = p
        self.isOpen = isOpen
        self.no = no

c = []
for i in range(n):
    x, r = map(int, input().split())
    c.append(Point(x - r, True, i))
    c.append(Point(x + r, False, i))
c.sort(key=lambda x: x.p)
s = []
ch = set()
for circle in c:
    next = circle
    if next.p in ch:
        print("NO")
        sys.exit(0)
    if next.isOpen:
        s.append(next)
        ch.add(next.p)
    elif s[-1].no != next.no:
        print("NO")
        sys.exit(0)
    else:
        ch.add(next.p)
        s.pop()
print('YES')
