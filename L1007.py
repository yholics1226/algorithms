# [Minimum Domino Rotations For Equal Row] https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

def minDominoRotations(tops, bottoms):
    ans = len(tops)
    for i in {tops[0], bottoms[0]}:
        ct = cb = 0
        for t, b in zip(tops, bottoms):
            if t != i and b != i:
                break
            if b != i:
                cb += 1
            if t != i:
                ct += 1
        else:
            ans = min(ct, cb)
    return ans if ans < len(tops) else -1
