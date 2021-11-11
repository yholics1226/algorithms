# [프로그래머스] 모의고사 (Lv.1)

def solution(answers):
    answer = []
    score = [0] * 4
    ans1 = [1, 2, 3, 4, 5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == ans1[i % 5]:
            score[1] += 1
        if answers[i] == ans2[i % 8]:
            score[2] += 1
        if answers[i] == ans3[i % 10]:
            score[3] += 1

    m = max(score)
    for i in range(1, 4):
        if score[i] == m:
            answer.append(i)

    return answer
    
