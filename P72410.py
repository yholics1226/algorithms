# [신규 아이디 추천] https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    # 1
    answer = new_id.lower()
    # 2
    tmp = []
    for x in answer:
        if x in {'-', '_', '.'} or x.isalnum():
            tmp.append(x)
    # 3
    i = 0
    while i < len(tmp):
        if tmp[i] != '.':
            i += 1
            continue
        else:
            j = 1
            while i+j < len(tmp) and tmp[i+j] == '.':
                tmp[i+j] = ''
                j += 1
            i = i + j
    # 4
    if tmp[0] == '.':
        tmp[0] = ''
    if tmp[-1] == '.':
        tmp[-1] = ''
    answer = ''.join(tmp)
    # 5
    if not answer:
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer

# regular expression
import re
def solution(new_id):
    # 1
    answer = new_id.lower()
    # 2
    answer = re.sub('[^a-z0-9-_.]', '', answer)
    # 3
    answer = re.sub('\.+', '.', answer)
    # 4
    answer = re.sub('^\.|\.$', '', answer)
    # 5
    if not answer:
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = re.sub('\.$', '', answer[:15])
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer
