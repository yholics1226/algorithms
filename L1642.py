# [Furthest Building You Can Reach] https://leetcode.com/problems/furthest-building-you-can-reach/

import heapq
def furthestBuilding(heights, bricks, ladders):
    minH = []
    n = len(heights)
    for i in range(n-1):
        diff = heights[i+1] - heights[i]
        if diff <= 0:
            continue
        heapq.heappush(minH, diff)
        if len(minH) > ladders:
            bricks -= heapq.heappop(minH)
            if bricks < 0:
                return i
    return n-1
