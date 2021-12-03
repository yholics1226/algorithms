# [House Robber] https://leetcode.com/problems/house-robber/

def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    else:
        dp = [0] * (n+1)
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])
        for i in range(3, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1], dp[i-3] + nums[i-1])
        return dp[n]
