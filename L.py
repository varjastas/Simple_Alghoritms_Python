import copy
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
#Сортировка массивва
#Элементы инициализации
#Функция быстрой сортировки
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array [1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
#Объявление переменных
newsp = []
norm_str_sp = []
sp = []
spnorm = []
norm = 0

#Запрос данных и наход нормы
a, b = [int(s) for s in input().split()]
for i in range(0, a):
    read = [int(s) for s in input().split()]
    read_copy_for_norm  = list(map(abs, read))
    norm = 0
    for i1 in read_copy_for_norm:
        for i2 in str(i1):
            norm += int(i2)

    spnorm.append(norm)
    sp.append(read)

#Объявление сортированной формы
spnorm_sorted = quicksort(spnorm)

#Объявляем переменные для следующих действий
kolsm = 0
i5 = 0
i4 = 0
spnorm_sorted_copy_for_while = copy.copy(spnorm_sorted)
spnorm_copy_for_while = copy.copy(spnorm)

#Создаём список, в котором идут отношения норма в несортированном списке - норма в сортированном списке
#Норма сортированного списка: норма несортированного списка
#Ищем норму несортированного списка и вставляем его в список строк, с сортированием по норме
#Сортировка по уменьшению
while len(spnorm_sorted_copy_for_while) != 0:
    while spnorm_sorted_copy_for_while[i5] != spnorm_copy_for_while[i4]:
        i4 += 1

    norm_str_sp.append(i4)
    spnorm_sorted_copy_for_while.pop(0)
    spnorm_copy_for_while[i4] = 1000000000
    i5 = 0
    i4 = i5

#Создаём новый список
for i in range(0, a):
    newsp.append(sp[norm_str_sp[i]])

print(newsp)