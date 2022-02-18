# [Remove K Digits] https://leetcode.com/problems/remove-k-digits/

def removeKdigits(num, k):
    stack = []
    for n in num:
        while stack and k and stack[-1] > n:
            stack.pop()
            k -= 1
        stack.append(n)
    while k:
        stack.pop()
        k -= 1
    ans = ''.join(stack) if stack else '0'
    return str(int(ans))

# another solution
import re
def removeKdigits(num, k):
    stack = []
    for n in num:
        while stack and k and stack[-1] > n:
            stack.pop()
            k -= 1
        stack.append(n)
    stack = stack[:-k] if k else stack
    ans = ''.join(stack)
    ans = re.sub('^0+', '', ans)
    return ans if ans else '0'
