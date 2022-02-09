# [K-diff Pairs in an Array] https://leetcode.com/problems/k-diff-pairs-in-an-array/

# sol 1: Sorting and Two Pointers
def findPairs(nums, k):
    if len(nums) == 1:
        return 0
    nums.sort()
    n = len(nums)
    s = set()
    lt, rt = 0, 1
    while lt < rt < n:
        if nums[rt] - nums[lt] == k:
            s.add(nums[lt])
            lt += 1
            rt += 1
        elif nums[rt] - nums[lt] < k:
            rt += 1
        else:
            lt += 1
            if lt == rt:
                rt += 1
    return len(s)

# sol 2: Hash Table
from collections import Counter
def findPairs(nums, k):
    nH = Counter(nums)
    cnt = 0
    if k == 0:
        for x in nH:
            if nH[x] > 1:
                cnt += 1
    else:
        for x in nH:
            if x + k in nH:
                cnt += 1
    return cnt
