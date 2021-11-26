# [큰 수 만들기] https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = []
    n = len(number)
    for i in range(n):
        while answer and answer[-1] < number[i]:
            answer.pop()
            k -= 1
            if k == 0:
                break
        answer.append(number[i])
        if k == 0:
            if i < n-1:
                answer += number[i+1:]
            break
    while k != 0:
        answer.pop()
        k -= 1
    return ''.join(answer)
