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

# using SortedList (faster)
from sortedcontainers import SortedList
def countSmaller(nums):
    ans = []
    s = SortedList()
    for num in nums[::-1]:
        i = SortedList.bisect_left(s, num)
        ans.append(i)
        s.add(num)
    return ans[::-1]
