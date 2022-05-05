# [Max Number of K-Sum Pairs] https://leetcode.com/problems/max-number-of-k-sum-pairs/

from collections import Counter
def maxOperations(nums, k):
    nH = Counter(nums)
    ans = 0
    for n in nH:
        m = k - n
        if n < m:
            ans += min(nH[n], nH[m])
        elif n == m:
            ans += nH[n] // 2
    return ans

# using sorting and two pointers
def maxOperations(nums, k):
    nums.sort()
    ans, lt, rt = 0, 0, len(nums) - 1
    while lt < rt:
        s = nums[lt] + nums[rt]
        if s < k:
            lt += 1
        elif s > k:
            rt -= 1
        else:
            ans += 1
            lt += 1
            rt -= 1
    return ans
