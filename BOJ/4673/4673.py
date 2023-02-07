# 문제 -> N 까지의 self number 출력
# 1~N list
# 자리수 더한 수 만들어서 list에서 빼기
# 남은 수가 self numbers

# N=100으로 테스트 해보기
N = 10000
_set = set([i for i in range(N)])

for i in range(N):
    str_i = str(i)
    dn = 0
    dn += i
    for j in range(len(str_i)):
        dn += int(str_i[j])
    _set.discard(dn)

_list = list(_set)
for i in range(len(_list)):
    print(_list[i])
