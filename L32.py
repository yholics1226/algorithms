# [Longest Valid Parentheses] https://leetcode.com/problems/longest-valid-parentheses/

def longestValidParentheses(s):
    stack = [-1]
    ans = 0
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                ans = max(ans, i - stack[-1])
    return ans
