# [곱셈] https://www.acmicpc.net/problem/1629

a, b, c = map(int, input().split())
a %= c
if a == 0:
    print(0)
else:
    x = 1
    while b:
        if b % 2:
            x = (x * a) % c
        b //= 2
        a = (a * a) % c
    print(x)

# using bitwise operation (faster)
a, b, c = map(int, input().split())
a %= c
if a == 0:
    print(0)
else:
    x = 1
    while b:
        if b & 1:
            x = (x * a) % c
        b >>= 1
        a = (a * a) % c
    print(x)

# Actually, there is a built-in function pow()
a, b, c = map(int, input().split())
print(pow(a, b, c))

'''
+) In general, it is known that:
    when dealing with large numbers and parallel modulus, pow() is more efficient,
    however when dealing with smaller numbers without modulus, ** is more efficient.
'''

# using my own pow() function
def myPow(x, y, z):
    if y == 1:
        return x % z
    tmp = myPow(x, y >> 1, z)
    if y & 1:
        return x * tmp * tmp % z
    else:
        return tmp * tmp % z
a, b, c = map(int, input().split())
print(myPow(a, b, c))
