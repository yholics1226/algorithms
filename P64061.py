# [크레인 인형뽑기 게임] https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    n = len(board)
    basket = [0]
    for x in moves:
        for i in range(n):
            if board[i][x-1] != 0:
                if board[i][x-1] == basket[-1]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(board[i][x-1])
                board[i][x-1] = 0
                break
    return answer
