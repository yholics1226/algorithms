# [Stone Game 4] https://leetcode.com/problems/stone-game-iv/

@cache
def canWin(n):
    return any(not canWin(n - m * m) for m in range(int(sqrt(n)), 0, -1))

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return canWin(n)
