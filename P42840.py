# [모의고사] https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    score = [0] * 4
    ans1 = [1, 2, 3, 4, 5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, ans in enumerate(answers):
        if ans == ans1[i % 5]:
            score[1] += 1
        if ans == ans2[i % 8]:
            score[2] += 1
        if ans == ans3[i % 10]:
            score[3] += 1
    m = max(score)
    for i in range(1, 4):
        if score[i] == m:
            answer.append(i)
    return answer
