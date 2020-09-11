import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
for i in range(0, 5):
    h, m, s = [int(s) for s in input().split()]
    if (h > -1) and (h < 24) and (m > -1) and (m < 60) and(s > -1) and (s < 60):
        print('YES')
    else:
        print('NO')
    