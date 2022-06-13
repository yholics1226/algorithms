# [Maximum Erasure Value] https://leetcode.com/problems/maximum-erasure-value/

def maximumUniqueSubarray(nums):
    seen = set()
    ans = tmp = i = 0
    for num in nums:
        while num in seen:
            seen.remove(nums[i])
            tmp -= nums[i]
            i += 1
        tmp += num
        seen.add(num)
        ans = max(ans, tmp)
    return ans
