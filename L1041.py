# [Robot Bounded in Circle] https://leetcode.com/problems/robot-bounded-in-circle/

def isRobotBounded(instructions):
    x, y = 0, 0
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    k = 0
    for inst in instructions:
        if inst == 'L':
            k = (k + 1) % 4
        elif inst == 'R':
            k = (k - 1) % 4
        else:
            x += dx[k]
            y += dy[k]
    if x == 0 and y == 0:
        return True
    elif k != 0:
        return True
    else:
        return False

# another solution
def isRobotBounded(instructions):
    x, y = 0, 0
    dx, dy = 0, 1
    for inst in instructions:
        if inst == 'L':
            dx, dy = -dy, dx
        elif inst == 'R':
            dx, dy = dy, -dx
        else:
            x += dx
            y += dy
    return (x, y) == (0, 0) or (dx, dy) != (0, 1)
