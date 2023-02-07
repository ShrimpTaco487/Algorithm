import sys

N = int(sys.stdin.readline())

for i in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split(' '))

    if (x1,y1,r1) == (x2,y2,r2):
        print(-1)
        continue
    ab = pow(pow(x1-x2,2) + pow(y1-y2,2),1/2)
    # ab>=r_max
    if ab>=max(r1,r2):
        if ab > r1+r2:
            print(0)
        elif ab == r1+r2:
            print(1)
        else: # ab < r1+r2
            print(2)
    # ab<r_max
    else: # ab<max(r1,r2)
        if ab < max(r1,r2)-min(r1,r2):
            print(0)
        elif ab == max(r1,r2)-min(r1,r2):
            print(1)
        else: # ab > max(r1,r2)-min(r1,r2):
            print(2)





