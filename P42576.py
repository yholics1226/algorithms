# [프로그래머스] 완주하지 못한 선수 (Lv.1)

def solution(participant, completion):
    import collections
    pH = collections.Counter(participant)
    cH = collections.Counter(completion)
    for x in pH:
        if pH[x] != cH[x]:
            return x
          
