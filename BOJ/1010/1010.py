import sys
T = int(input())
for t in range(T):
    a, b = map(int, sys.stdin.readline().split(' '))
    head = 1
    feet = 1
    for i in range(min(a,b)):
        head *= (max(a,b)-i)
        feet *= (min(a,b)-i)
    print(head//feet)