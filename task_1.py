num = int(input("Введите число"))
number = 0
while num >= 1:
    number = num % 10 + number
    num = num // 10
print(number)