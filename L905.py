# [Sort Array By Parity] https://leetcode.com/problems/sort-array-by-parity/

def sortArrayByParity(nums):
    return sorted(nums, key=lambda x: x % 2)

# another solution
def sortArrayByParity(nums):
    return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2]

# using two pointers
def sortArrayByParity(nums):
    idx = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[idx], nums[i] = nums[i], nums[idx]
            idx += 1
    return nums
