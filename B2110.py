# [공유기 설치] https://www.acmicpc.net/problem/2110

import sys
input = sys.stdin.readline
n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()
ans, lt, rt = 1, 1, x[-1] - x[0]
while lt <= rt:
    mid = (lt + rt) // 2
    cur = x[0]
    cnt = 1
    for i in range(1, n):
        if x[i] >= cur + mid:
            cur = x[i]
            cnt += 1
    if cnt >= c:
        lt = mid + 1
        ans = mid
    else:
        rt = mid - 1
print(ans)
