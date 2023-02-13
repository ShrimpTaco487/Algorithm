n, x = map(int, input().split(' '))
l = list(map(int, input().split(' ')))
a = [str(i) for i in l if i<x]
print(' '.join(a))