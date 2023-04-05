def f(a, b):
    if a == b:
        return 1
    elif a > b or a == 14:
        return 0
    else:
        return f(a+1, b) + f(a+2, b)

print(f(2, 9) * f(9, 18))