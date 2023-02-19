# 종종 잊어버리는 것들

### if & for in list comprehension
```[조건o 출력값 for thing in things if 조건]```
### if & else & for in list comprehension
```[조건o 출력값 if 조건 else 조건x 출력값 for thing in thigs]```

### delimiter로 구분된 문자열 출력 / 괄호 없이 리스트 출력
,로 구분된 문자열 출력: 

```print(', '.join(str_list))``` 

공백으로 구분된 문자열 출력:

```print(' '.join(str_list))```