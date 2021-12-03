# [Maximum Product Subarray] https://leetcode.com/problems/maximum-product-subarray/

def maxProduct(nums):
    n = len(nums)
    lp, rp = nums[0], nums[-1]
    ans = max(lp, rp)
    for i in range(1, len(nums)):
        lp = nums[i] if lp == 0 else lp * nums[i]
        rp = nums[n-1-i] if rp == 0 else rp * nums[n-1-i]
        ans = max(ans, lp, rp)
    return ans
