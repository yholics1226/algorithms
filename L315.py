# [Count of Smaller Numbers After Self] https://leetcode.com/problems/count-of-smaller-numbers-after-self/

from bisect import bisect_left
def countSmaller(nums):
    ans = []
    tmp = sorted(nums)
    for num in nums:
        i = bisect_left(tmp, num)
        ans.append(i)
        del tmp[i]
    return ans
