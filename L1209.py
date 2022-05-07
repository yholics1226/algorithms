# [Remove All Adjacent Duplicates in String II] https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

def removeDuplicates(s, k):
    stack = [('', 0)]
    for c in s:
        x, y = stack[-1]
        if c != x:
            stack.append((c, 1))
        elif y+1 == k:
            for _ in range(y):
                stack.pop()
        else:
            stack.append((c, y+1))
    return ''.join([x for x, y in stack])
