# [토너먼트] https://www.acmicpc.net/problem/1057

import sys
_, a, b = map(int, sys.stdin.readline().split())
ans = 0
while a != b:
    a = (a + 1) // 2
    b = (b + 1) // 2
    ans += 1
print(ans)
