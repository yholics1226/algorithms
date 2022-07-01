# [Minimum Moves to Equal Array Elements II] https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

def minMoves2(nums):
    nums.sort()
    m = nums[len(nums)//2]
    return sum(abs(num - m) for num in nums)
