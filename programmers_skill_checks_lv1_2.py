def solution(participant, completion):
    import collections
    pH = collections.Counter(participant)
    cH = collections.Counter(completion)
    for x in pH:
        if pH[x] != cH[x]:
            answer = x
    return answer
