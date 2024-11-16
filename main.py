#Написать программу, которая:
# - Создаёт с помощью генератора списков, список случайных целых чисел от -50 до 50 размером 25 элементов.
# - Находит количество положительных, отрицательных и нулевых элементов в списке.
# - Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
# - Выводит самое большое и самое маленькое значение
import random #Подключаем модуль рандома
spisok = [random.randint(-50, 50) for _ in range(25)] #Создаем список по условию задачи
polozh = 0 #Инициализируем счётчик положительных чисел
otric = 0 #Инициализируем счётчик отрицательных чисел
nulev = 0 #Инициализируем счётчик нулевых чисел
for intager in spisok: #Для каждого числа в списке
    if intager == 0: #Если число равно нулю
        nulev += 1 #Увеличиваем счётчик нулевых чисел на 1
    elif intager > 0: #Или если число больше 0
        polozh += 1 #Увеличиваем число положительных чисел на 1
    elif intager < 0: #Или если число меньше 0
        otric += 1 #Увеличиваем число отрицательных чисел на 1
vsego = polozh + otric + nulev #Считаем количество всех чисел
print(f"Всего положительных чисел: {polozh} {(polozh / vsego * 100)}%") #Выводим сообщение по условию задачи с положительными числами
print(f"Всего отрицательных чисел: {otric} {(otric / vsego * 100)}%") #Выводим сообщение по условию задачи с отрицательными числами
print(f"Всего нулевых чисел: {nulev} {(nulev / vsego * 100)}%") # Выводим сообщение по условию задачи с нулевыми числами
spisok.sort(reverse = True) #Сортируем список от больше к меньшему (для удобства)
print(f"Самое большое значение из списка: {spisok[0]} \nСамое маленькое значение из списка: {spisok[24]}") #Выводим самое большее и самое меньшее значение из списка