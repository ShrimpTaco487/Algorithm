N = int(input())
l = list(map(int,input().split(' ')))
v = int(input())
print(sum([True if v == i else False for i in l]))