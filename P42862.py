# [체육복] https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    ch = [1] * n
    for x in lost:
        ch[x-1] -= 1
    for x in reserve:
        ch[x-1] += 1
    for i in range(n):
        if ch[i] == 2:
            if i > 0 and ch[i-1] == 0:
                ch[i], ch[i-1] = 1, 1
            elif i < n-1 and ch[i+1] == 0:
                ch[i], ch[i+1] = 1, 1
    for x in ch:
        if x > 0:
            answer += 1
    return answer
