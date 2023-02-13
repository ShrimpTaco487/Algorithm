N = int(input())

def is_han(n: str):
    if len(n) <= 2:
        return True
    else:
        for i in range(len(n)-2):
            if int(n[i])-int(n[i+1]) == int(n[i+1])-int(n[i+2]):
                pass
            else:
                return False
        return True

ans = 0
for i in range(1,N+1):
    if is_han(str(i)):
        ans +=1
print(ans)

