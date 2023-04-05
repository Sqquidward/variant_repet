def f(a, b, n):
    if a + b >= 75 and n == 3:
        return True
    elif a + b >= 75 and n < 3:
        return False
    elif a + b < 75 and n == 3:
        return False
    else:
        if n % 2 == 1:
            return f(a + 1, b, n + 1) and f(a + b, b, n + 1) and f(a, b + 1, n + 1) and f(a, b + a, n + 1)
        else:
            return f(a + 1, b, n + 1) or f(a + b, b, n + 1) or f(a, b + 1, n + 1) or f(a, b + a, n + 1)


for i in range(1, 68):
    if f(7, i, 0):
        print(i, end='')