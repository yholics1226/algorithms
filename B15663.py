# [N과 M (9)] https://www.acmicpc.net/problem/15663

from collections import Counter
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted([*map(int, input().split())])
cnt = Counter(nums)
keys = cnt.keys()
res = []
def dfs():
    if len(res) == m:
        print(*res)
    else:
        for x in keys:
            if cnt[x] > 0:
                res.append(x)
                cnt[x] -= 1
                dfs()
                res.pop()
                cnt[x] += 1
dfs()

# another solution
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
        prev = 0
        for i in range(n):
            if not ch[i] and prev != nums[i]:
                prev = nums[i]
                res.append(nums[i])
                ch[i] = True
                dfs()
                res.pop()
                ch[i] = False
dfs()
