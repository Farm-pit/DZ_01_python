# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть


n = int(input("Введите количество монеток: ")) 
eagle = 0 
tails = 0 
for i in range(n): 
    coin = int(input("Напишите какой они лежат, использую 1 и 0: ")) 
    if coin == 1: 
        eagle += 1 
    else: 
        tails += 1 
print(min(eagle, tails))
