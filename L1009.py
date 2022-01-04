# [Complement of Base 10 Integer] https://leetcode.com/problems/complement-of-base-10-integer/
# (Almost same as 476, but this question includes 0 for the input)

def bitwiseComplement(n):
    return 2**(len(bin(n))-2)-1-n

# another solution
def bitwiseComplement(n):
    if n == 0:
        return 1
    else:
        l = n.bit_length()
        mask = (1 << l) - 1
        return n ^ mask
