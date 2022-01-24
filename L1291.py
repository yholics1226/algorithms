# [Sequential Digits] https://leetcode.com/problems/sequential-digits/

def sequentialDigits(low, high):
    ans = []
    for x in range(1, 9):
        while x <= high:
            r = x % 10
            if r == 0:
                break
            if x >= low:
                ans.append(x)
            x = x * 10 + r + 1
    return sorted(ans)
