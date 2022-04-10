# [Baseball Game] https://leetcode.com/problems/baseball-game/

def calPoints(ops):
    stack = []
    for x in ops:
        if x == "+":
            stack.append(stack[-1] + stack[-2])
        elif x == "D":
            stack.append(stack[-1] * 2)
        elif x == "C":
            stack.pop()
        else:
            stack.append(int(x))
    return sum(stack)
