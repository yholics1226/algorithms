# [N-Queen] https://www.acmicpc.net/problem/9663

n = int(input())
col = [False] * n
diag1 = [False] * (2*n-1)
diag2 = [False] * (2*n-1)
ans = 0
def dfs(k):
    global ans
    if k == n:
        ans += 1
    else:
        for m in range(n if k else n//2):
            if not col[m] and not diag1[k+m] and not diag2[k-m]:
                col[m] = diag1[k+m] = diag2[k-m] = True
                dfs(k+1)
                col[m] = diag1[k+m] = diag2[k-m] = False
dfs(0)
ans *= 2
if n % 2:
    m = n // 2
    col[m] = diag1[m] = diag2[-m] = True
    dfs(1)
print(ans)
