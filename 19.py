def f(a, b, n):
    if a + b >= 75 and n == 2:
        return True
    elif a + b >= 75 and n < 2:
        return False
    elif a + b < 75 and n == 2:
        return False
    else:
        return f(a + 1, b, n + 1) or f(a + b, b, n + 1) or f(a, b + 1, n + 1) or f(a, b + a, n + 1)


for i in range(1, 68):
    if f(7, i, 0):
        print(f'Answer: {i}')
        break