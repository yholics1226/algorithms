# [N과 M (12)] https://www.acmicpc.net/problem/15666

import sys
input = sys.stdin.readline
_, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))
n = len(nums)
res = []
def dfs(s):
    if len(res) == m:
        print(*res)
    else:
        for i in range(s, n):
            res.append(nums[i])
            dfs(i)
            res.pop()
dfs(0)

# another solution
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted([*map(int, input().split())])
res = []
def dfs(s):
    if len(res) == m:
        print(*res)
    else:
        prev = 0
        for i in range(s, n):
            if prev != nums[i]:
                prev = nums[i]
                res.append(nums[i])
                dfs(i)
                res.pop()
dfs(0)

# using itertools
from itertools import combinations_with_replacement as comb
import sys
input = sys.stdin.readline
_, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))
for x in comb(nums, m):
    print(*x)
