print("Введите сумму двух чисел")
sum = int(input())

print("Введите произведение двух чисел")
mnoj = int(input())

for i in range (1000):
    for j in range(1000):
        if (i + j == sum) and (i * j) == mnoj:
            print(i, j)