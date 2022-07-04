# [Wiggle Subsequence] https://leetcode.com/problems/wiggle-subsequence/

def wiggleMaxLength(nums):
    ans, sign = 1, 0
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i-1]
        if diff == 0:
            continue
        if diff > 0:
            if sign <= 0:
                sign = 1
                ans += 1
        elif sign >= 0:
            sign = -1
            ans += 1
    return ans

# another solution
def wiggleMaxLength(nums):
    up = down = 1
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            up = down + 1
        elif nums[i-1] > nums[i]:
            down = up + 1
    return max(up, down)
