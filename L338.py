# [Counting Bits] https://leetcode.com/problems/counting-bits/

# O(n log n)
def countBits(n):
    ans = []
    for i in range(n+1):
        num, res = i, 0
        while num:
            res += num % 2
            num //= 2
        ans.append(res)
    return ans

# O(n)
def countBits(n):
    ans = [0]
    while len(ans) <= n:
        ans += [x+1 for x in ans]
    return ans[:n+1]
