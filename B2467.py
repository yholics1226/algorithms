# [용액] https://www.acmicpc.net/problem/2467

import sys
input = sys.stdin.readline
n = int(input())
sols = [*map(int, input().split())]
lt, rt = 0, n-1
ans = [sols[lt], sols[rt]]
res = float('inf')
while lt < rt:
    tmp = sols[lt] + sols[rt]
    if tmp == 0:
        print(sols[lt], sols[rt])
        sys.exit(0)
    elif tmp < 0:
        if abs(tmp) < res:
            ans = [sols[lt], sols[rt]]
            res = abs(tmp)
        lt += 1
    elif tmp > 0:
        if abs(tmp) < res:
            ans = [sols[lt], sols[rt]]
            res = abs(tmp)
        rt -= 1
print(*ans)
