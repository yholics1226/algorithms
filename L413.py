# [Arithmetic Slices] https://leetcode.com/problems/arithmetic-slices/

def numberOfArithmeticSlices(nums):
    n = len(nums)
    if n < 3:
        return 0
    ans, cnt, d = 0, 0, 3000
    for i in range(1, n):
        diff = nums[i] - nums[i-1]
        if diff == d:
            cnt += 1
            ans += cnt
        else:
            d = diff
            cnt = 0
    return ans
