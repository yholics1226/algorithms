# [Broken Calculator] https://leetcode.com/problems/broken-calculator/

def brokenCalc(startValue, target):
    ans = 0
    while startValue < target:
        ans += 1
        if target % 2:
            target += 1
        else:
            target //= 2
    return ans + startValue - target
