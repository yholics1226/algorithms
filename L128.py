# [Longest Consecutive Sequence] https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(nums):
    ans = 0
    nums = set(nums)
    for num in nums:
        if num - 1 not in nums:
            n = num + 1
            while n in nums:
                n += 1
            ans = max(ans, n - num)
    return ans
