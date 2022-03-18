# [Score of Parentheses] https://leetcode.com/problems/score-of-parentheses/

def scoreOfParentheses(s):
    stack = [0]
    for x in s:
        if x == '(':
            stack.append(0)
        else:
            a = stack.pop()
            stack[-1] += 2*a or 1
    return stack[0]
