flag = 0
max = 0
for i in range(9):
    number = int(input())
    if number > max:
        max = number
        flag = i+1
print(max, flag)