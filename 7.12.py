import re
print("Введите слово 'stop' для получения результата")
summa = 0
p=re.compile(r"^[-]?[0-9]+$", re.S)
while True:
    x=input("Введите число: ")
    x=x.rstrip("\r")
    if x == "stop":
            break
    if not p.search(x):
        print("Необходим ввести число, а не строку!")
        continue
    x=int(x)
    summa += x
print("Сумма чисел равна:", summa)
input()
