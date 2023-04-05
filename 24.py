file = open('24.txt')
count = 0
str = file.read()
str = str.replace('E', 'E E')
list = str.split()
count = 0
for i in list:
    flag = True
    if len(i) < 12:
        continue
    for j in range(1, len(i)-1):
        if i[j] == 'F':
            flag = False
    if flag == True:
        count += 1
print(count)




