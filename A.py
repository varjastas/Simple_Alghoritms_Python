# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
dovg, shir, vis = [int(s) for s in input().split()]
shirrul, dovgrul = [int(s) for s in input().split()]
shirrul = shirrul / 1000 * 0.9
dovgrul = dovgrul / 1000 * 0.9
plosh = (2 * (dovg * shir) +  2 * (dovg * vis)  + (shir * vis)) * 0.85
ploshodnrul = shirrul * dovgrul 
kolrul = plosh / ploshodnrul
if int(kolrul) == kolrul:
    print(kolrul)
else:
    print(int(kolrul) + 1)