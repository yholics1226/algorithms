# [좌표 압축] https://www.acmicpc.net/problem/18870

import sys
input = sys.stdin.readline
n = int(input())
x = [*map(int, input().split())]
s = list(set(x))
s.sort()
d = {k: i for i, k in enumerate(s)}
print(*[d[k] for k in x])
