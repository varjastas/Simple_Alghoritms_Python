import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
#Создание переменных
N = int(input())
g = [int(s) for s in input().split()]
chet = []
nechet = []
#Создание списка из чётных ии нечётных элементов
for i in g:
    if i % 2 == 0:
        chet.append(i)
    else:
        nechet.append(i)
g = chet + nechet
for i in range(0, len(g)):
    g[i] = str(g[i])
ch = ' '.join(g)
print(ch)