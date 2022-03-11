# [숫자 문자열과 영단어] https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, e in enumerate(eng):
        s = s.replace(e, str(i))
    return int(s)
