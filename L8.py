# [String to Integer (atoi)] https://leetcode.com/problems/string-to-integer-atoi/

import re
def myAtoi(s):
    s = re.sub('^\s+', '', s)
    sign = -1 if s and s[0] == '-' else 1
    s = re.sub('^[\-\+]', '', s)
    s = re.findall('^\d+', s)
    s = 0 if not s else int(s[0])
    s *= sign
    if s >= 2**31:
        return 2**31-1
    elif s < -2**31:
        return -2**31
    else:
        return s

# another solution
def myAtoi(s):
    s = s.strip()
    if not s:
        return 0
    sign = 1
    idx = 0
    if s[0] == '-':
        sign = -1
        idx += 1
    elif s[0] == '+':
        idx += 1
    res = 0
    for i in range(idx, len(s)):
        if s[i].isdigit():
            res = res * 10 + int(s[i])
        else:
            break
    res *= sign
    if res >= 2**31:
        return 2**31-1
    elif res < -2**31:
        return -2**31
    else:
        return res
