# [거리두기 확인하기] https://programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    answer = []
    dx = [0, 1, 1, 1]
    dy = [1, 0, -1, 1]

    def chk(place, x, y):
        for i in [0, 1]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] == 'P':
                return 0
            if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] == 'O':
                nnx = nx + dx[i]
                nny = ny + dy[i]
                if 0 <= nnx < 5 and 0 <= nny < 5 and place[nnx][nny] == 'P':
                    return 0
        for i in [2, 3]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] == 'P' and (place[x][ny] == 'O' or place[nx][y] == 'O'):
                return 0
        return 1

    for place in places:
        flag = 1
        for x in range(5):
            if flag == 0:
                break
            for y in range(5):
                if flag == 0:
                    break
                if place[x][y] == 'P':
                    flag = chk(place, x, y)
        answer.append(flag)

    return answer
