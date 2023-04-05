def f(i, n):
    list = '0123456789abcdef'
    b = ''
    while i > 0:
        b += list[i % n]
        i //= n
    return b[::-1]







primer =  4**34 + 5 * 4**22 + 4**13 + 2 * 4*9 + 82


print(set(f(primer, 16)))