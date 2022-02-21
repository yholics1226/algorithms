# [Majority Element] https://leetcode.com/problems/majority-element/

from collections import Counter
def majorityElement(nums):
    n = len(nums) // 2
    nH = Counter(nums)
    for k, v in nH.items():
        if v > n:
            return k

# another solution
def majorityElement(nums):
    return sorted(nums)[len(nums)//2]

# another solution
def majorityElement(nums):
    cnt = 0
    for num in nums:
        if cnt == 0:
            ans = num
        cnt += 1 if num == ans else -1
    return ans
