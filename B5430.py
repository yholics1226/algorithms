# [AC] https://www.acmicpc.net/problem/5430

from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    p = input().rstrip()
    if input() == '0\n' and 'D' in p:
        input()
        print('error')
    else:
        flag = 0
        x = deque(input()[1:-2].split(','))
        for c in p:
            if c == 'R':
                flag = 1 - flag
            elif x:
                if flag:
                    x.pop()
                else:
                    x.popleft()
            else:
                print('error')
                break
        else:
            if flag:
                x.reverse()
            print('[' + ','.join(x) + ']')
