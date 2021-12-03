# [수들의 합 2] https://www.acmicpc.net/problem/2003

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
s, lt, rt = nums[0], 0, 0
while rt < n:
    if s == m:
        cnt += 1
        s -= nums[lt]
        lt += 1
        rt += 1
        if rt < n:
            s += nums[rt]
    elif s > m:
        s -= nums[lt]
        lt += 1
    else:
        rt += 1
        if rt < n:
            s += nums[rt]
print(cnt)
