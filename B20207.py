# [달력] https://www.acmicpc.net/problem/20207

import sys
input = sys.stdin.readline
n = int(input())
nums = [0] * 366
for _ in range(n):
    s, e = map(int, input().split())
    nums[s-1] += 1
    nums[e] -= 1
ans = cnt = maxc = lt = 0
for i, num in enumerate(nums):
    if num == 0:
        continue
    if cnt == 0:
        lt = i
    cnt += num
    maxc = max(maxc, cnt)
    if cnt == 0:
        ans += maxc * (i - lt)
        maxc = 0
print(ans)

# another solution
import sys
input = sys.stdin.readline
n = int(input())
nums = [0] * 366
for _ in range(n):
    s, e = map(int, input().split())
    nums[s-1] += 1
    nums[e] -= 1
for i in range(1, 366):
    nums[i] += nums[i-1]
ans = w = h = 0
for num in nums:
    if num:
        w += 1
        h = max(h, num)
    else:
        ans += w * h
        w = h = 0
print(ans)
