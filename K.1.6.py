sp = []
a, b = [int(s) for s in input().split()]
for i in range(0, a):
    read_sp = []
    for j in range(0, b):
        read = int(input())
        read_sp.append(read)
    sp.append(read_sp)
    
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
min_sp = []
max_sp = []
for i in range(0, a):
    min_sp.append(sp[i][min_number])
    max_sp.append(sp[i][max_number])

for i in range(0, a):
    sp[i][max_number] = min_sp[i]
    sp[i][min_number] = max_sp[i]

print(sp)