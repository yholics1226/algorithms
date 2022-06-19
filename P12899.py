# [124 나라의 숫자] https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''
    digits = ['1', '2', '4']
    while n:
        n -= 1
        answer = digits[n % 3] + answer
        n //= 3
    return answer
