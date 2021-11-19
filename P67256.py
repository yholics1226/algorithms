# [키패드 누르기] https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    lf, rf = [3, 0], [3, 2]
    for i in range(len(numbers)):
        x = (numbers[i] - 1) // 3
        y = (numbers[i] - 1) % 3
        if numbers[i] == 0:
            x, y = 3, 1
        if numbers[i] in [1, 4, 7]:
            answer += 'L'
            lf = [x, y]
        elif numbers[i] in [3, 6, 9]:
            answer += 'R'
            rf = [x, y]
        else:
            if abs(x - lf[0]) + abs(y - lf[1]) < abs(x - rf[0]) + abs(y - rf[1]):
                answer += 'L'
                lf = [x, y]
            elif abs(x - lf[0]) + abs(y - lf[1]) > abs(x - rf[0]) + abs(y - rf[1]):
                answer += 'R'
                rf = [x, y]
            else:
                if hand == 'left':
                    answer += 'L'
                    lf = [x, y]
                else:
                    answer += 'R'
                    rf = [x, y]
    return answer
  
# 과정 출력 버전
def sol(numbers, hand):
    answer = ''
    lf, rf = [3, 0], [3, 2]
    for i in range(len(numbers)):
        x = (numbers[i] - 1) // 3
        y = (numbers[i] - 1) % 3
        if numbers[i] == 0:
            x, y = 3, 1
        print(f'lf: {lf}, rf: {rf}, target: {numbers[i]} = [{x}, {y}]')
        if numbers[i] in [1, 4, 7]:
            answer += 'L'
            lf = [x, y]
        elif numbers[i] in [3, 6, 9]:
            answer += 'R'
            rf = [x, y]
        else:
            if abs(x - lf[0]) + abs(y - lf[1]) < abs(x - rf[0]) + abs(y - rf[1]):
                answer += 'L'
                lf = [x, y]
            elif abs(x - lf[0]) + abs(y - lf[1]) > abs(x - rf[0]) + abs(y - rf[1]):
                answer += 'R'
                rf = [x, y]
            else:
                if hand == 'left':
                    answer += 'L'
                    lf = [x, y]
                else:
                    answer += 'R'
                    rf = [x, y]
        print(f'=> {answer[-1]}')
    return answer
