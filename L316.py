# [Remove Duplicate Letters] https://leetcode.com/problems/remove-duplicate-letters/

def removeDuplicateLetters(s):
    pos = {x: i for i, x in enumerate(s)}
    stack = []
    for i, x in enumerate(s):
        if x not in stack:
            while stack and stack[-1] > x and pos[stack[-1]] > i:
                stack.pop()
            stack.append(x)
    return ''.join(stack)
