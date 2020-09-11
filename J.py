import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
#Создание списка из символов
g = input()
#При создании списка таким способом, от множественных пробелов остаётся лишь пустой символ
q = g.split(' ')
# Создание счётчика слов
y = 0
#Нахождение слов-палиндромов(срезка с шагом -1 делает reverse слова)
for i in range(0, len(q)):
    if (q[i] != '') and (q[i][::-1] == q[i]):
        y += 1
print(y)