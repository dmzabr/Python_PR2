import random


print("Введите количество монет")
n = int(input())
coin = []

#1 - орел
#0 - решка

for i in range (n):
    res = random.getrandbits(1)
    coin.append("Орел") if res == 1 else coin.append("Решка")
    
print(coin)

if coin.count("Орел") > coin.count("Решка"):
    print("Число переворачиваний - ", coin.count("Решка"))
else:
    print("Число переворачиваний - ", coin.count("Орел"))
