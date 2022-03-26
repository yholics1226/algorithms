# [후위 표기식] https://www.acmicpc.net/problem/1918

d = {'+': 3, '-': 3, '*': 2, '/': 2, '(': 1}
ans = ''
ops = []
for x in input():
    if x == ')':
        while ops[-1] != '(':
            ans += ops.pop()
        ops.pop()
    elif x in d:
        while ops and d[ops[-1]] <= d[x] and ops[-1] != '(':
            ans += ops.pop()
        ops.append(x)
    else:
        ans += x
while ops:
    ans += ops.pop()
print(ans)
