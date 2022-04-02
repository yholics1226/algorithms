# [Split Array Largest Sum] https://leetcode.com/problems/split-array-largest-sum/

def splitArray(nums, m):
    def chk(lim):
        cnt, tmp = 1, 0
        for n in nums:
            if tmp + n > lim:
                cnt += 1
                tmp = 0
            tmp += n
        return cnt > m
    lo, hi = max(nums), sum(nums)
    while lo <= hi:
        mid = (lo + hi) // 2
        if chk(mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return lo
