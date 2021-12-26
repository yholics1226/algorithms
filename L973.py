# [K Closest Points to Origin] https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
def kClosest(points, k):
    answer = []
    H = []
    for [x, y] in points:
        heapq.heappush(H, (x*x + y*y, [x, y]))
    for _ in range(k):
        answer.append(heapq.heappop(H)[1])
    return answer

# another solution
def kClosest(points, k):
    return sorted(points, key=lambda x: x[0] * x[0] + x[1] * x[1])[:k]
