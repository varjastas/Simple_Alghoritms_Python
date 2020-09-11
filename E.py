import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
sp = []
i = 0
posl = 1
spposl = []
while i < 10001:
    sp.append(int(input()))
    if i > 0:
        if (sp[i] == 0) and (sp[i - 1] == 0):
            del sp[i], sp[i - 1]
            break
    i += 1
if len(sp) == 0:
    print(0)
else:
    for n in range(1, len(sp)):
        if sp[n] == sp[n - 1]:
            posl += 1
        else:
            spposl.append(posl)
            posl = 1
            continue
    spposl.append(posl)
    print(max(spposl))