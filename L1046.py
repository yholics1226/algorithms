# [Last Stone Weight] https://leetcode.com/problems/last-stone-weight/

import heapq
def lastStoneWeight(stones):
    maxH = [-stone for stone in stones]
    heapq.heapify(maxH)
    while len(maxH) > 1:
        heapq.heappush(maxH, heapq.heappop(maxH)-heapq.heappop(maxH))
    return -heapq.heappop(maxH)
