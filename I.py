import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
#Создание переменных
g = input()
q = g.split(' ')
#Создание счётчика не слов
y = 0
for i in range(0, len(q)):
    #Если найдено не слово(пустое место) - длина -1
    if q[i] == '':
        y += 1
print(len(q) - y)