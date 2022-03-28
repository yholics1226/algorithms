# [피보나치 수 6] https://www.acmicpc.net/problem/11444

# using linear algebra:
# F(n+2) = F(n+1) + F(n) => [[F(n+2)],[F(n+1)]] = [[1,1],[1,0]][[F(n+1)],[F(n)]]
# => [[F(n+2),F(n+1)],[F(n+1),F(n)]] = [[1,1],[1,0]][[F(n+1),F(n)],[F(n),F(n-1)]]
#     = ... = [[1,1],[1,0]]^n [[F(2),F(1)],[F(1),F(0)]] = [[1,1],[1,0]]^(n+1)
# => [[F(n+1),F(n)],[F(n),F(n-1)]] = [[1,1],[1,0]]^n (n > 0)
def mul(A, B):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += A[i][k] * B[k][j]
            res[i][j] %= 1000000007
    return res
def fib(M, n):
    if n == 1:
        return M
    if n % 2:
        return mul(M, fib(M, n-1))
    return fib(mul(M, M), n // 2)
n = int(input())
print(fib([[1, 1], [1, 0]], n)[0][1])

# using d'Ocagne's identity
f = {1: 1, 2: 1, 3: 2}
def fib(n):
    if n in f:
        return f[n]
    k = n//2
    f[n] = (fib(k-1) * fib(n-k) + fib(k) * fib(n-k+1)) % 1000000007
    return f[n]
n = int(input())
print(fib(n))
