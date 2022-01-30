# [Rotate Array] https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sol 1
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        
        # # sol 2
        # for _ in range(k % len(nums)):
        #     nums.insert(0, nums.pop())
        
        # # sol 3
        # n = len(nums)
        # tmp = [0] * n
        # for i in range(n):
        #     tmp[(i + k) % n] = nums[i]
        # nums[:] = tmp
        
        # # sol 4
        # tmp = deque(nums)
        # tmp.rotate(k)
        # nums[:] = tmp
