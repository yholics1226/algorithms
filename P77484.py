# [로또의 최고 순위와 최저 순위] https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = [0, 0]
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt = len(set(lottos) & set(win_nums))
    answer[1] = rank[cnt]
    cnt += lottos.count(0)
    answer[0] = rank[cnt]
    return answer
