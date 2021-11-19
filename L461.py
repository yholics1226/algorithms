# [Hamming Distance] https://leetcode.com/problems/hamming-distance/

def hammingDistance(x, y):
    answer = 0
    a, b = max(x, y), min(x, y)
    while a:
        if a % 2 != b % 2:
            answer += 1
        a = a // 2
        b = b // 2
    return answer
