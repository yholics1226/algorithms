# [Validate Stack Sequences] https://leetcode.com/problems/validate-stack-sequences/

def validateStackSequences(pushed, popped):
    stack = []
    j = 0
    for x in pushed:
        stack.append(x)
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return not stack
