# [Minimize Deviation in Array] https://leetcode.com/problems/minimize-deviation-in-array/

import heapq
def minimumDeviation(nums):
    heapq.heapify(nums)
    nmax = max(nums)
    dev = nmax - nums[0]
    while nums[0] % 2:
        tmp = heapq.heappop(nums) * 2
        heapq.heappush(nums, tmp)
        nmax = max(nmax, tmp)
        dev = min(dev, nmax - nums[0])
    nmin = nums[0]
    nums = [-n for n in nums]
    heapq.heapify(nums)
    while nums[0] % 2 == 0:
        tmp = -heapq.heappop(nums) // 2
        heapq.heappush(nums, -tmp)
        nmin = min(nmin, tmp)
        dev = min(dev, -nums[0] - nmin)
    return dev
