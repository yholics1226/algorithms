# [Min Cost to Connect All Points] https://leetcode.com/problems/min-cost-to-connect-all-points/

import heapq
def minCostConnectPoints(points):
    n = len(points)
    unf = [i for i in range(n)]
    ans = cnt = 0
    def find(v):
        if v == unf[v]:
            return v
        else:
            unf[v] = find(unf[v])
            return unf[v]
    def dist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    hq = []
    for i in range(n):
        for j in range(i+1, n):
            heapq.heappush(hq, [dist(points[i], points[j]), i, j])
    while cnt < n-1:
        d, a, b = heapq.heappop(hq)
        fa, fb = find(a), find(b)
        if fa != fb:
            unf[fb] = fa
            cnt += 1
            ans += d
    return ans
