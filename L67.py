# [Add Binary] https://leetcode.com/problems/add-binary/

def addBinary(a, b):
    ans = ''
    la, lb = len(a), len(b)
    if la > lb:
        b = '0' * (la - lb) + b
    else:
        a = '0' * (lb - la) + a
    ru = 0
    for i in range(len(a)-1, -1, -1):
        tmp = int(a[i]) + int(b[i]) + ru
        if tmp > 1:
            ru = 1
            tmp %= 2
        else:
            ru = 0
        ans = str(tmp) + ans
    if ru:
        ans = '1' + ans
    return ans
