# [Subsets] https://leetcode.com/problems/subsets/

from itertools import combinations
def subsets(nums):
    ans = [[]]
    n = len(nums)
    for r in range(1, n+1):
        for comb in combinations(nums, r):
            ans += [comb]
    return ans

# w/o itertools
def subsets(nums):
    ans = [[]]
    for num in nums:
        ans += [x + [num] for x in ans]
    return ans
