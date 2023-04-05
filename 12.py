minimum = 10**10
for i in range(200, 10000):
    str = '1' * i


    while '1111' in str:
        str = str.replace('1111', '22')
        str = str.replace('222', '1')
    print(i, str)


