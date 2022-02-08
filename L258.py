# [Add Digits] https://leetcode.com/problems/add-digits/

def addDigits(num):
    while num > 9:
        tmp= 0
        while num:
            tmp += num % 10
            num //= 10
        num = tmp
    return num

# anoher solution
def addDigits(num):
    if num == 0:
        return 0
    elif num % 9:
        return num % 9
    else:
        return 9

# another solution
def addDigits(num):
    if num == 0:
        return 0
    else:
        return 1 + (num - 1) % 9
