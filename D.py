import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
ch = int(input())
if ch > 1:
    if ch % 2 == 0:
        print('YES')
        print(ch + 2)
    else:
        print('NO')
        print(ch + 1)
else:
    print('NO')
    print('2')