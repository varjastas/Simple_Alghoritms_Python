import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

ch = input()
if (ch == '0') or (ch == '-0'):
    print(0)
    sys.exit()
n = 0
listch = list(ch)

if listch[0] == '-':
    minus = True
    del listch[0]
else:
    minus = False

listch = listch[::-1]

ch = ''.join(listch)
for i in ch:
    if i == '0':
        n += 1
    if i != '0':
        break

if minus == True:
    final_ch = '-' + ch[n::]
else:
    final_ch = ch[n::]
    
print(final_ch)