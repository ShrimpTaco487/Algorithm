import sys

N = int(input())
S, G, P, D = map(int, sys.stdin.readline().split(' '))
str_grade = input()

result = 0
last_result = 0
for i in range(N):
    grade = str_grade[i]

    if grade == 'B':
        tmp_result = S - 1 - last_result
    elif grade == 'S':
        tmp_result = G - 1 - last_result
    elif grade == 'G':
        tmp_result = P - 1 - last_result
    elif grade == 'P':
        tmp_result = D - 1 - last_result
    elif grade == 'D':
        tmp_result = D

    last_result = tmp_result
    result += tmp_result
print(result)