# [Maximize Distance to Closest Person] https://leetcode.com/problems/maximize-distance-to-closest-person/

def maxDistToClosest(seats):
    n = len(seats)
    dist = [0] * n
    d = n
    for i in range(n):
        if seats[i] == 1:
            dist[i] = 0
            d = 0
        else:
            d += 1
            dist[i] = d
    d = n
    for i in range(n-1, -1, -1):
        if seats[i] == 1:
            d = 0
        else:
            d += 1
            dist[i] = min(dist[i], d)
    ans = max(dist)
    return ans

# another solution
def maxDistToClosest(seats):
    n = len(seats)
    ans = 0
    prev = -1
    for i in range(n):
        if seats[i]:
            d = i if prev < 0 else (i - prev) // 2
            ans = max(ans, d)
            prev = i
    ans = max(ans, n-1 - prev)
    return ans
