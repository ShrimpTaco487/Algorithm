n, m = map(int, input().split(' '))


dict = {}

for idx in range(1, n+1):
    dict[idx] = 0
for idx in range(m):
    i, j, k = map(int, input().split(' '))
    for iidx in range(i,j+1):
        dict[iidx] = k
print(' '.join(map(str,list(dict.values()))))
