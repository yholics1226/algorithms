# [홀짝 칵테일] https://www.acmicpc.net/problem/21312

import sys
cock = [*map(int, sys.stdin.readline().split())]
odds = [x for x in cock if x%2]
ans = 1
if odds:
    for x in odds:
        ans *= x
else:
    for x in cock:
        ans *= x
print(ans)
