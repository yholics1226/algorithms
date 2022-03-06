# [N과 M (5)] https://www.acmicpc.net/problem/15654

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted([*map(int, input().split())])
ch = [False] * n
res = []
def dfs():
    if len(res) == m:
        print(*res)
    else:
        for i in range(n):
            if not ch[i]:
                ch[i] = True
                res.append(nums[i])
                dfs()
                res.pop()
                ch[i] = False
dfs()

# using itertools
from itertools import permutations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted([*map(int, input().split())])
for x in permutations(nums, m):
    print(*x)
