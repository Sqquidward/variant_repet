def f_maxN():
    summa, count = 0, 0
    for i in range(len(list)):
        if summa > int(max):
            return count-1
        else:
            summa += list[i]
            count += 1
    return count


def f_maxSum():
    n = f_maxN()
    sum  = 0
    for i in range(n-1):
        sum += list[i]
    for j in range(1000):
        sum += list[n-1+j]
        if sum > int(max):
            return list[n-1+j]

file = open('26.txt')
max, n = file.readline().split()
list = []
for i in range(int(n)):
    list.append(int(file.readline()))


list = sorted(list)
print(f_maxN(), f_maxSum())




