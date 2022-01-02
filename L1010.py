# [Pairs of Songs With Total Durations Divisible by 60] https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

import collections
def numPairsDivisibleBy60(time):
    nH = collections.Counter([t % 60 for t in time])
    ans = (nH[0] * (nH[0] - 1)) // 2 + (nH[30] * (nH[30] - 1)) // 2
    for i in range(1, 30):
        ans += (nH[i] * nH[60-i])
    return ans
