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

# bit 연산 이용
def solution(x, y):
    res = (bin(x ^ y))[2:]
    answer = 0
    for x in res:
        if x == '1':
            answer += 1
    return answer
