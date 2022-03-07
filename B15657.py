# [N과 M (8)] https://www.acmicpc.net/problem/15657

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted([*map(int, input().split())])
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

# using itertools
from itertools import *
n, m = map(int, input().split())
*starmap(print, combinations_with_replacement(sorted(map(int, input().split())), m)),
