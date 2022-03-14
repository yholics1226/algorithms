# [Valid Parentheses] https://leetcode.com/problems/valid-parentheses/

def isValid(s):
    pair = {')': '(', '}': '{', ']': '['}
    stack = []
    for p in s:
        if p in '({[':
            stack.append(p)
        elif stack and stack[-1] == pair[p]:
            stack.pop()
        else:
            return False
    return not stack
