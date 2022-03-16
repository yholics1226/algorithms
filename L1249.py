# [Minimum Remove to Make Valid Parentheses] https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

def minRemoveToMakeValid(s):
    stack = []
    rm = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if len(stack) == 0:
                rm.append(i)
                continue
            stack.pop()
    rm += stack
    ans = ''
    i = 0
    for j in rm:
        ans += s[i:j]
        i = j+1
    ans += s[i:]
    return ans
