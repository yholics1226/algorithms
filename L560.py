# [Subarray Sum Equals K] https://leetcode.com/problems/subarray-sum-equals-k/

from collections import defaultdict
def subarraySum(nums, k):
    ans = 0
    s = 0
    sH = defaultdict(int)
    for num in nums:
        s += num
        if s == k:
            ans += 1
        if sH[s-k]:
            ans += sH[s-k]
        sH[s] += 1
    return ans

# another solution
def subarraySum(nums, k):
    ans = 0
    s = 0
    sH = {0: 1}
    for num in nums:
        s += num
        if s-k in sH:
            ans += sH[s-k]
        if s in sH:
            sH[s] += 1
        else:
            sH[s] = 1
    return ans
