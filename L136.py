# [Single Number] https://leetcode.com/problems/single-number/

from collections import Counter
def singleNumber(nums):
    nH = Counter(nums)
    for x in nH:
        if nH[x] == 1:
            return x

# another solution (bit manipulation)
def singleNumber(nums):
    ans = 0
    for num in nums:
        ans ^= num
    return ans
