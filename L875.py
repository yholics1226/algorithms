# [Koko Eating Bananas] https://leetcode.com/problems/koko-eating-bananas/

def minEatingSpeed(piles, h):
    def count(k):
        cnt = 0
        for x in piles:
            cnt += (x - 1) // k + 1
        return cnt
    lt, rt = 1, sum(piles)
    while lt <= rt:
        mid = (lt + rt) // 2
        if count(mid) <= h:
            ans = mid
            rt = mid -1
        else:
            lt = mid + 1
    return ans
