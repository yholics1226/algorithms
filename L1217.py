# [Minimum Cost to Move Chips to The Same Position] https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

def minCostToMoveChips(position):
    odd, even = 0, 0
    for x in position:
        if x % 2:
            odd += 1
        else:
            even += 1
    return min(odd, even)
