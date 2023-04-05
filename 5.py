def f(n):
    n_2 =bin(n)[2:]
    if n % 2 == 0:
        return int('1' + n_2 + '0', 2)
    return int('11' + n_2 + '11', 2)

for i in range(100):
    answer = f(i)
    if answer > 52:
        print(answer)
        break
