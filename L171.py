# [Excel Sheet Column Number] https://leetcode.com/problems/excel-sheet-column-number/

def titleToNumber(columnTitle):
    ans = 0
    for ct in columnTitle:
        ans = ans * 26 + ord(ct) - 64
    return ans
