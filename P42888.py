# [오픈채팅방] https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    dic = dict()
    for r in record:
        if r[0] != 'L':
            dic[r.split()[1]] = r.split()[2]
    for r in record:
        if r[0] == 'E':
            answer.append(dic[r.split()[1]] + "님이 들어왔습니다.")
        elif r[0] == 'L':
            answer.append(dic[r.split()[1]] + "님이 나갔습니다.")
    return answer
