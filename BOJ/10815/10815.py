n = int(input())

s_cards = list(map(int, input().split(' ')))
dict={}
for i in range(n):
    dict[s_cards[i]]=True

m = int(input())
cards = list(map(int, input().split(' ')))

for card in cards:
    try:
        if dict[card]:
            print(1)
    except:
        print(0)
