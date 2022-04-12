# [리모컨] https://www.acmicpc.net/problem/1107

import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
ans = abs(n - 100)
if m == 0:
    print(min(len(str(n)), ans))
else:
    broken = set(input().split())
    for num in range(max(0, n - ans), n + ans):
        for x in str(num):
            if x in broken:
                break
        else:
            ans = min(ans, len(str(num)) + abs(n - num))
    print(ans)

# another expression
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
ans = abs(n - 100)
if m == 0:
    print(min(len(str(n)), ans))
else:
    broken = set(input().split())
    for num in range(max(0, n - ans), n + ans):
        if set(str(num)) & broken:
            continue
        ans = min(ans, len(str(num)) + abs(n - num))
    print(ans)
