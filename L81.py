# [Search in Rotated Sorted Array 2] https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

def search(nums, target):
    lt, rt = 0, len(nums)-1
    while lt <= rt:
        while lt < rt and nums[lt] == nums[lt+1]:
            lt += 1
        while lt < rt and nums[rt] == nums[rt-1]:
            rt -= 1
        mid = (lt + rt) // 2
        if nums[mid] == target:
            return True
        if nums[lt] <= nums[mid]:
            if nums[lt] <= target < nums[mid]:
                rt = mid - 1
            else:
                lt = mid + 1
        else:
            if nums[mid] < target <= nums[rt]:
                lt = mid + 1
            else:
                rt = mid - 1
    return False
