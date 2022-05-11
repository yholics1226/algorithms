# [내려가기] https://www.acmicpc.net/problem/2096

import sys
input = sys.stdin.readline
n = int(input())
A = B = C = 0
a = b = c = 0
for _ in range(n):
    x, y, z = map(int, input().split())
    A, B, C = x + max(A, B), y + max(A, B, C), z + max(B, C)
    a, b, c = x + min(a, b), y + min(a, b, c), z + min(b, c)
print(max(A, B, C), min(a, b, c))
