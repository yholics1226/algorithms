# [기타줄] https://www.acmicpc.net/problem/1049

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
x = y = 1000
for _ in range(m):
    a, b = map(int, input().split())
    x, y = min(x, a), min(y, b)
print(min(n * y, n // 6 * x + min(x, n % 6 * y)))

# another solution
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
x = y = 1000
for _ in range(m):
    a, b = map(int, input().split())
    x, y = min(x, a, 6 * b), min(y, b)
print(n // 6 * x + min(x, n % 6 * y))
