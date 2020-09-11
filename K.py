# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
#Инициализация переменных
sp = []
a, b = [int(s) for s in input().split()]
for i in range(0, a):
    read = [int(s) for s in input().split()]
    sp.append(read)

#Нахождения максимума и минимума и их номеров их столбцов
maxx = int(sp[0][0])
minn = int(sp[0][0])
min_number = 0
max_number = 0
for j in range(0, b):
    for i in range(0, a):
        if maxx <= sp[i][j]:
            maxx = int(sp[i][j])
            max_number = j
        if minn > sp[i][j]:
            minn = int(sp[i][j])
            min_number = j
# Создание списка в виде минимального и максимального столбца для их смены в новом списке
min_sp = []
max_sp = []
for i in range(0, a):
    min_sp.append(sp[i][min_number])
    max_sp.append(sp[i][max_number])

#Смена максимума и минимума
for i in range(0, a):
    sp[i][max_number] = min_sp[i]
    sp[i][min_number] = max_sp[i]

print(sp)