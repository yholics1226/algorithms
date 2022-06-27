# [Maximum Points You Can Obtain from Cards] https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

def maxScore(cardPoints, k):
    n = len(cardPoints) - k
    exclude = sum(cardPoints[:n])
    res = exclude
    for i in range(k):
        exclude += cardPoints[n+i] - cardPoints[i]
        res = min(res, exclude)
    return sum(cardPoints) - res
