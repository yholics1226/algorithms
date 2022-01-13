# [Minimum Number of Arrows to Burst Balloons] https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

def findMinArrowShots(points):
    if not points:
        return 0
    else:
        cnt = 1
        points.sort(key=lambda x: x[1])
        rt = points[0][1]
        for x in points:
            if x[0] > rt:
                rt = x[1]
                cnt += 1
        return cnt
