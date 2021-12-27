# [Number Complement] https://leetcode.com/problems/number-complement/

def findComplement(num):
    return 2**(len(bin(num))-2)-1-num

# bit manipulation
def findComplement(num):
    n = num.bit_length()
    mask = (1 << n) - 1
    return num ^ mask
