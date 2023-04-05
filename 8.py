from itertools import product

count = 0
for i in product('AВОРТ', repeat = 4):
    count+=1

    if ''.join(i) == 'ТAРA':
        print(count, *i)
