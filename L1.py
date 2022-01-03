# [Two Sum] https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    nH = dict()
    for i, n in enumerate(nums):
        if target-n in nH:
            return nH[target-n], i
        else:
            nH[n] = i
