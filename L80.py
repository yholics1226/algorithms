# [Remove Duplicates from Sorted Array 2] https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

def removeDuplicates(nums):
    k, i = len(nums), 1
    while i < k:
        if nums[i-1] == nums[i]:
            j = i+1
            while j < k and nums[i] == nums[j]:
                del nums[j]
                k -= 1
        i += 1
    return k
