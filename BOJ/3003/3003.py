# import sys
# from operator import sub
#
# gijun = [1,1,2,2,2,8]
# k,q,l,b,kn,p = map(int, sys.stdin.readline().split(' '))
# a = [k,q,l,b,kn,p]
#
# print(' '.join(list(map(str,map(sub, gijun,a)))))
#
#
#

k, q, l, b, kn, p = map(int, input().split(' '))
print(1-k, 1-q, 2-l, 2-b, 2-kn, 8-p)
