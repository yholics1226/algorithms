# [덩치] https://www.acmicpc.net/problem/7568

import sys
input = sys.stdin.readline
n = int(input())
nums = []
for i in range(n):
    x, y = map(int, input().split())
    nums.append((x, y, i))
nums = sorted(nums, key=lambda x: (x[0], x[1]), reverse=True)
ans = [1] * n
for i in range(1, n):
    cnt = 0
    for j in range(i):
        if nums[i][0] < nums[j][0] and nums[i][1] < nums[j][1]:
            cnt += 1
    ans[nums[i][2]] += cnt
print(*ans)

# another solution (slightly faster?)
import sys
input = sys.stdin.readline
n = int(input())
nums = [[*map(int, input().split())] for _ in range(n)]
for x in nums:
    cnt = 1
    for y in nums:
        if x[0] < y[0] and x[1] < y[1]:
            cnt += 1
    print(cnt, end=' ')
