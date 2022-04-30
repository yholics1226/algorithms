# [좌표 압축] https://www.acmicpc.net/problem/18870

import sys
input = sys.stdin.readline
n = int(input())
x = [*map(int, input().split())]
xs = list(set(x))
xs.sort()
xd = {k: i for i, k in enumerate(xs)}
print(*[xd[k] for k in x])
