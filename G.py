import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array [1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
N = int(input())
g = [int(s) for s in input().split()]
g = quicksort(g)
for i in range(0, N):
    print(g[i])