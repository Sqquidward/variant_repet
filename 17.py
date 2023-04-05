file = open('17-7.txt')
list = [int(x) for x in file]
count, mx = 0, 0
for i in range(len(list)-1):
    if list[i] % 3 == 0 or list[i+1] % 3 == 0:
        count += 1
        mx = max(mx, list[i] + list[i+1])
print(count, mx)