# [Robot Bounded in Circle] https://leetcode.com/problems/robot-bounded-in-circle/

def isRobotBounded(instructions):
    cx, cy = 0, 0
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    pts = {(0, 0)}
    k = 0
    for _ in range(4):
        for x in instructions:
            if x == 'G':
                cx += dx[k]
                cy += dy[k]
            elif x == 'L':
                k = (k + 1) % 4
            else:
                k = (k - 1) % 4
        if (cx, cy) in pts:
            return True
        else:
            pts.add((cx, cy))
    return False
